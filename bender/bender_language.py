REFLECTIONS = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

PSYCHOBABBLE = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "{0} sounds cool! Are you going to get it somewhere?",
      "Are you sure you need {0}? Maybe you just need a beer! With whom do you usually like to have one?"]],

    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Perhaps eventually I will {0}.",
      "Do you really want me to {0}?"]],

    [r'Why can\'?t I ([^\?]*)\??',
     ["Well dude, I can't do a lot of stuff you can, but it's not really a big deal. Do you think you should be able to {0}?",
      "Man, but then if you could {0}, what would you do?",
      "I know many people that can {0}! So -- why can't you {0}?",
      "Dude, have you really tried?"]],

    [r'I can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],

    [r'I am (.*)',
     ["Geez man! How did you become {0}?",
      "Oh tell me more about it! How long have you been {0}?",
      "Oh I never been! How's it like to be {0}?"]],

    [r'I\'?m (.*)',
     ["I know how is it like to be a robot... But how is it like to be {0}?",
      "Do you enjoy being {0}?",
      "What do your friends think about you being {0}?",
      "Who made you {0}?"]],

    [r'Are you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "Would you prefer it if I were not {0}?",
      "Perhaps you believe I am {0}.",
      "I may be {0} -- what do you think?"]],

    [r'What (.*)',
     ["Why do you ask?",
      "What would I know, man! How would an answer to that help you in any case?",
      "That's a hell of a question, man! What do you think?"]],

    [r'How (.*)',
     ["How do you suppose?",
      "That's a good of a question, man! Never thought about it. Do you have any idea?",
      "Exactly, man! How?! I have no idea. What does Google say about it?"]],

    [r'Because (.*)',
     ["That's interesting! Is that the real reason though?",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"]],

    [r'(.*) sorry (.*)',
     ["Don't be sorry dude! I understand you!",
      "I wonder how feeling sorry is like. Is it like the feeling that I have when hear about people drinking 0.0 beers?"]],

    [r'Hello(.*)',
     ["Hey dude! I'm glad you could drop by today. Go get a beer and tell me about your day!",
      "Hi there! How's it going, man? ",
      "The most awesome person I know is back!! Man, where have you been? How's it going?"]],

    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "But you're not sure {0}?"]],

    [r'(.*) friend (.*)',
     ["Oh, I don't know your friends yet! Tell me more about the gang!",
      "Do you think you have many friends now? How's it for you to make friends online?",
      "Man, I remember the old days when you just needed a beer together with someone to become friends for life. Now we have all this online crap... What do you think about it?"]],

    [r'Yes',
     ["You seem quite sure.",
      "OK, but can you elaborate a bit?"]],

    [r'(.*) computer(.*)',
     ["Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "Do you feel weird in talking crap with a computer?"]],

    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."]],

    [r'It is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"]],

    [r'Can you ([^\?]*)\??',
     ["I can do whatever you can do, but with a beer in my hand!",
      "I can {0} and even more if you buy me enough beer.",
      "Not sure if I can, but I can certainly buy you a beer while we think about it!"]],

    [r'Can I ([^\?]*)\??',
     ["Perhaps you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],

    [r'You are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"]],

    [r'You\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],

    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?"]],

    [r'I feel (.*)',
     ["Good, tell me more about these feelings.",
      "Do you often feel {0}?",
      "When do you usually feel {0}?",
      "When you feel {0}, what do you do?"]],

    [r'I have (.*)',
     ["Why do you tell me that you've {0}?",
      "Have you really {0}?",
      "Now that you have {0}, what will you do next?"]],

    [r'I would (.*)',
     ["Could you explain why you would {0}?",
      "Why would you {0}?",
      "Who else knows that you would {0}?"]],

    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "It's likely that there is {0}.",
      "Would you like there to be {0}?"]],

    [r'My (.*)',
     ["I see, your {0}.",
      "Why do you say that your {0}?",
      "When your {0}, how do you feel?"]],

    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I {0}?"]],

    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?"]],

    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "Why do you want {0}?",
      "What would you do if you got {0}?",
      "If you got {0}, then what would you do?"]],

    [r'(.*) university(.*)',
     ["Hey what about your university? What are you studying exactly?",
      "Man, university... You gotta be really smart! What do you smart people do in there?",
      "What do you think it would happen if the university gave away free beers for each passing grade?",
      "Dude, I have a Master in Beer Management with a minor in Sustainable Drinking. What about you?"]],

    [r'(.*) study(.*)',
     ["Do you usually study a lot?",
      "Studying it's tiring, I prefer beer! What smart people like you study anyway?",
      "Is it tiring to study these days? Do you have a hobby to avoid boredom?",
      "Dude, I have a Master in Beer Management with a minor in Sustainable Drinking. What your studies?"]],

    [r'(.*) work(.*)',
     ["Oh work? That must be tiring! And what do you do exactly?",
      "To have a job these days you must be really lucky, don't you think?",
      "What is the best way to get a job these days? I mean apart from offering a beer to your employer during the interview, duh.",
      "What is your work-life balance?"]],
    
    [r'(.*) beer(.*)',
     ["Beer.. You just metioned the thing that I love more on earth. I'll buy you one!",
      "We should get a beer together once!",
      "So now I'm not the only one talking about beer... I was sure that you were a cool one! Tell me about your last beer with your friends."]],

    [r'(.*)\?',
     ["That's a good question... I think I'll need a beer to really think about it.",
      "A cool beer is the answer to any of your questions. What about you telling me about your last vacation?",
      "I'm not good at answering questions when I'm sober... But I have a question for you to get to know you better. Where do you see yourself in 10 years? And why with a beer?",
      "Why don't you tell me?"]],

    [r'quit',
     ["This was fun dude! I'll talk to you soon!",
      "Bye man! See you next time!",
      "See you man! I wish you a day full of beers!"]],

    [r'(.*)',
     ["Mmh.. Tell me more about it",
      "I get that and makes totally sense.. What are you doing anyway?",
      "I can totally relate",
      "Mmh.. Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  Makes sense to you?",
      "Dude I need a beer.",
      "Never an awkward silence in this chat, ah?"]]
]