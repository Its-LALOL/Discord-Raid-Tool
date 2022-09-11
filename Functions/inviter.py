import requests
from tkinter import Tk, Button, Label, Entry, INSERT, messagebox
from pyperclip import paste
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver
from os import system
from threading import Thread

isexit=False
clear=lambda: system('cls||clear')

def starter():
	Thread(target=start).start()
def start():
	file=open('Functions/tokens.txt', encoding='utf-8')
	for token in file:
		if isexit:
			window.destroy()
			exit()
			return
		token=token.replace('\n', '')
		response=requests.get('https://discord.com/api/v9/users/@me/library',headers={'Authorization': token})
		if response.status_code==200 or response.status_code==202 or response.status_code==204:
			driver=undetected_chromedriver.Chrome()
			clear()
			driver.maximize_window()
			driver.get(invite.get())
			driver.execute_script('function login(token){setInterval(()=>{document.body.appendChild(document.createElement`iframe`).contentWindow.localStorage.token=`"${token}"`},50);setTimeout(()=>{},2500)}login("' + token + '");')
			driver.get(invite.get())
			sleep(5)
			driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/section/div/button').click()
			print('Please solve capthca')
			while True:
				if driver.current_url!=invite:
					clear()
					driver.quit()
					del driver
					break
				sleep(0.5)
	messagebox.showinfo('Raid Tool by LALOL | Inviter', 'All valid accounts joined!')
def exitt():
	global isexit
	isexit=True
	window.destroy()
	exit()
def paste_invite():
	textt=paste()
	invite.insert(INSERT, textt)
window=Tk()
window.geometry('400x74')
window.resizable(width=False, height=False)
window.title('Raid Tool by LALOL | Inviter')
window.protocol("WM_DELETE_WINDOW", exitt)
window.config(bg='black')
Label(text='Invite: ', fg='white', bg='black', font=('Fixedsys', 10)).place(x=0,y=0)
invite=Entry(width=32, fg='black', bg='grey', font=('Fixedsys', 10))
invite.place(x=140, y=0)
Button(text='Paste', fg='black', bg='grey', command=paste_invite).place(x=103, y=0)
Button(text='Start', fg='yellow', bg='grey', font=('Georgia', 13), command=starter).place(x=0, y=40)
window.mainloop()
