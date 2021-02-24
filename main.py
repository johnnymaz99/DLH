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
Entry1_var = StringVar()
Entry2_var = StringVar()
Entry3_var = StringVar()
Entry4_var = StringVar()
Entry5_var = StringVar()
Entry6_var = StringVar()
Entry7_var = StringVar()
Entry8_var = StringVar()
Entry9_var = StringVar()
#go to 9
def LogIn():
    Label(master, text="Welcome to the Post Oak Distance Learning Hub", anchor="w", bg="lightgreen", fg="White",font=('Times New Roman', '20')).place(x=102, y=0, height=40, width=398)
LogIn()

def mainMenu():

    Button(master, text='Open Common Websites', command=comWeb, bg="green", fg="white", highlightbackground="green", font=('Times New Roman', '15')).place(x=32, y=100, height=100, width=160)
    Button(master, text='Open Class Meetings', command=classMeet, bg="yellow", fg="black", highlightbackground="yellow", font=('Times New Roman', '15')).place(x=222, y=100, height=100, width=150)
    Button(master, text='Open Personal Meetings', command=personMeet, bg="blue", fg="white", highlightbackground="blue",font=('Times New Roman', '15')).place(x=400, y=100, height=100, width=160)
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
    var1 = box1s.get()
    var2 = box2s.get()
    var3 = box3s.get()
    var4 = box4s.get()
    var5 = box5s.get()
    var6 = box6s.get()
    var7 = box7s.get()
    var8 = box8s.get()
    var9 = box9s.get()
    varArray = [var1,var2,var3,var4,var5,var6,var7,var8,var9]
    with open('pref.ini','r') as file:
        data = file.readlines()
        print(data)
    counter = 1
    with open('pref.ini', 'w') as file:
        for i in varArray:
            if counter <=8:

                #counter += 1
                lineValue = 'box' + str(counter) + 's = '+i+'\n'
                print(lineValue)
                file.writelines(lineValue)
                counter += 1
        file.writelines(data[8])
        file.writelines(data[9])
        file.writelines(data[10])
        file.writelines(data[11])
        file.writelines(data[12])
        file.writelines(data[13])
        file.writelines(data[14])
        file.writelines(data[15])
        file.writelines(data[16])
        file.writelines(data[17])
        #file.writelines(data[18])
        #file.writelines(data[19])
        #go to 18

#

