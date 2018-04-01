from tkinter import *
from tkinter import filedialog
import cv2
import os
from capture import Capture_Image
from GenerateCaption import caption
import PIL
from PIL import Image

window=Tk()

window.title("Drishti - Vision for Life")

#introducing window
def About():
    about=Tk()
    about.title("About Drishti - Vision for Life")
    message = Label( about, text = """
    Drishti is a Software that provides information to the blind about the surrounding
    1. Real Time Image Annotation
    2. Stored Image Annotation
    """ )
    message.pack( side = TOP)
    about.geometry('500x100')

    about.mainloop()

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)

#to tae real time image
def Capture_Img():
	img = Capture_Image()
	#im = Image.open(img)
	#im.show()
	caption(img, 'Cloud Sight API Key')


#to use the stored images
def Stored_Img():

	def Openfile():
		image_name = filedialog.askopenfilename(initialdir = "/ImageCaption/Images/",title = "Select file",filetypes = (("jpg files","*.jpg"),("all files","*.*")))
		return (image_name)

	image_path=Openfile()	
	caption(image_path, 'Cloud Sight API Key')


# introducing window structure
canvas_width = 650
canvas_height =470
canvas = Canvas(window,
           width=canvas_width,
           height=canvas_height)
canvas.pack()


img = PhotoImage(file = "drishti.png")
canvas.create_image(0,0, anchor=NW, image=img)

message = Label( window, text = "Select any one of the following services" )
message.pack( side = TOP )

b1=Button(window, text="Capture Image", command= Capture_Img)
b1.pack(padx=20, pady=5)

b2=Button(window, text="Use Stored Image", command= Stored_Img)
b2.pack(padx=20, pady=5)

window.mainloop()