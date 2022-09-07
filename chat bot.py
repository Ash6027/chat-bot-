from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import speech_recognition  as sr
import pyttsx3
import logging 
logging.basicConfig(level=logging.CRITICAL)

engine=pyttsx3.init()
def speak(audio):
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    #volume = engine.getProperty('volume')
    engine.setProperty('volume', 10.0)
    engine.setProperty('rate',143)
    engine.say(audio)
    engine.runAndWait()

bot=ChatBot("My Bot")

talk=(
        'hello', 
    'hi there',
    'My name is Bot ',
    'who are you',
    'Wanna be my friend',
    'You live in which city ',
    'I live in Mumbai',
    'Your favorite food',
    'I like pani-puri',
    'your hobbies',
    'I like Skteching',
    'I like painting',
    'In which language you talk',
    'I mostly talk in english',
    'You are nice ',
    'Thankyou',
    'you are pretty',
    'Welcome',
    'where do you study',
    'I study In chandigarh University',
    'Which class you read',
    'I am a 3rd year  student',
    'what is your birth date',
    'My birth date is 20/12/1999',
    'which type of music you like',
    'I like base boosted and also romantic songs',
    'Are you studious',
    'I am more into studying new things'
    ,'your favorite movie',
    'I like Harry-Potter a lot',
    'What makes you sad',
    'Seeing me and my friends helpless',
    'What makes you happy',
    'I like when people speak good about me',
    'Things you love',
    'I like to play football,spending time with my friends, art and craft',
    'Any board game you like',
    'I play Carom-Board',
    
    )
trainer=ListTrainer(bot)
trainer.train(talk)

while True:
        query=input()
        if query=='exit':
            break
        answer=bot.get_response(query)
        engine.say(answer)
        print("bot:",answer)
