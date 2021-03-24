from transformers import AutoModelWithLMHead, AutoTokenizer
import torch
import arguments
import random
import os
import warnings




def game(tokenizer,model, character):                                           #start a 5 lines chat
    questions_counter = 0
    new_user_input_counter = 0
    guess = False
    while questions_counter in range(5):
        args.guessing_counter +=1
        user_guess = input("Ask me something:")                                 #get user question
        user_guess = user_guess.lower()
        print("\n")
        if user_guess== "exit":                                                 #if user want to stop the game
            exit()

        elif "what" in user_guess and "name" in user_guess:                     #if user askes the agent over his/her name
            print("No, you tell me!!","\n")

        elif "your name is" in user_guess or "you are" in user_guess:           #if the user guess the true name
            if character.lower() in user_guess:
                print("here we go!!","\n")
                args.counter = 3
                guess = True
                break
        
        else:                                                                   # if the user ask a question over the character from the series
            new_user_input_ids = tokenizer.encode(user_guess + tokenizer.eos_token, return_tensors='pt')

                                                                                 # append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if new_user_input_counter > 0 else new_user_input_ids

                                                             
            chat_history_ids = model.generate(                                   # generated a response while limiting the total chat history to 200 tokens
                bot_input_ids, max_length=200,
                pad_token_id=tokenizer.eos_token_id,  
                no_repeat_ngram_size=3,       
                do_sample=True, 
                top_k=100, 
                top_p=0.7,
                temperature = 0.8
            )

            new_user_input_counter +=1
                                                                                #print the generated answer
            print("Character:{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)),"\n")
        print("You still have ",10 - args.guessing_counter, "guesses","\n")         #remind the user with the number of the guesses left
        questions_counter += 1    
    return guess


if __name__ == '__main__':
    warnings.filterwarnings("ignore")                       #to ignore warning messages from the model and don't printed in the terminal 
    args = arguments.Args()
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")       #start the model        
    characters = ['Phoebe', 'Monica', 'Ross', 'Chandler', 'Joey', 'Rachel']
    random.shuffle(characters)
    guess = True
    for character in characters:                    #choose randomally one character and start the guessing game
        args.guessing_counter = 0
        args.counter = 0
        while args.counter < 2:                     #every chat allow the user to have only five lines so call the guessing game twice if the user didn't guess the character 
            folder= 'output-small-' + character
            model = AutoModelWithLMHead.from_pretrained(folder)
            guess = game(tokenizer,model, character)
            if guess == True:                          #if the user guess the character break the loop and move to the next character
                break
            else:
                args.counter +=1
        if guess == False:
            args.true_guesses -=1
            print("The character was ...", character)           #if the user did not manage to guess the character print the name of the character
        args.character_counter +=1
        if args.character_counter !=6:
            print("Moving to the next character","\n")
    os.system("cls")                                        #clean the terminal
    print("You have guessed", args.true_guesses, "characters out of 6")             #print the final result
    if args.true_guesses > 3:
        print("Well done")
    else:
        print("You probably need to rewatch our series again")