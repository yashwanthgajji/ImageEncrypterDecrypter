import tkinter
import os
from tkinter.filedialog import askopenfilename,askdirectory
import ImageEncryptDecrypt as ied
global image_path,key,destination_folder
def select_file():
	global image_path
	filename = askopenfilename()
	image_path=filename
	file_text.set(image_path)

def get_key():
	global key
	key=int(key_text.get(),base=10)

def select_destination_folder():
	global destination_folder
	dest_loc=askdirectory()
	destination_folder=dest_loc
	folder_text.set(destination_folder)

def encrypt_function():
	get_key()
	enc=ied.Encrypt(image_path,key,destination_folder)
	enc.convert()
	convert_text.set("Immage is Encrypted")
	print("Encrypted")

def decrypt_function():
	get_key()
	dec=ied.Decrypt(image_path,key,destination_folder)
	dec.convert()
	convert_text.set("Image is Decrypted")
	print("Decrypted")

def clear_function():
	file_text.set("");
	folder_text.set("");
	convert_text.set("");
	key_text.delete(0,"end");
	image_path="";
	destination_folder="";
	key="";

window = tkinter.Tk()
window.title("Image Encrypter and Decrypter")
# window.geometry("500x500")
tkinter.Label(window,text="Image Encrypter Decrypter").grid(row=0,column=1)
tkinter.Label(window,text="Select Image").grid(row=1)
file_button=tkinter.Button(window,text="Choose Image File",command=select_file).grid(row=1,column=1)
file_text=tkinter.StringVar()
file_label=tkinter.Label(window,textvariable=file_text).grid(row=1,column=2)
tkinter.Label(window,text="Enter any Key between 1 to 256").grid(row=2)
key_text = tkinter.Entry(window)
key_text.grid(row=2, column=1)
tkinter.Label(window,text="Select Destination Folder").grid(row=3)
folder_button=tkinter.Button(window,text="Choose Destination Folder",command=select_destination_folder).grid(row=3,column=1)
folder_text=tkinter.StringVar()
folder_label=tkinter.Label(window,textvariable=folder_text).grid(row=3,column=2)
encrypt_button=tkinter.Button(window, text ="Encrypt",command=encrypt_function).grid(row=4,column=0)
decrypt_button=tkinter.Button(window, text ="Decrypt",command=decrypt_function).grid(row=4,column=1)
clear_button=tkinter.Button(window, text ="Clear",command=clear_function).grid(row=4,column=2)
convert_text=tkinter.StringVar()
convert_label=tkinter.Label(window,textvariable=convert_text).grid(row=5,column=1)
window.mainloop()