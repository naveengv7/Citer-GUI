#import necessory libraries
from tkinter import *
from tkinter import Canvas, Entry, Text, Button, PhotoImage, filedialog
from PIL import Image, ImageTk

root =Tk()
root.geometry("900x600")
root.title('CITER FACE QUALITY ASSESMENT')
root.configure(bg = "#FFFFFF")

sub_name_var=StringVar()
sub_id_var=StringVar()

#Create left canvas for start page
left_canvas = Canvas(
	root,
	bg = "#FFFFFF",
	height = 600,
	width = 360,
	bd = 0,
	highlightthickness = 0,
	relief = "ridge"
)
left_canvas.place(x=0,y=0)

#Citer logo
citer_img = ImageTk.PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/CITeR-logo.png')
left_canvas.create_image(
	0, 
	0, 
	image=citer_img, 
	anchor=NW
)

left_canvas.create_text(
	0,
	90,
	anchor="nw",
	text="Welcome",
	fill="#4A5568",
	font=("Roboto", 24 * -1)
)

left_canvas.create_text(
	0,
	130,
	anchor="nw",
	text="Fill out the form and\nclick start button to start",
	fill="#1A202C",
	font=("RobotoRoman SemiBold", 24 * -1)
)

left_canvas.create_text(
	0,
	200,
	anchor="nw",
	text="Subject name",
	fill="#4A5568",
	font=("Roboto", 24 * -1)
)

left_canvas.create_text(
	0,
	300,
	anchor="nw",
	text="Subject ID",
	fill="#4A5568",
	font=("Roboto", 24 * -1)
)

entry_1 = Entry(
	bd=0,
	bg="#FFFFFF",
	font=("Roboto", 24 * -1),
	highlightthickness=1,
	textvariable=sub_name_var
)
entry_1.place(
	x=0,
	y=245,
	width=360,
	height=40
)

entry_2 = Entry(
	bd=0,
	bg="#FFFFFF",
	font=("Roboto", 24 * -1),
	highlightthickness=1,
	textvariable=sub_id_var
)
entry_2.place(
	x=0,
	y=345,
	width=360,
	height=40
)

start_button = Button(
	bd=0,
	bg="#04C35C",
	fg="#FFFFFF",
	text="Start",
	font=("Roboto", 30 * -1),
	borderwidth=0,
	highlightthickness=0,
	command=lambda: print("start clicked"),
	relief="solid"
)
start_button.place(
	x=0,
	y=410,
	width=360,
	height=50
)

stop_button = Button(
	bd=0,
	bg="#1B1D1C",
	fg="#FFFFFF",
	text="Stop",
	font=("Roboto", 30 * -1),
	borderwidth=0,
	highlightthickness=0,
	command=lambda: print("Stop clicked"),
	relief="solid"
)

stop_button.place(
	x=0,
	y=480,
	width=360,
	height=50
)	

right_canvas1 = Canvas(
	root,
	bg = "#545151",
	height = 300,
	width = 270,
	bd = 0,
	highlightthickness = 3,
	relief = "ridge"
)

#Create right side canvas for camera frames
right_canvas1.place(x=360,y=0)

citer_img1 = PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/start.png')

camera_frame1=Frame(right_canvas1)
camera_frame1.pack()
camera_panel1=Label(camera_frame1, image=citer_img1)
camera_panel1.pack()


right_canvas2 = Canvas(
	root,
	bg = "#545151",
	height = 300,
	width = 270,
	bd = 0,
	highlightthickness = 3,
	relief = "ridge"
)
right_canvas2.place(x=630,y=0)

citer_img2 = PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/start.png')

camera_frame2=Frame(right_canvas2)
camera_frame2.pack()
camera_panel2=Label(camera_frame2, image=citer_img2)
camera_panel2.pack()

right_canvas3 = Canvas(
	root,
	bg = "#545151",
	height = 300,
	width = 270,
	bd = 0,
	highlightthickness = 3,
	relief = "ridge"
)

citer_img3 = PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/start.png')

camera_frame3=Frame(right_canvas3)
camera_frame3.pack()
camera_panel3=Label(camera_frame3, image=citer_img3)
camera_panel3.pack()

right_canvas3.place(x=360,y=300)

citer_img = PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/start.png')

right_canvas4 = Canvas(
	root,
	bg = "#545151",
	height = 300,
	width = 270,
	bd = 0,
	highlightthickness = 3,
	relief = "ridge"
)

right_canvas4.place(x=630,y=300)

camera_frame4=Frame(right_canvas4)
camera_frame4.pack()
camera_panel4=Label(camera_frame4, image=citer_img1)
camera_panel4.pack()

#main loop
root.resizable(False,False)
root.mainloop()