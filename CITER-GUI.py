from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk,ImageDraw
#import cv2
#import os,time
#from datetime import datetime

def stop_scan():
    pass

def start_camera_capture():
    pass

###########################
### GUI START
###########################

root = Tk()
root.title('CITER FACE QUALITY ASSESMENT')

#getting screen width and height of display
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry(f'{width}x{height}')

root.geometry("%dx%d" % (900, 600))

left_frame = Frame(root)
left_frame.pack(side=LEFT,anchor=NW)
#left_frame.grid(row=0,column=0,padx=0,pady=0)

right_frame = Frame(root)
right_frame.pack(side=RIGHT)
#right_frame.place(x=360,y=0)


#show logo
citer_logo = PhotoImage(file = 'CITeR-logo.png')
logo_label=Label(left_frame, image=citer_logo)
logo_label.grid(row=0,column=0)
#show logo end


#first frame start
message_frame = Frame(left_frame)
message_frame.grid(row=1, column=0, padx=0, pady=10)
message_frame.grid_columnconfigure(0, weight=360)

message_label=Label(message_frame, text="Fill out the form and \nclick start button to start",font=('Aerial 15 bold'),anchor=N)
message_label.grid(row=0, column=0, padx=0, pady=0)
#first frame end


#form frame start
form_frame =Frame(left_frame)
form_frame.grid(row=2, column=0, padx=0, pady=10)

sub_name_var=StringVar()
sub_id_var=StringVar()
sub_name_var.set("test_subject")
sub_id_var.set("1") 

sub_name_label = Label(form_frame,text="Subject Name")
#sub_name_label.place(width=360)
sub_name_label.grid(row=0, column=0, padx=0, pady=10)
sub_name_entry = Entry(form_frame,textvariable=sub_name_var,width=50)
sub_name_entry.grid(row=1, column=0, padx=0, pady=10)
sub_id_label = Label(form_frame,text="Subject Id")
sub_id_label.grid(row=2, column=0, padx=0, pady=10)
sub_id_entry = Entry(form_frame,textvariable=sub_id_var,width=50)
sub_id_entry.grid(row=3, column=0, padx=0, pady=10)


#Start button
start_button = Button(left_frame,bd=0,bg="#04C35C",fg="#FFFFFF",text="Start",font=("Roboto", 30 * -1),borderwidth=0,
                        highlightthickness=0,command=start_camera_capture,relief="groove")
#start_button.place(x=0,y=410,width=360,height=50)
start_button.grid(row=4, column=0, padx=0, pady=10)

#Stop button
stop_button = Button(left_frame,bd=0,bg="#1B1D1C",fg="#FFFFFF",text="Stop",font=("Roboto", 30 * -1),borderwidth=0,highlightthickness=0,
                        command=stop_scan,relief="raised")
#stop_button.place(x=0,y=480,width=360,height=50)
stop_button.grid(row=5, column=0, padx=0, pady=10)

#form frame end


# camera frame start 
camera_frame =Frame(right_frame,bg="gray")
camera_frame.pack()

#add new camera panel
camera_panel = Label(camera_frame)
camera_panel.pack()

#camera frame end

#root.iconbitmap('/home/baset/Activity/clarkson/gui/final/icon.ico')
#root.iconphoto(False, PhotoImage(file='asset/icon.png'))
root.resizable(False,False)
root.mainloop()