def readINI():
    file=open('pref.ini')
    for line in file:
        line = line.strip('\n')
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
#class meeting page(ADD 9/10 PAGE)
def classMeet(): #This is the class meeting window, it will take you to classes.
    small = Toplevel(master)
    small.title("Class Meetings")
    small.geometry('700x400')
    small.configure(background='gray20')
    Label(small, text="Class Meetings", anchor="w", bg="gray20", fg="White",font=('Times New Roman', '20')).place(x=290, y=0, height=30, width=440)
    #9/10 Classes
    Label(small, text="9/10", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=110, y=25, height=35, width=440)

    Button(small, text='ELA', command=knowTheory, bg="pink", fg="white",highlightbackground="pink").place(x=5, y=70, height=32, width=100)
    Button(small, text='Math', command=mathSL, bg="orange", fg="white", highlightbackground="orange").place(x=150,y=70,height=32,width=100)
    Button(small, text='Visual Art', command=artTwelve, bg="yellow", fg="black", highlightbackground="yellow").place(x=5, y=145, height=32, width=100)
    Button(small, text='Theatre', command=thEAtre, bg="white", fg="black", highlightbackground="white").place(x=150,y=145,height=32,width=100)
    Button(small, text='Chinese', command=chineseClass, bg="red", fg="white", highlightbackground="red").place(x=5,y=220,height=32,width=100)
    Button(small, text='Spanish', command=spanishClass, bg="red", fg="white", highlightbackground="red").place(x=150,y=220,height=32,width=100)
    Button(small, text='IHSS', command=gpHC, bg="blue", fg="white", highlightbackground="blue").place(x=5,y=295,height=32,width=100)
    Button(small, text='Science', command=bioLOGY, bg="purple", fg="white", highlightbackground="purple").place(x=150,y=295,height=32,width=100)
    #11/12 Classes
    Label(small, text="11/12", anchor="w", bg="gray20", fg="White", font=('Times New Roman', '20')).place(x=520, y=25, height=35,width=440)

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
    small.geometry('500x650')
    small.configure(background='gray20')
    Label(small, text="Personal Meeting Rooms", anchor="w", bg="gray20", fg="white",font=('Times New Roman', '20')).place(x=155, y=0, height=40, width=440)
    Button(small, text='Mr. Beradino', command=comp_sci_, bg="blue", fg="white", highlightbackground="blue").place(x=35, y=50, height=32, width=115)
    Button(small, text='Dr. Cobos', command=knowTheory, bg="pink", fg="black",highlightbackground="pink").place(x=35, y=150, height=32, width=115)
    Button(small, text='Mr. Grisbee', command=mathSL, bg="orange", fg="black", highlightbackground="orange").place(x=35,y=250, height=32, width=115)
    Button(small, text='Mr. Jacobs', command=mathStudies, bg="orange", fg="black", highlightbackground="orange").place(x=35, y=350, height=32, width=115)
    Button(small, text='Ms. Vasquez', command=artEleven, bg="yellow", fg="black", highlightbackground="yellow").place(x=200, y=50, height=32, width=115)
    Button(small, text='Ms. Sloan', command=artTwelve, bg="yellow", fg="black", highlightbackground="yellow").place(x=200, y=150, height=32, width=115)
    Button(small, text='Ms. Bowman', command=thEAtre, bg="yellow", fg="black", highlightbackground="yellow").place(x=200, y=250, height=32,width=115)
    Button(small, text='Ms. Harrison', command=filmClass, bg="white", fg="black", highlightbackground="white").place(x=200,y=350,height=32,width=115)
    Button(small, text='Mr. Zhou', command=chineseClass, bg="red", fg="white", highlightbackground="red").place(x=368,y=50,height=32,width=115)
    Button(small, text='Ms. Novak', command=spanishClass, bg="red", fg="white", highlightbackground="red").place(x=368,y=150,height=32,width=115)
    Button(small, text='Mr. Roddy', command=gpHC, bg="blue", fg="white", highlightbackground="blue").place(x=368,y=250,height=32,width=115)
    Button(small, text='Dr. Quillin', command=ecON, bg="blue", fg="white", highlightbackground="blue").place(x=368, y=350,height=32,width=115)
    Button(small, text='Ms. Mayhew', command=chemISTRY, bg="purple", fg="white", highlightbackground="purple").place(x=35, y=450, height=32, width=115)
    Button(small, text='Dr. Ott', command=bioLOGY, bg="purple", fg="white", highlightbackground="purple").place(x=200,y=450,height=32,width=115)
    Button(small, text='Mr. Dorsey', command=coLLEGE, bg="white", fg="black", highlightbackground="white").place(x=368, y=450, height=32, width=115)
    Button(small, text='Dr. Lee', command=lEE, bg="white", fg="black", highlightbackground="white").place(x=35, y=450, height=32, width=115)
    Button(small, text='Ms. Pilisi', command=heALTH, bg="pink", fg="black", highlightbackground="pink").place(x=200, y=450, height=32, width=115)
    Button(small, text='Mr. Lowery', command=lowERY, bg="white", fg="black", highlightbackground="white").place(x=200, y=550, height=32, width=115)
#This function is user-specific, it allows the user to choose their own presets for links and meetings to make the use of this app more streamline.

Entry1_var = StringVar()
Entry2_var = StringVar()
Entry3_var = StringVar()
Entry4_var = StringVar()
Entry5_var = StringVar()
Entry6_var = StringVar()
Entry7_var = StringVar()
Entry8_var = StringVar()
Entry9_var = StringVar()


