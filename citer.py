from tkinter import *
from tkinter import Canvas, Entry, Text, Button, PhotoImage, filedialog
from PIL import Image, ImageTk

root =Tk()
root.geometry("900x600")
root.title('CITER FACE QUALITY ASSESMENT')
root.configure(bg = "#FFFFFF")

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

entry_image = ImageTk.PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/entry_1.png')
left_canvas.create_image(
	0,
	240,
	image=entry_image, 
	anchor=NW
)
left_canvas.create_image(
	0,
	340,
	image=entry_image,
	anchor=NW
)

sub_name_var=StringVar()

entry_1 = Entry(
	bd=0,
	bg="#FFFFFF",
	highlightthickness=0,
	textvariable=sub_name_var
)
entry_1.place(
	x=0,
	y=245,
	width=200,
	height=40
)

sub_id_var=StringVar()

entry_2 = Entry(
	bd=0,
	bg="#FFFFFF",
	highlightthickness=0,
	textvariable=sub_id_var
)
entry_2.place(
	x=0,
	y=345,
	width=200,
	height=40
)

start_image = ImageTk.PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/start.png')
start_button = Button(
	image=start_image,
	borderwidth=0,
	highlightthickness=0,
	command=lambda: print("start clicked"),
	relief="flat"
)
start_button.place(
	x=0,
	y=410,
	width=360,
	height=65
)

stop_image = ImageTk.PhotoImage(file='/Users/lab3/Desktop/Citer/HardCode/stop.png')
stop_button = Button(
	image=stop_image,
	borderwidth=0,
	highlightthickness=0,
	command=lambda: print("stop clicked"),
	relief="flat"
)
stop_button.place(
	x=0,
	y=500,
	width=360,
	height=65
)	


right_canvas = Canvas(
	root,
	#bg = "#FFFFFF",
	bg="#CACACA",
	height = 60,
	width = 540,
	bd = ,
	highlightthickness = 0,
	relief = "ridge"
)


'''form_frame =Frame(root)
form_frame.pack(pady=5)

# camera frame start
camera_frame =Frame(root,bg="gray")
camera_frame.pack()

#add new camera panel
camera_panel = Label(camera_frame)
camera_panel.pack()



# root frame start 
root_frame =Frame(root,bg="gray")
root_frame.pack()

#add new root panel
root_panel = Label(root_frame)
root_panel.pack()'''

#root.iconphoto(False, PhotoImage(file='icon.png'))'''

root.resizable(False,False)
root.mainloop()