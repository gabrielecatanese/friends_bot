from transformers import AutoModelWithLMHead, AutoTokenizer
import torch
import arguments



def main(tokenizer,model, character):    
    # Let's chat for 5 lines
    step = 0
    guess = False
    while step in range(5):
        user_guess = input(">> User:")
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
                if user_guess[-1].lower() == character.lower():
                    print("here we go!!")
                    args.counter = 3
                    guess = True
                    break
        elif "your name" in user_guess.lower():
            print("No, you tell me!!")
        else:
            new_user_input_ids = tokenizer.encode(user_guess + tokenizer.eos_token, return_tensors='pt')
        
            # print(new_user_input_ids)

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
            print(chat_history_ids)
            # pretty print last ouput tokens from bot
            print("Friends :{}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
            step +=1
    return guess



if __name__ == '__main__':
    args = arguments.Args()
    tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
    characters = ['Phoebe', 'Monica', 'Ross', 'Chandler', 'Joey', 'Rachel']
    for character in characters:
        args.counter = 0
        while args.counter < 2:
            folder= 'output-small-' + character
            model = AutoModelWithLMHead.from_pretrained(folder)
            guess = main(tokenizer,model, character)
            if guess == True:
                break
            else:
                args.counter +=1
        print(character)