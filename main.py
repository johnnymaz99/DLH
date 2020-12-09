'''
John Mazziotti
September 17th, 2020
This is the "Post Oak Distance Learning Hub" Application
Inside you will find various links to websites and Zoom meetings.
The overall goal of this application is to simplify a student's distance learning experience.
'''

from tkinter import *
from tkmacosx import Button
import webbrowser
master = Tk()

#Main Structure
master.title("Post Oak Distance Learning Hub")
master.geometry("600x400") #dimensions
master.configure(background='gray20')

def LogIn():
    Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="lightgreen", fg="White",font=('Times New Roman', '20')).place(x=102, y=0, height=40, width=398)
LogIn()

def mainMenu():

    Button(master, text='Open Common Websites', command=comWeb, bg="green", fg="black", highlightbackground="green", font=('Times New Roman', '15')).place(x=32, y=100, height=100, width=160)
    Button(master, text='Open Class Meetings', command=classMeet, bg="yellow", fg="black", highlightbackground="yellow", font=('Times New Roman', '15')).place(x=222, y=100, height=100, width=150)
    Button(master, text='Open Personal Meetings', command=personMeet, bg="blue", fg="black", highlightbackground="blue",font=('Times New Roman', '15')).place(x=400, y=100, height=100, width=160)
    Button(master, text='Open Custom Presets', command=customPreset, bg="red", fg="white", highlightbackground="red", font=('Times New Roman', '25')).place(x=32, y=210, height=100, width=528)


def comWeb():
    small = Toplevel(master)
    small.title("Common Websites")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(small, text="Common Websites", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=174, y=0, height=40, width=440)
    #left buttons for com web
    Button(small, text='Google', command=browse_web, bg="green", fg="white", highlightbackground="green").place(x=12, y=75, height=30, width=110)
    Button(small, text='Power School', command=postoak_school, bg="orange", fg="white", highlightbackground="orange").place(x=12, y=135, height=30, width=110)
    Button(small, text='Padlet', command=pad_let, bg="gray", fg="white", highlightbackground="gray").place(x=12, y=190, height=30, width=110)
    #middle Buttons
    Button(small, text='Google Drive', command=googDrive, bg="yellow", fg="black", highlightbackground="yellow").place(x=193, y=75, height=30, width=110)
    Button(small, text='Google Calendar', command=googCal, bg="blue", fg="white", highlightbackground="blue").place(x=193, y=135, height=30, width=110)
    Button(small, text='Gmail', command=googMail, bg="red", fg="white", highlightbackground="red").place(x=193, y=190, height=30, width=110)
    #right buttons
    Button(small, text='Flip Grid', command=flipGrid, bg="purple", fg="white", highlightbackground="purple").place(x=360, y=74, height=30, width=110)
    Button(small, text='Loom', command=theLoom, bg="pink", fg="black", highlightbackground="pink").place(x=360, y=135, height=30, width=110)
    Button(small, text='Blogger', command=blogGer, bg="orange", fg="white", highlightbackground="orange").place(x=360, y=190, height=30, width=110)
    #master search button
    Button(small, text='Master Search', command=masterSearch, bg="red", fg="white", highlightbackground="red").place(x=300, y=250,height=30,width=150)
    Button(small, text='Save Presets', command=savePresets, bg="white", fg="black", highlightbackground="white").place(x=45, y=250, height=30, width=150)

    '''
    file = open('pref.ini')
    counter = 0

    for line in file:
        line = line.strip('\n')
        #print(line)
        counter += 1
        lineValue = 'box' + str(counter) + 's = 0'
        if lineValue == line:
            print(line)
            box1.deselect()
            '''
#Below are all the check boxes that allow the user to use the 'master search' function, which is what these boxes coincide with.
    global box1s,box1
    box1s = StringVar()
    box1 = Checkbutton(small,text='',variable=box1s,bg="gray20",fg="white")
    box1.deselect()
    box1.place(x=130,y=80)

    global box2s,box2
    box2s = StringVar()
    box2 = Checkbutton(small, text='', variable=box2s, bg="gray20", fg="black")
    box2.deselect()
    box2.place(x=130, y=140)

    global box3s,box3
    box3s = StringVar()
    box3 = Checkbutton(small, text='', variable=box3s, bg="gray20", fg="black")
    box3.deselect()
    box3.place(x=130, y=195)

    global box4s,box4
    box4s = StringVar()
    box4 = Checkbutton(small, text='', variable=box4s, bg="gray20", fg="white")
    box4.deselect()
    box4.place(x=310, y=80)

    global box5s,box5
    box5s = StringVar()
    box5 = Checkbutton(small, text='', variable=box5s, bg="gray20", fg="black")
    box5.deselect()
    box5.place(x=310, y=140)

    global box6s,box6
    box6s = StringVar()
    box6 = Checkbutton(small, text='', variable=box6s, bg="gray20", fg="black")
    box6.deselect()
    box6.place(x=310, y=195)

    global box7s,box7
    box7s = StringVar()
    box7 = Checkbutton(small, text='', variable=box7s, bg="gray20", fg="white")
    box7.deselect()
    box7.place(x=475, y=79)

    global box8s,box8
    box8s = StringVar()
    box8 = Checkbutton(small, text='', variable=box8s, bg="gray20", fg="black")
    box8.deselect()
    box8.place(x=475, y=139)

    global box9s,box9
    box9s = StringVar()
    box9 = Checkbutton(small, text='', variable=box9s, bg="gray20", fg="black")
    box9.deselect()
    box9.place(x=475, y=195)

    readINI()

