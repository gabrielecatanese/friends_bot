# The FriendsBot Project
This repository contains the code and data used for Empathic Robot Project for the VU Amsterdam course **Text Mining Domains**.

The project consisted in training 6 different conversational agents provided with human-like personality traits. By finetuning the [DialoGPT](https://github.com/microsoft/DialoGPT) coversational model over the personality charged dialog scripts of the TV series '*Friends*', we obtained an agent for each of the main characters of the show.

The contributors to this project are Wael Al-Masri, Gabriele Catanese and Breta Micha.
The project was supervised by Professor Piek Vossen.

## Folders
### friends_bot/project
This folder contains the scripts and data used for training our conversational agents.

* `arguments.py` this script defines the argument class that is imported for the training.
* `train.py` this script trains and pickles a conversational agent for each of the main characters of '*Friends*'
* `run.py` this script runs the guessing game that was used for testing the agents.

### friends_bot/project/MELD
this folder contains the '*Friends*' [MELD dataset](https://github.com/declare-lab/MELD) used for training the agents. It is splitted in training, development and test sets.

## Requirements
The required Python 3.8 packages for running the scripts contained in this repository can be found in the `requirements` file and installed directly through pip.

## Trained Agents
Running the training script is costly in terms of time and computational power. Our training time was around 8h for each run with the following setup:  
* Processor: core i7, 4.1GHz.
* RAM: ~100GB.
* Video card: GTx 1070, 8GB.  

If you want to avoid the training step, you can directly download the trained agents from the links below (2.58GB total):
* **Ross** = https://vu.data.surfsara.nl/index.php/s/Q9MdptUcIICmy0M
* **Rachel** = https://vu.data.surfsara.nl/index.php/s/1NldXCnoT3aSpcA
* **Phoebe** = https://vu.data.surfsara.nl/index.php/s/pqPDK2oXf1117Hd
* **Monica** = https://vu.data.surfsara.nl/index.php/s/XaEvDztdENFlXW9
* **Joey** = https://vu.data.surfsara.nl/index.php/s/v2gcJ46bYUSl7iP
* **Chandler** = https://vu.data.surfsara.nl/index.php/s/FbW9WqpYDeRwJC3

**These files should be located in the `project` folder with the .py files.**

## References
The code used for training was inspired by this [colab](https://colab.research.google.com/drive/15wa925dj7jvdvrz8_z3vU7btqAFQLVlG#scrollTo=78afhsngLZMw).

