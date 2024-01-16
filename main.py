from tkinter import *
from tkinter import messagebox
import base64
import os
from tkinter import PhotoImage


def decrypt():
    password=code.get()
    
    if password == "1234":
        screen2=Toplevel(root)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")
        
        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,decrypt)
        
    elif password=="":
        messagebox.showerror("encryption","Input password")
    
    elif password!="1234":
        messagebox.showerror("encryption","Input password")
    
def encrypt():
    password=code.get()
    
    if password == "1234":
        screen1=Toplevel(root)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
        
    elif password=="":
        messagebox.showerror("encryption","Input password")
    
    elif password!="1234":
        messagebox.showerror("encryption","Input password")  
    
def main_screen():
    
    global root
    
    global code
    
    global text1
    
    root=Tk()
    root.geometry("500x500")
    #title
    root.title("ECD APP")
    
     # Load the image
    image2 = PhotoImage(file="EDT 2.png")    

    # Set the image as the icon
    root.iconphoto(False, image2)

    # Create a Label to display the image
    image_label = Label(root, image=image2)
    image_label.pack()
    
    
    #icon in the title
    image =PhotoImage(file="key.png")
    root.iconphoto(False,image)
    root.configure(bg="white")  # Set the background color to white or any other color

    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    #1st label
    Label(text="Enter text for encryption and decryption",font=("calibri",14)).place(x=15,y=40)
    
    text1=Text(font="Robote 20", bg="lightgray", relief=GROOVE, wrap=WORD, bd=0)

    
    text1.place(x=15,y=70,width=200,height=90)
    
    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",14)).place(x=15,y=170)
    
    code=StringVar()
    Entry(textvariable=code,width=10,bd=0,font=("arial",25),show="*",bg="lightgray").place(x=15,y=200)
    
    #buttons
    Button(text="Encrypt",height="2",width=30,bg="#ed3833",fg="white",bd=0,command=encrypt).place(x=15,y=350)
    
    Button(text="Decrypt",height="2",width=30,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=15,y=400)
    
    Button(text="Reset",height="2",width=64,bg="#1089ff",fg="white",bd=0,command=reset).place(x=15,y=450)
    
    
    root.mainloop()
    
    
main_screen()
    