#This function is devoted to allowing the user to select multiple links at the same time to open them simotaniously
def masterSearch():
    print('masterSearch')
    if (box1s.get()=='1'):
        browse_web()

    if (box2s.get()=='1'):
        postoak_school()

    if (box3s.get()=='1'):
        pad_let()

    if (box4s.get()=='1'):
        googDrive()

    if (box5s.get()=='1'):
        googCal()

    if (box6s.get()=='1'):
        googMail()

    if (box7s.get()=='1'):
        flipGrid()

    if (box8s.get()=='1'):
        theLoom()

    if (box9s.get()=='1'):
        blogGer()

def savePresets():
    print('savePresets')
    var1=box1s.get()
    print(var1)
    print(type(var1))
    lineValue = 'box' + str(var1) + 's = 1'
    with open('pref.ini', 'r') as file:
       data = file.readlines()
    data[0]=lineValue + '\n'
    with open('pref.ini', 'w') as file:
        file.writelines(data)
def readINI():
    file=open('pref.ini')
    for line in file:
        line = line.strip('\n')
        #lineValue='box'+str(counter)+'s = 1'
        if 'box1s = 1' == line:
            box1.select()
        if 'box2s = 1' == line:
            box2.select()
        if 'box3s = 1' == line:
            box3.select()
        if 'box4s = 1' == line:
            box4.select()
        if 'box5s = 1' == line:
            box5.select()
        if 'box6s = 1' == line:
            box6.select()
        if 'box7s = 1' == line:
            box7.select()
        if 'box8s = 1' == line:
            box8.select()
        if 'box9s = 1' == line:
            box9.select()

#class meeting page
def classMeet(): #This is the class meeting window, it will take you to classes.
    small = Toplevel(master)
    small.title("Class Meetings")
    small.geometry('700x400')
    small.configure(background='gray20')
    Label(small, text="Class Meetings", anchor="w", bg="gray20", fg="White",font=('Times New Roman', '20')).place(x=290, y=0, height=40, width=440)
    Label(small, text="9/10", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=120, y=25, height=40, width=440)
    Label(small, text="11/12", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=520, y=25, height=40,width=440)
    Button(small, text='Computer Science', command=comp_sci_, bg="blue", fg="white", highlightbackground="blue").place(x=560, y=60, height=32, width=135)
    Button(small, text='Theory of Knowledge', command=knowTheory, bg="pink", fg="white", highlightbackground="pink").place(x=400, y=60, height=32, width=135)
    Button(small, text='Math SL', command=mathSL, bg="orange", fg="white", highlightbackground="orange").place(x=560, y=100, height=32, width=135)
    Button(small, text='Math Applications', command=mathStudies, bg="orange", fg="white", highlightbackground="orange").place(x=400, y=100,height=32,width=135)
    Button(small, text='Visual Art 11', command=artEleven, bg="yellow", fg="black", highlightbackground="yellow").place(x=560, y=140,height=32,width=135)
    Button(small, text='Visual Art 12', command=artTwelve, bg="yellow", fg="black", highlightbackground="yellow").place(x=400, y=140,height=32,width=135)
    Button(small, text='Theatre', command=thEAtre, bg="white", fg="black", highlightbackground="white").place(x=560, y=180,height=32,width=135)
    Button(small, text='Film', command=filmClass, bg="white", fg="black", highlightbackground="white").place(x=400, y=180,height=32,width=135)
    Button(small, text='Chinese', command=chineseClass, bg="red", fg="white", highlightbackground="red").place(x=560, y=220,height=32,width=135)
    Button(small, text='Spanish', command=spanishClass, bg="red", fg="white", highlightbackground="red").place(x=400, y=220,height=32,width=135)
    Button(small, text='Global Politics', command=gpHC, bg="blue", fg="white", highlightbackground="blue").place(x=560, y=260,height=32,width=135)
    Button(small, text='Economics', command=ecON, bg="blue", fg="white", highlightbackground="blue").place(x=400, y=260,height=32,width=135)
    Button(small, text='Chemistry', command=chemISTRY, bg="purple", fg="white", highlightbackground="purple").place(x=400, y=300,height=32,width=135)
    Button(small, text='Biology', command=bioLOGY, bg="purple", fg="white", highlightbackground="purple").place(x=560, y=300,height=32,width=135)

#Personal Meeting page
def personMeet():
    small = Toplevel(master) #This is the personal meeting window.
    small.title("Personal Meetings")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(small, text="Personal Meeting Rooms", anchor="w", bg="gray20", fg="White",
          font=('Times New Roman', '20')).place(x=155, y=0, height=40, width=440)
