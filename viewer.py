from tkinter import *
from PIL import ImageTk,Image
import os
from untitled1 import randomPicture
root = Tk()
root.title('Codemy.com Image Viewer')
root.iconbitmap('c:/gui/codemy.ico')



my_img11=Image.open(randomPicture(26))
my_img12=my_img11.resize((700,700),Image.ANTIALIAS)
my_img1=ImageTk.PhotoImage(my_img12)

my_img21=Image.open(randomPicture(26))
my_img22=my_img21.resize((700,700),Image.ANTIALIAS)
my_img2=ImageTk.PhotoImage(my_img22)

my_img31=Image.open(randomPicture(26))
my_img32=my_img31.resize((700,700),Image.ANTIALIAS)
my_img3=ImageTk.PhotoImage(my_img32)

my_img41=Image.open(randomPicture(26))
my_img42=my_img41.resize((700,700),Image.ANTIALIAS)
my_img4=ImageTk.PhotoImage(my_img42)

my_img51=Image.open(randomPicture(26))
my_img52=my_img51.resize((700,700),Image.ANTIALIAS)
my_img5=ImageTk.PhotoImage(my_img52)


#my_img1 = ImageTk.PhotoImage(Image.open(randomPicture(26)))
#my_img2 = ImageTk.PhotoImage(Image.open(randomPicture(26)))
#my_img3 = ImageTk.PhotoImage(Image.open(randomPicture(26)))
#my_img4 = ImageTk.PhotoImage(Image.open(randomPicture(26)))
#my_img5 = ImageTk.PhotoImage(Image.open("E:/Pictures/melee1.png"))




image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]



my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=0, column=0)
	button_forward.grid(row=0, column=2)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=1, column=0, columnspan=3)
	button_back.grid(row=0, column=0)
	button_forward.grid(row=0, column=2)



button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.destroy)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=0, column=0)
button_exit.grid(row=0, column=1)
button_forward.grid(row=0, column=2)

root.mainloop()