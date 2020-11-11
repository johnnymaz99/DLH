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

def LogIn():
    Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="lightgreen", fg="White",font=('Times New Roman', '20')).place(x=102, y=0, height=40, width=398)
    Button(master, text='Log In', command=LogIn, bg='gray40', fg='black', highlightbackground='gray30').place(x=5, y=350, height=35, width=70) #login button
    Label(master, text='First Name', bg='gray40', fg='white', highlightbackground='gray30').place(x=5, y=275) #next 4 lines are labels and entry boxes for first and last name.
    Entry(master).place(x=85, y=273, width=150)
    Label(master, text='Last Name', bg='gray40', fg='white', highlightbackground='gray30').place(x=5, y=320)
    Entry(master).place(x=85, y=318, width=150)
    Label(master, text='Login Status', bg='red', fg='white', highlightbackground='red').place(x=250, y=297)#changes from red to green which checks to make sure user has logged in
LogIn()


def mainMenu():

    Button(master, text='Open Common Websites', command=comWeb, bg="green", fg="black", highlightbackground="green").place(x=32, y=100, height=100, width=150)
    Button(master, text='Open Class Meetings', command=classMeet, bg="gray20", fg="black", highlightbackground="yellow").place(x=222, y=100, height=100, width=150)
    Button(master, text='Open Personal Meetings', command=personMeet, bg="gray20", fg="black", highlightbackground="blue").place(x=415, y=100, height=100, width=150)


def comWeb():
    small = Toplevel(master)
    small.title("Common Websites")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(small, text="Common Websites", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=174, y=0, height=40, width=440)
    #left buttons for com web
    Button(small, text='Google', command=browse_web, bg="gray40", fg="black", highlightbackground="green").place(x=12, y=75, height=30, width=110)
    Button(small, text='Power School', command=postoak_school, bg="gray40", fg="black", highlightbackground="orange").place(x=12, y=135, height=30, width=110)
    Button(small, text='Padlet', command=pad_let, bg="gray40", fg="black", highlightbackground="gray").place(x=12, y=190, height=30, width=110)
    #middle Buttons
    Button(small, text='Google Drive', command=googDrive, bg="gray40", fg="black", highlightbackground="yellow").place(x=193, y=75, height=30, width=110)
    Button(small, text='Google Calendar', command=googCal, bg="gray40", fg="black", highlightbackground="blue").place(x=193, y=135, height=30, width=110)
    Button(small, text='Gmail', command=googMail, bg="gray40", fg="white", highlightbackground="red").place(x=193, y=190, height=30, width=110)
    #right buttons
    Button(small, text='Flip Grid', command=flipGrid, bg="gray40", fg="white", highlightbackground="purple").place(x=375, y=75, height=30, width=110)
    Button(small, text='Loom', command=theLoom, bg="gray40", fg="black", highlightbackground="pink").place(x=375, y=135, height=30, width=110)
    Button(small, text='Blogger', command=blogGer, bg="gray40", fg="white", highlightbackground="orange").place(x=375, y=190, height=30, width=110)
#class meeting page
def classMeet():
    small = Toplevel(master)
    small.title("Class Meetings")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(small, text="Class Meetings", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=190, y=0, height=40, width=440)
#Personal Meeting page
def personMeet():
    small = Toplevel(master)
    small.title("Personal Meetings")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(small, text="Personal Meeting Rooms", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=155, y=0, height=40, width=440)
mainMenu()
#Below are the functions which go to commonly used websites websites
def browse_web():
    new = 1
    url = "https://www.google.com"
    webbrowser.open(url,new=new)
    print("Going to Google...")
def postoak_school():
    new = 1
    url = "https://postoakschool.learning.powerschool.com/"
    webbrowser.open(url,new=new)
    print("Taking you to Powerschool...")
def pad_let():
    new = 1
    url = "https://postoakschool.padlet.org/dashboard"
    webbrowser.open(url,new=new)
    print("Taking you to Padlet...")
def googDrive():
    new = 1
    url = "https://drive.google.com"
    webbrowser.open(url,new=new)
    print("Taking you to Google Drive...")
def googCal():
    new = 1
    url = "https://calendar.google.com"
    webbrowser.open(url,new=new)
    print("Taking you to Google Calendar...")
def googMail():
    new = 1
    url = "https://mail.google.com"
    webbrowser.open(url,new=new)
    print("Taking you to Google Mail...")
def flipGrid():
    new = 1
    url = "https://info.flipgrid.com"
    webbrowser.open(url,new=new)
    print("Taking you to Flip Grid...")
def theLoom():
    new = 1
    url = "https://www.loom.com"
    webbrowser.open(url, new=new)
    print("Taking you to Loom...")
def blogGer():
    new = 1
    url = "https://www.blogger.com/"
    webbrowser.open(url, new=new)
    print("Taking you to Blogger...")


#this function build the smaller windows which open and display one of the three choosable meetings.
def buildSmall():
    small = Toplevel(master)
    small.title("Common Websites")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(master, text="Common Websites", anchor="w", bg="gray20", fg="White",
      font=('Times New Roman', '20')).place(x=90, y=0, height=40, width=440)

def comp_sci_():
  new = 1
  url = "https://postoakschool.zoom.us/j/7521788524?pwd=QmtnNUYxRy8zcFlBSndkeEErRjUzdz09"
  webbrowser.open(url,new=new)
  print("Taking you to Computer Science...")

#buttons,
# (MAKE SURE YOU ADD ",,,.place(x=45,y=345,height= 40, width=40)"

#Labels for App
#Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=90,y=0,height= 40, width=440)

master.mainloop()