def loadEntry():
    varArray = [Entry1_var,Entry2_var,Entry3_var,Entry4_var,Entry5_var,Entry6_var,Entry7_var,Entry8_var,Entry9_var]
    with open('pref.ini','r') as file:
        data = file.readlines()
        #print(data)
    #print(len(data))
    #print(var10)
    counter = 9
    var_counter = 0
    for i in data[9:]:
        print(i)
        if i != '\n':
            #data[10] = (var10)
            #Entry1_var.set(i)
            varArray[var_counter].set(i.rstrip("\n"))
        counter = counter + 1
        var_counter = var_counter +1
loadEntry()

def saveEntry():
    with open('pref.ini','r') as file:
        data = file.readlines()
    print(data)
    var1 = Entry1_var.get().rstrip("\n") +"\n"
    data[9] = var1
    var2 = Entry2_var.get().rstrip("\n") +"\n"
    data[10] = var2
    var3 = Entry3_var.get().rstrip("\n") +"\n"
    data[11] = var3
    var4 = Entry4_var.get().rstrip("\n") +"\n"
    data[12] = var4
    var5 = Entry5_var.get().rstrip("\n") +"\n"
    data[13] = var5
    var6 = Entry6_var.get().rstrip("\n") +"\n"
    data[14] = var6
    var7 = Entry7_var.get().rstrip("\n") +"\n"
    data[15] = var7
    var8 = Entry8_var.get().rstrip("\n") +"\n"
    data[16] = var8
    var9 = Entry9_var.get().rstrip("\n")
    data[17] = var9
    with open('pref.ini','w') as file:
        file.writelines(data)
    print(data)
def getEntry():

    if(box19s.get()=='1'):
        LocalEntry1_var = Entry1_var.get()
        new = 1
        url = LocalEntry1_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry1_var)

    if (box20s.get() == '1'):
        LocalEntry2_var = Entry2_var.get()
        new = 1
        url = LocalEntry2_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry2_var)

    if (box21s.get() == '1'):
        LocalEntry3_var = Entry3_var.get()
        new = 1
        url = LocalEntry3_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry3_var)

    if (box22s.get() == '1'):
        LocalEntry4_var = Entry4_var.get()
        new = 1
        url = LocalEntry4_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry4_var)

    if (box23s.get() == '1'):
        LocalEntry5_var = Entry5_var.get()
        new = 1
        url = LocalEntry5_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry5_var)

    if (box24s.get() == '1'):
        LocalEntry6_var = Entry6_var.get()
        new = 1
        url = LocalEntry6_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry6_var)

    if (box25s.get() == '1'):
        LocalEntry7_var = Entry7_var.get()
        new = 1
        url = LocalEntry7_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry7_var)

    if (box26s.get() == '1'):
        LocalEntry8_var = Entry8_var.get()
        new = 1
        url = LocalEntry8_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry8_var)

    if (box27s.get() == '1'):
        LocalEntry9_var = Entry9_var.get()
        new = 1
        url = LocalEntry9_var
        webbrowser.open(url, new=new)
        print("Going to " + LocalEntry9_var)

def customPreset():
    small = Toplevel(master)
    small.title("Custom Saved Presets")
    small.geometry('600x300')
    small.configure(background='gray30')
    Label(small, text="User's Custom Presets", anchor="w", bg="gray30", fg="White",font=('Times New Roman', '20')).place(x=210, y=0, height=40, width=300)
    Button(small, text='Search', command=getEntry, bg='green', fg='white', highlightbackground='green').place(x=340,y=246, height=35,width=70)  # search button
    global Entry1,Entry2,Entry3,Entry4,Entry5, Entry6, Entry7,Entry8,Entry9
    #Left Entry Boxes
    Entry1 = Entry(small, textvariable = Entry1_var).place(x=40,y=75, height=30,width=145)
    Entry2 = Entry(small, textvariable = Entry2_var).place(x=40, y=135, height=30, width=145)
    Entry3 = Entry(small, textvariable = Entry3_var).place(x=40, y=190, height=30,width=145)
    #Middle Entry Boxes
    Entry4 = Entry(small, textvariable = Entry4_var).place(x=230, y=75, height=30, width=145)
    Entry5 = Entry(small, textvariable = Entry5_var).place( x=230, y=135, height=30, width=145)
    Entry6 = Entry(small, textvariable = Entry6_var).place(x=230, y=190, height=30, width=145)
    #Right Entry Bozes
    Entry7 = Entry(small, textvariable = Entry7_var).place( x=420, y=74, height=30, width=145)
    Entry8 = Entry(small, textvariable = Entry8_var).place(x=420, y=135, height=30,width=145)
    Entry9 = Entry(small, textvariable = Entry9_var).place(x=420,y=190, height=30,width=145)

    #Set Button
    Button(small, text='Set', command=saveEntry, bg='white', fg='black', highlightbackground='white').place(x=200,y=246, height=35,width=70)
