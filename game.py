#number guessing game project
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import math
import random
class NumGuess:
    def __init__(self,root):
        self.root=root
        self.root.geometry("700x550+420+70")
        self.root.title('Number Guessing Game')
        self.root.resizable(False,False)
        self.root.configure(background='blue')
        self.heading=Label(self.root,text='Number Guessing Game',font=('impact',30,'bold'),background='blue')
        self.heading.pack(pady=5)
        
        #variable
        self.getrandomvalue=StringVar()
        self.getguessNumber=StringVar()
        self.getval=StringVar()
        #--------------
        #you have only 7 chances
        self.noteFrame=Frame(self.root,relief=RIDGE,background='red',width=693,height=55)
        self.noteFrame.place(x=3,y=70)
        
        #image add 1 in frame 1
        image_1=Image.open(r'D:\Number Guessing Game\Photo\431-4317544_backhand-index-pointing-right-icon-finger-pointing-right.png')
        image_1=image_1.resize((50,50))
        self.photo1=ImageTk.PhotoImage(image_1)
        self.imageLabel=Label(self.noteFrame,image=self.photo1)
        self.imageLabel.place(x=0,y=0)
        
        randomNum=Label(self.noteFrame,text="You've only 7 chances to guess the number..",font=('times new roman',20,'bold'),background='red')
        randomNum.place(x=100,y=5)
        
        self.statusFrame=Frame(self.root,relief=RIDGE,background='yellow')
        self.statusFrame.place(x=3,y=140,width=693,height=50)
        
        totalchance=Label(self.statusFrame,text='Total Chance:',font=('times new roman',20,'bold'),background='yellow')
        totalchance.grid(row=0,column=0,pady=2,padx=5)
        
        
        totalEntry=Entry(self.statusFrame,font=('times new roman',20,'bold'),width=5,background='yellow',justify='center')
        totalEntry.grid(row=0,column=1,pady=7,padx=40)
        totalEntry.insert(7,7)
        
        leftchance=Label(self.statusFrame,text='Left Chance:',font=('times new roman',20,'bold'),background='yellow')
        leftchance.grid(row=0,column=2,pady=2,padx=50)
        
        
        leftEntry=Entry(self.statusFrame,textvariable=self.getval,font=('times new roman',20,'bold'),width=5,background='yellow',justify='center')
        leftEntry.grid(row=0,column=3,pady=7)
        leftEntry.insert(7,7)
        
        self.gameFrame=Frame(self.root,relief=RIDGE,background='cyan')
        self.gameFrame.place(x=3,y=200,width=693,height=300)
        
        randomNum=Label(self.gameFrame,text='Generate A Number Between 0 and ',font=('times new roman',20,'bold'),background='cyan')
        randomNum.grid(row=0,column=0,padx=15,pady=15)
        self.randomNumEntry=ttk.Entry(self.gameFrame,textvariable=self.getrandomvalue,font=('times ew roman',15,'bold'),width=10,justify='center')
        self.randomNumEntry.grid(row=0,column=1,padx=3,pady=3)
        
                
        guessNum=Label(self.gameFrame,text='Guess The Number ',font=('times new roman',20,'bold'),background='cyan')
        guessNum.grid(row=1,column=0,padx=15,pady=3)
        guessNumEntry=ttk.Entry(self.gameFrame,font=('times ew roman',15,'bold'),textvariable=self.getguessNumber,width=10,justify='center')
        guessNumEntry.grid(row=1,column=1,padx=3,pady=3)
        #generate
        genbtn=Button(self.gameFrame,text='Generate',command=self.randomGenerate,font=('times new roman',14,'bold'),background='yellow',width=8)
        genbtn.grid(row=0,column=3,pady=5,padx=10)
        
        #play button
        playbtn=Button(self.gameFrame,text='Play',command=self.play,font=('times new roman',14,'bold'),background='yellow',width=8)
        playbtn.grid(row=1,column=3,pady=5,padx=10)
        #output show of random number
        self.output=Text(self.gameFrame,font=('times new roman',22,'bold'),background='cyan')
        self.output.place(x=3,y=130,height=50,width=687)
        #start new game
        self.newgame=Button(self.gameFrame,command=self.newGame,text='New Game',font=('times new roman',14,'bold'),width=8,background='yellow')
        self.newgame.place(x=300,y=210)
        
    #logic game 
    global x 
    global val    
    global count
       
    def randomGenerate(self):
        try:
            self.val=int(self.getrandomvalue.get())
            self.x=random.randint(0,self.val)
        except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    
    def play(self):
        self.count=0
        while self.count<math.log(self.val-0+1,2):
            self.output.delete(1.0,END)
            guessNum=int(self.getguessNumber.get())
            
            if(self.x==guessNum and int(self.getval.get())>=0):
                self.output.insert(END,'\tcongratulation,You won the game!!')
                self.remain=int(self.getval.get())-1
                self.getval.set(str(self.remain))
                break
            
            elif self.x>guessNum and int(self.getval.get())>=0:
                self.output.insert(END,'\t\tyou guess too small!!')
                self.remain=int(self.getval.get())-1
                self.getval.set(str(self.remain))
                break
        
            elif self.x< guessNum and int(self.getval.get())>=0:
                self.output.insert(END,'\t\tyou guess too large!!')
                self.remain=int(self.getval.get())-1
                self.getval.set(str(self.remain))
                break
            
        if(int(self.getval.get())<=0):
            self.getval.set('0')
            
        if(int(self.getval.get())==0 and self.x != guessNum):
            self.output.delete(1.0,END)
            self.output.insert(END,'\t\tButter luck next time!!')

        
    def newGame(self):
        self.getguessNumber.set('')
        self.getrandomvalue.set('')
        self.output.delete(1.0,END)
        self.getval.set('7')

splash_win=Tk()
splash_win.geometry("700x550+420+70")
splash_win.overrideredirect(1)
splash_win.configure(background='brown')
guessImage=Image.open(r'D:\Number Guessing Game\Photo\maxresdefault.jpg')
guessImage=guessImage.resize((700,550))
photo1=ImageTk.PhotoImage(guessImage)
imageLabel=Label(splash_win,image=photo1)
imageLabel.place(x=0,y=0)


def mainWin():
    splash_win.destroy()
    root=Tk()
    NumGuess(root)
    
splash_win.after(4500,mainWin)
mainloop()