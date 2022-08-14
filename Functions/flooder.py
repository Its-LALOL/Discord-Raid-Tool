import requests
from tkinter import Tk, Button, Label, Entry, INSERT
from threading import Thread
import random, string
from pyperclip import paste
from time import sleep

isexit=False

def start():
	file=open('Functions/tokens.txt', encoding='utf-8')
	number=0
	for token in file:
		token=token.replace('\n', '')
		for i in range(5):
			Thread(target=flood, args=(token, int(id.get()), text.get())).start()
def flood(token, id, message):
	while True:
		if isexit:
			window.destroy()
			exit()
			return
		chars=''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=8))
		response=requests.post(f"https://discord.com/api/v9/channels/{id}/messages", headers={'Authorization': token}, json={"content": f"{message} ||{chars}||"})
		if response.status_code==200 or response.status_code==202 or response.status_code==204:
			print('Message sented')
		elif response.status_code==429:
			rate_limit=response.json()['retry_after']
			sleep(rate_limit)
			print(f'Ratelimited {rate_limit}s')
		else:
			print(f'\nError {response.status_code}\n{token}\n{response.text}\n')
			return
def exitt():
	global isexit
	isexit=True
	window.destroy()
	exit()
def paste_text():
	textt=paste()
	text.insert(INSERT, textt)
def paste_id():
	idd=paste()
	id.insert(INSERT, idd)
window=Tk()
window.geometry('400x74')
window.resizable(width=False, height=False)
window.title('Raid Tool by LALOL | Flooder')
window.protocol("WM_DELETE_WINDOW", exitt)
window.config(bg='black')
Label(text='Text: ', fg='white', bg='black', font=('Fixedsys', 10)).place(x=0,y=0)
text=Entry(width=32, fg='black', bg='grey', font=('Fixedsys', 10))
text.place(x=140, y=0)
Button(text='Paste', fg='black', bg='grey', command=paste_text).place(x=103, y=0)
Label(text='Channel ID: ', fg='white', bg='black', font=('Fixedsys', 10)).place(x=0,y=20)
id=Entry(width=32, fg='black', bg='grey', font=('Fixedsys', 10))
id.place(x=140, y=20)
Button(text='Paste', fg='black', bg='grey', command=paste_id).place(x=103, y=20)
Button(text='Start', fg='yellow', bg='grey', font=('Georgia', 13), command=start).place(x=0, y=40)
window.mainloop()