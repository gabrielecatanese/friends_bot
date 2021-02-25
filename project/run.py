from transformers import AutoModelWithLMHead, AutoTokenizer
import torch
import arguments
import random
import time
import os



def main(tokenizer,model, character):    
    # Let's chat for 5 lines
    step = 0
    guess = False
    while step in range(5):
        args.guessing_counter +=1
        user_guess = input("Ask me something:")
        if user_guess.lower() == "exit":
            exit()
        if "your name is" in user_guess.lower():
            user_guess = user_guess.split("your name is")
            user_guess = user_guess[-1].split(" ")
            if "?" in user_guess[-1]:
                user_guess[-1] = user_guess[-1].split("?")
                if user_guess[-1][0].lower() == character.lower():
                    print("here we go!!")
                    args.counter = 3
                    guess = True
                    break
                else:
                    print("Try again")
                    print("You still have ",10 - args.guessing_counter, "guesses")
            else:
                if user_guess[-1].lower() == character.lower():
                    print("here we go!!")
                    args.counter = 3
                    guess = True
                    break
                else:
                    print("Try again")
                    print("You still have ",10 - args.guessing_counter, "guesses")
        elif "your name" in user_guess.lower():
            print("No, you tell me!!")
        else:
            new_user_input_ids = tokenizer.encode(user_guess + tokenizer.eos_token, return_tensors='pt')

            # append the new user input tokens to the chat history
            bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

            # generated a response while limiting the total chat history to 1000 tokens, 
            chat_history_ids = model.generate(
                bot_input_ids, max_length=200,
                pad_token_id=tokenizer.eos_token_id,  
                no_repeat_ngram_size=3,       
                do_sample=True, 
                top_k=100, 
                top_p=0.7,
                temperature = 0.8
            )
            # pretty print last ouput tokens from bot
            print("Character:{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
            step +=1
            print("You still have ",10 - args.guessing_counter, "guesses")
    return guess



def welcome():
    welcome_list = ["Hello There",
                    "The guessing game will start soon",
                    "You are allowed to ask 9 questions in order to guess which character from Friends series you are talking with" , 
                    "If you know the character you should write 'your name is' and the name of the character",
                    "If you want to exit the game, please type 'exit' in place of the question"
                    "Are you ready?",
                    "Loading... please wait"]

    for element in welcome_list:
        os.system("cls")                            #clean the terminal
        print(element)
        if len(element) > 70:
            time.sleep(7)
        else:
            time.sleep(4)
  
        

if __name__ == '__main__':
    welcome()
    args = arguments.Args()
    tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
    characters = ['Phoebe', 'Monica', 'Ross', 'Chandler', 'Joey', 'Rachel']
    random.shuffle(characters)
    guess = True
    for character in characters:
        args.guessing_counter = 0
        args.counter = 0
        while args.counter < 2:
            folder= 'output-small-' + character
            model = AutoModelWithLMHead.from_pretrained(folder)
            guess = main(tokenizer,model, character)
            if guess == True:
                break
            else:
                args.counter +=1
        if guess == False:
            args.true_guesses -=1
            print("The character was ...", character)
        args.character_counter +=1
        if args.character_counter !=6:
            print("Moving to the next character")
    os.system("cls")
    print("You have guessed", args.true_guesses, "characters out of 6")
    if args.true_guesses > 3:
        print("Well done")
    else:
        print("You probably need to rewatch our series again")