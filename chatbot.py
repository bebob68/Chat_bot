from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('/home/binesh/Documents/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english'):
    data = open('/home/binesh/Documents/chatterbot/chatterbot-corpus-master/chatterbot_corpus/data/english'+files,'r').readlines()
    bot.train(data)

while True:
        message = input('You:')
        if message.strip() !='Bye':
             reply = bot.get_response(message)
             print('ChatBot:',reply)
        if message.strip() == 'Bye':
               print('ChatBot: Bye')
               break
