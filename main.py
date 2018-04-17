from tkinter import *
from tkinter import filedialog
import cv2
import os
from capture import Capture_Image
from GenerateCaption import Caption
import PIL
from PIL import Image, ImageTk
import time
from time import sleep
from sendemail import email
import GenerateVoice as GV

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

#new window for caption display
def Caption_Window(image_path, sentence):
	caption = Toplevel()
	caption.title("Caption Generated - Drishti")
	canvas_width = 400
	canvas_height =400
	canvas = Canvas(caption,width=canvas_width,height=canvas_height)
	canvas.pack()
	Filter_Phone=['smartphone', 'phone', 'mobile', 'Smartphone', 'Phone' ,'Mobile']
	caps = str(sentence)
	for content in Filter_Phone:
		if content in caps:
			sleep(0.05)
			GV.speak("Can not display image")
			image_name = 'blocked.jpg'
			print("Can not display image")
			break		
		else:
			image_name = image_path
	#resizing of the image
	r_image = cv2.imread(image_name)
	r_image = cv2.resize(r_image,(400,400))
	#to write the caption over the image
	font = cv2.FONT_HERSHEY_SIMPLEX
	#cv2.putText(r_image,caps,(10,350), font, 5,(72,61,139),2)
	cv2.imwrite(image_name, r_image) 
	img = ImageTk.PhotoImage(Image.open(image_name))
	canvas.create_image(0,0, anchor=NW, image=img)

	head = Label(caption, text = "Generated Caption") 
	head.pack(side = TOP)
	message = Label(caption, text = sentence)
	message.pack( side = TOP )
	def play():
		os.system('play caption.wav')
	b1=Button(caption, text="Replay", command= play)
	b1.pack(padx=20, pady=5)
	
	#Function to send email
	def Email(image_path,sentence):
		#calls the email() function of sendemail file by creating obj
		mail_obj = email()
		mail_obj.configure('Sender Email ID','password')
		sender = 'Sender Email ID'
		password = 'Sender Email Password'
		message = sentence
		receivers = ['Email ID']
		lst = [image_path,'caption.wav']
		mail_obj.send_email('Sender\'s Email ID',password,lst,receivers,message)

	b2=Button(caption, text="Send as Email", command= lambda: Email(image_name,sentence))
	b2.pack(padx=20, pady=5)

	caption.mainloop()
	


#to capture real time image
def Capture_Img():
    img = Capture_Image()
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), img)

    sentence=Caption(image_path, '')
    Caption_Window(image_path, sentence)

#to use the stored images
def Stored_Img():

    def Openfile():
        image_name = filedialog.askopenfilename(initialdir = "/ImageCaptioning/Images/",title = "Select file",filetypes = (("jpg files","*.jpg"),("all files","*.*")))
        return (image_name)

    image_path=Openfile()
    sentence=Caption(image_path, ' ') 
    Caption_Window(image_path, sentence)

    
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