#Search Check Boxes

    #Left Search Check Boxes
    global box19s,box19
    box19s = StringVar()
    box19 = Checkbutton(small,text="Search", variable=box19s,bg="gray30",fg="white")
    box19.deselect()
    box19.place(x=90,y=50)


    global box20s,box20
    box20s = StringVar()
    box20 = Checkbutton(small, text="Search", variable=box20s, bg="gray30", fg="white")
    box20.deselect()
    box20.place(x=90, y=110)

    global box21s,box21
    box21s = StringVar()
    box21 = Checkbutton(small, text="Search", variable=box21s, bg="gray30", fg="white")
    box21.deselect()
    box21.place(x=90, y=165)

    #Middle Search Check Boxes
    global box22s,box22
    box22s = StringVar()
    box22 = Checkbutton(small, text="Search", variable=box22s, bg="gray30", fg="white")
    box22.deselect()
    box22.place(x=275, y=50)

    global box23s,box23
    box23s = StringVar()
    box23 = Checkbutton(small, text="Search", variable=box23s, bg="gray30", fg="white")
    box23.deselect()
    box23.place(x=275, y=110)

    global box24s,box24
    box24s = StringVar()
    box24 = Checkbutton(small, text="Search", variable=box24s, bg="gray30", fg="white")
    box24.deselect()
    box24.place(x=275, y=165)

    #Right Search Check Boxes
    global box25s,box25
    box25s = StringVar()
    box25 = Checkbutton(small, text="Search", variable=box25s, bg="gray30", fg="white")
    box25.deselect()
    box25.place(x=460, y=50)

    global box26s,box26
    box26s = StringVar()
    box26 = Checkbutton(small, text="Search", variable=box26s, bg="gray30", fg="white")
    box26.deselect()
    box26.place(x=460, y=110)

    global box27s,box27
    box27s = StringVar()
    box27 = Checkbutton(small, text="Search", variable=box27s, bg="gray30", fg="white")
    box27.deselect()
    box27.place(x=460, y=165)
    #6 entry boxes two checkmarks on each side of a check box(Set and Search)

def customLink():
    new = 1
    url = " "
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
def coLLEGE():
    new = 1
    url = "https://postoakschool.zoom.us/j/7773704334"
    webbrowser.open(url, new=new)
    print("Taking you to Mr. Dorsey...")
def lEE():
    new = 1
    url = "https://postoakschool.zoom.us/j/6493991948?pwd=MHR3MEpsbHNwcDVCRE9Tc09TVzlFQT09"
    webbrowser.open(url, new=new)
    print("Taking you to Dr. Lee...")
def heALTH():
    new = 1
    url = "https://postoakschool.zoom.us/j/7489168410"
    webbrowser.open(url, new=new)
    print("Taking you to Ms. Pilisi...")
def lowERY():
    new = 1
    url = "https://postoakschool.zoom.us/j/3054948681?pwd=NGs3YTZnaXQvOXM5bTZ6QXBoNFdtZz09"
    webbrowser.open(url, new=new)
    print("Taking you to Mr. Lowery...")


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
