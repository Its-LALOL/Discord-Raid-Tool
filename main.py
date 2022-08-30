from tkinter import Tk, Button, Label
from subprocess import Popen
from os import system

def load(name):
	Popen(f'python Functions/{name}.py || python3 Functions/{name}.py')
def flooder():
	load('flooder')
def inviter():
	load('inviter')
def tokens():
	system('start Functions/tokens.txt')
window=Tk()
window.resizable(width=False, height=False)
window.title('Raid Tool by LALOL | Menu')
window.geometry('340x666')
window.config(bg='black')
Button(text='Flooder', fg='red', bg='grey', font=('Fixedsys', 47), command=flooder).place(x=0, y=0)
Button(text='Inviter', fg='red', bg='grey', font=('Fixedsys', 47), command=inviter).place(x=0, y=139)
#Button(text='DM Flooder', fg='red', bg='grey', font=('Fixedsys', 37), command=dmflooder).place(x=-18, y=139)
Button(text='Tokens', fg='yellow', bg='grey', font=('Fixedsys', 45), command=tokens).place(x=-18, y=555)
window.mainloop()
