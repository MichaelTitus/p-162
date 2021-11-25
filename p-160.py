from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("NOTEPAD")


open_image=ImageTk.PhotoImage(Image.open("openfile.png"))
play_image=ImageTk.PhotoImage(Image.open("play.png"))
save_image=ImageTk.PhotoImage(Image.open("save.png"))

label_file_name=Label(root,text="File Name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.58,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

name=""

def open_file():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file=filedialog.askopenfilename(title="open text file",filetypes=(("Text Files","*.html"),))
    print(text_file)
    name=os.path.basename(text_file)
    formattedname=name.split('.')[0]
    root.title(formattedname)
    text_file=open(text_file,'r')
    para=text_file.read()
    my_text.insert(END,para)
    text_file.close()  

def save():
    input_name=input_file_name.get()
    file=open(input_name+".html",'w')
    data=my_text.get(1.0,END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","success")
    
def play():
    global name
    filepath=""
    webbrowser.open_file(filepath)
    
    
    
    
open_button=Button(root,image=open_image,text="Open File",command=open_file)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

play_button=Button(root,image=play_image,text="play",command=play)
play_button.place(relx=0.09,rely=0.03,anchor=CENTER)

save_button=Button(root,image=save_image,text="Save",command=save)
save_button.place(relx=0.13,rely=0.03,anchor=CENTER)




root.mainloop()