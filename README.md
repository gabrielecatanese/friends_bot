# The Friends-Bot Project
This repository contains the code and data used for Empathic Robot Project for the VU Amsterdam course **Text Mining Domains**.

The project consisted in training 6 different conversational agents provided with human-like personality traits. The agents by finetuning the DialoGPT coversational model over the scripts of the TV series '*Friends*', obtaining an agent for each of the main characters of the show.

The contributors to this project are Wael Al-Masri, Gabriele Catanese and Breta Micha.
The project was supervised by Professor Piek Vossen.

### friends_bot/project
This folder contains the scripts and data used for training our conversational agents.

`arguments.py` this script defines the argument class that is imported for the training.
`train.py` this script trains and pickles a conversational agent for each of the main characters of '*Friends*'
`run.py` this script runs the guessing game that was used for testing the agents.

#### friends_bot/project/MELD 
this folder contains the '*Friends*' [MELD dataset](https://github.com/declare-lab/MELD) used for training the agents. It is splitted in training, development and test sets.

### Requirements
These are the required Python 3.8 packages for running the scripts contained in this repository (latest available versions: 20-03-2021):
* glob
* logging
* os
* pickle
* shutil
* typing
* pandas
* numpy
* tqdm
* pathlib 
* transformers 
* torch
* tensorboardX 

# References
The code used for training was inspired by this [colab](https://colab.research.google.com/drive/15wa925dj7jvdvrz8_z3vU7btqAFQLVlG#scrollTo=78afhsngLZMw).

