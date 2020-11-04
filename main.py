'''
John Mazziotti
September 17th, 2020
This is the "Post Oak Distance Learning Hub" Application
Inside you will find various links to websites and Zoom meetings.
The overall goal of this application is to simplify a student's distance learning experience.
'''

from tkinter import *
import webbrowser
master = Tk()

#Main Structure
master.title("Post Oak Distance Learning Hub")
master.geometry("600x400") #dimensions
master.configure(background='gray20')

class LogIn:
    def __init__(self,firstName,lastName):
        Button(master, text='Log In',command=self.logIn(firstName,lastName),bg='gray40',fg='white',highlightbackground='gray30').place(x=10,y=80)
        Label(master, text='First Name',bg='gray40',fg='white',highlightbackground='gray30').place(x=5,y=10)
        self.e = Entry(master).place(x=85,y=9,width=150)
        Label(master, text='Last Name',bg='gray40',fg='white',highlightbackground='gray30').place(x=5,y=43)
        self.e = Entry(master).place(x=85,y=40,width=150)
    def logIn(self,firstName,lastName):
        print(firstName,lastName)
LogIn.logIn(master,"John","Maz")


class mainMenu:
    master.title("Post Oak Distance Learning Hub")
    master.geometry("600x400")  # dimensions
    master.configure(background='gray20')
    Button(master, text='Open Common Websites', command='na', bg="gray20", fg="black", highlightbackground="green",activebackground="deep sky blue").place(x=32, y=100, height=100, width=150)
    Button(master, text='Open Class Meetings', command='classMeet', bg="gray20", fg="black", highlightbackground="yellow",activebackground="deep sky blue").place(x=222, y=100, height=100, width=150)
    Button(master, text='Open Personal Meetings', command='na', bg="gray20", fg="black", highlightbackground="blue",activebackground="deep sky blue").place(x=415, y=100, height=100, width=150)

class comWeb:
    small = Toplevel(master)
    small.title("Common Websites")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(master, text="Common Websites", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=90, y=0, height=40, width=440)
    def __init__(self):
        print("Going to Common Websites")
    def buildSmall(self):
        #this function build the smaller windows which open and display one of the three choosable meetings.
        small = Toplevel(master)
        small.title("Common Websites")
        small.geometry('500x300')
        small.configure(background='gray20')
        Label(master, text="Common Websites", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=90, y=0, height=40, width=440)
    def browse_web(self):
        new = 1
        url = "https://www.google.com"
        webbrowser.open(url,new=new)
        print("Going to Google...")
    def postoak_school(self):
        new = 1
        url = "https://postoakschool.learning.powerschool.com/"
        webbrowser.open(url,new=new)
        print("Taking you to Powerschool...")
    #buttons for com web
    Button(small, text='Open Google', command=browse_web, bg="gray20", fg="black", highlightbackground="green").place(x=10, y=75, height=30, width=80)
    Button(small, text='Haiku Learning', command=postoak_school, bg="gray20", fg="black", highlightbackground="orange").place(x=10, y=110, height=30, width=110)

class classMeet:
    master.title("Post Oak Distance Learning Hub: Class Meetings")
    master.geometry("600x400")  # dimensions
    def comp_sci_(self):
      new = 1
      url = "https://postoakschool.zoom.us/j/7521788524?pwd=QmtnNUYxRy8zcFlBSndkeEErRjUzdz09"
      webbrowser.open(url,new=new)
      print("Taking you to Computer Science...")

#buttons,
# (MAKE SURE YOU ADD ",,,.place(x=45,y=345,height= 40, width=40)"

#Labels for App
Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=90,y=0,height= 40, width=440)

master.mainloop()
