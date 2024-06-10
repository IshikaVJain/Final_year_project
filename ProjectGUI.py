import tkinter as tk

from tkinter import font as tkfont
import subprocess
from tkinter import messagebox, PhotoImage
from tkinter import font as tkfont
from PIL import Image, ImageTk

import subprocess
import pyttsx3
import datetime
import speech_recognition as sr

script1="objectdetection.py"
script2="VoiceAsst.py"


script1="objectdetection.py"   #Button1


script2="VoiceAsst.py"    #Button2


def button1_click():
    # messagebox.showinfo("Button 1 Clicked", "You clicked Button 1!")
    script1="objectdetection.py"
    subprocess.run(['python',script1],bufsize=4096)

def button2_click():
    # messagebox.showinfo("Button 2 Clicked", "You clicked Button 2!")
    script2="VoiceAsst.py" 
    subprocess.run(['python',script2],bufsize=4096)






# Create the main tkinter window
root = tk.Tk()
root.title("JYOTHI-Assistant for Visually Impaired Project")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

root.config(bg="blue")

image = Image.open("bg1.png")  # Specify the path to your image
image = image.resize((800, 600), Image.LANCZOS)  # Resize the image as needed
background_image = ImageTk.PhotoImage(image)

# Create a label to display the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # P

# Create a custom font for the label
custom_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

# Create a label widget
label = tk.Label(root, text="JYOTHI-Assistant for Visually Impaired Project", font=custom_font)
label.pack(pady=20)

# Create Button 1
button1 = tk.Button(root, text="Object Detection", command=button1_click)
button1.pack(pady=10, padx=20)

# Create Button 2
button2 = tk.Button(root, text="Voice Assistant", command=button2_click)
button2.pack(pady=10, padx=20)


button1.place(x=650, y=65)
button2.place(x=800, y=65)

# Start the tkinter main event loop







root.mainloop()
