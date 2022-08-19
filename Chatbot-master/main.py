
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading
engine= pp.init()

voices= engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot=ChatBot("MY BOT")

convo = [
         'Hello',
         'hi there',
         'How are you?',
         'I am good !',

         'Tell me about R E C Banda ',
         'Rajkiya Engineering College, Banda was established by the Government of Uttar Pradesh in the year 2010 with three branches, Electrical Engineering, Mechanical Engineering, and Information Technology with annual intake of Sixty in each branch',

    'Address of REC Banda?',
    'It is located in a small town Atarra in district Banda , Uttar Pradesh.',

    'Pin code of atarra?',
    'PIN code of atarra is 210201',

    'what is old name of college?',
    'Dr. Bhim Rao Ambedkar Engineering College of Information Technology',

    'Branches offered by the college?',
    'three branches, Electrical Engineering, Mechanical Engineering, and Information Technology',

    'Who is director of College?',
    'Director of Rajkiya Engineering College Banda Prof. Sheo Prasad Shukla',

    'Faculty members of IT department ?',
    'faculty members of IT department are Dr. Vibhash Yadav , Dr. Siddharth Arjaria , Mr. Shantanu Shukla , Miss Manjari Ganghwar , Miss Sonali Pandey , Mr. Arindam',

]

trainer = ListTrainer(bot)

# now training the bot

trainer.train(convo)

#answer = bot.get_response("Hello")
#print(answer)
#print("Talk to bot")
#while True:
#    query = input()
#    if query=='exit':
#        break
#   answer=bot.get_response(query)
#   print("bot :",answer)

main = Tk()
main.geometry("450x600")                    #setting dimension of windows
main.title("My Chatbot")                    #adding title
img= PhotoImage(file="bot1.png")            #creating image object
photoL=Label(main,image=img)                #setting img
photoL.pack(pady=5)                         #padding y axis
# takes audio input from user and convert it to string
def take_query():
    sr=s.Recognizer()                          #making object of recognizer
    sr.pause_threshold=1                       #setting pause threshold
    print("Your bot is listening try to speak!")
    with s.Microphone() as m:
        audio = sr.listen(m)
        query=sr.recognize_google(audio, language = 'en-IN', show_all = True )
        print(query)
        textF.delete(0,END)
        textF.insert(0,query)
        ask_bot()

#funtion ask_bot

def ask_bot():
    query= textF.get()                                      #get text from text field
    ans_from_bot = bot.get_response(query)
    msg.insert(END,"YOU :" + query)                         #flashes user query
    msg.insert(END,"BOT :" + str(ans_from_bot))             #flashes bots ans
    speak(ans_from_bot)                                     #speaks the answer
    textF.delete(0,END)                                     #clear screen at every run
    msg.yview(END)                                          #to keep scrollbar at end mssgs

#adding frame to the window

frame=Frame(main)
sc=Scrollbar(frame)                                              #creating scrollbar
msg= Listbox(frame,width=60,height=20,yscrollcommand=sc.set)     #creating listbox
sc.pack(side=RIGHT,fill=Y)
msg.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating textfield
textF=Entry(main,font=("Verdana",20))
textF.pack(fill=X,pady=10)
#creating button
btn=Button(main,text="Ask",font=("Verdana",20),command=ask_bot)
btn.pack()

#creating function for enter button
def enter_func(event):
    btn.invoke()


#binding main window with enter key
main.bind('<Return>',enter_func)

t = threading.Thread(target=take_query)   # creating thread for speech rec. so it will not interupt GUI
t.start()
main.mainloop()