#This function is user-specific, it allows the user to choose their own presets for links and meetings to make the use of this app more streamline.
def customPreset():
    small = Toplevel(master)
    small.title("Custom Saved Presets")
    small.geometry('500x300')
    small.configure(background='gray30')
    Label(small, text="User's Custom Presets", anchor="w", bg="gray30", fg="White",
          font=('Times New Roman', '20')).place(x=160, y=0, height=40, width=300)
    Button(small, text='Search', command=customLink, bg='green', fg='white', highlightbackground='green').place(x=380,y=246, height=35,width=70)  # login button
    Label(small, text='Custom URL', bg='gray40', fg='white', highlightbackground='gray30').place(x=5,y=252, )
    Entry(small).place(x=100, y=250, width=275)
def customLink():
    new = 1
    url= " "
    webbrowser.open(url, new=new)
# next 4 lines are labels and entry boxes for first and last name
mainMenu()
#Below are the functions which are displayed in the "Common Websites" window, these take you to commonly used websites
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

#Below are the class meeting functions, these will appear in the "Class Meetings" window
def comp_sci_():
  new = 1
  url = "https://postoakschool.zoom.us/j/7521788524?pwd=QmtnNUYxRy8zcFlBSndkeEErRjUzdz09"
  webbrowser.open(url,new=new)
  print("Taking you to Computer Science...")
def knowTheory():
  new = 1
  url = "https://postoakschool.zoom.us/j/2625303187?pwd=R2tMSjJKc0dIUVJRQitHWkV0Y1JKdz09"
  webbrowser.open(url,new=new)
  print("Taking you to TOK...")
def mathSL():
  new = 1
  url = "https://postoakschool.zoom.us/j/2565996744?pwd=Z3dhVmhqVWprTjZCTVdpM1h6T0JyUT09"
  webbrowser.open(url,new=new)
  print("Taking you to Standard Level Math...")
def mathStudies():
  new = 1
  url = "https://postoakschool.zoom.us/j/6533994640?pwd=LzMrMVN6RlRESlhrZG5EYlNXRjN4UT09"
  webbrowser.open(url,new=new)
  print("Taking you to Math Applications...")
def artEleven():
  new = 1
  url = "https://postoakschool.zoom.us/j/3233251845"
  webbrowser.open(url,new=new)
  print("Taking you to Art Grade 11...")
def artTwelve():
  new = 1
  url = "https://postoakschool.zoom.us/j/7519659352?pwd=L05pZWViQ29mZEhndnZoQnNuajZWdz09"
  webbrowser.open(url,new=new)
  print("Taking you to Art Grade 12...")
def thEAtre():
  new = 1
  url = "https://postoakschool.zoom.us/j/5200316552"
  webbrowser.open(url,new=new)
  print("Taking you to Theatre...")
def filmClass():
    new = 1
    url = "https://postoakschool.zoom.us/j/6471240173?pwd=UDdGbXhTY1FnRXAyWGdBS0dpUEhxUT09"
    webbrowser.open(url, new=new)
    print("Taking you to Film...")
def spanishClass():
    new = 1
    url = "https://postoakschool.zoom.us/j/2112829629?pwd=MXBMUzd6cHRmK2tpRmJnTkVhZ3lXZz09"
    webbrowser.open(url, new=new)
    print("Taking you to Spanish...")
def chineseClass():
    new = 1
    url = "https://postoakschool.zoom.us/j/3332685495?pwd=ejlCVkFpV1c1SnpuMkJnTThpblN0UT09"
    webbrowser.open(url, new=new)
    print("Taking you to Chinese...")
def gpHC():
    new = 1
    url = "https://postoakschool.zoom.us/j/7926370075?pwd=eUV5SjVjUDNTdnhFV0czK2UxeDcwdz09"
    webbrowser.open(url, new=new)
    print("Taking you to Global Politics...")
def ecON():
    new = 1
    url = "https://postoakschool.zoom.us/j/8496755996?pwd=b0h4d3RxNThESlJBS3kxdlpxZmpiZz09"
    webbrowser.open(url, new=new)
    print("Taking you to Economics...")
def chemISTRY():
    new = 1
    url = "https://postoakschool.zoom.us/j/9816073304?pwd=ZjYxZmVTTElkaHR2V3dFRzBFL21kZz09"
    webbrowser.open(url, new=new)
    print("Taking you to Chemistry...")
def bioLOGY():
    new = 1
    url = "https://postoakschool.zoom.us/j/9718918223?pwd=NXJtWXE2MEsrQWs3MzhwbXFocnZEUT09"
    webbrowser.open(url, new=new)
    print("Taking you to Biology...")


#this function build the smaller windows which open and display one of the three choosable tabs.
def buildSmall():
    small = Toplevel(master)
    small.title("Common Websites")
    small.geometry('500x300')
    small.configure(background='gray20')
    Label(master, text="Common Websites", anchor="w", bg="gray20", fg="White",
      font=('Times New Roman', '20')).place(x=90, y=0, height=40, width=440)



#buttons,
# (MAKE SURE YOU ADD ",,,.place(x=45,y=345,height= 40, width=40)"

#Labels for App
#Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=90,y=0,height= 40, width=440)

master.mainloop()
