from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

window = Tk() #defines window
window.title("QR Code Generator") #title for window
 


#set the window color) 
  


#generate function
def generate():
    if len(subject.get()) !=0: #length not zero
        global qr,photo 
        qr = pyqrcode.create(subject.get())
        photo = BitmapImage(data = qr.xbm(scale = 8)) #size photo and creates it
    else:
        messagebox.showinfo("Please enter a subject")
    try:
        showcode() #will show error
    except:
        pass

#showcode       
def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text = "QR of " + subject.get())


#save function
def save():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) !=0:
            qr.png(os.path.join(dir,name.get()+".png"), scale = 8)
        else:
            messagebox.showinfo("Please enter a File name")
    except:
        messagebox.showinfo("Generte the QR code first!")
        
            
    
    

    

#inputs
sub = Label(window, text = "Enter subject", fg = 'red') #what the user will enter
sub.grid(row = 0, column = 0) #so they dont mix??

fName = Label(window, text = "Enter File Name", fg = 'red',) #what to save as
fName.grid(row = 1, column = 0) #under subject

subject = StringVar() #what can be entered
subEntry = Entry(window, textvariable = subject) #the entry box for user #entry
subEntry.grid(row = 0, column = 1) #next to subject 

name = StringVar() #file name what can be entered
nameEntry = Entry(window, textvariable = name) #file
nameEntry.grid(row = 1, column = 1) #next to filename 

#buttons
button = Button(window, fg = 'red', text = "Generate", width = 15, command = generate) #(location, words on button, size, the action) 
button.grid(row = 0, column = 3)


saveButton = Button(window, fg='red', text = "Save as PNG", width = 15,  command = save)
saveButton.grid(row = 1, column = 3)



#add image label
imageLabel = Label(window) #for qr code picture
imageLabel.grid(row = 2, column = 1)

subLabel = Label(window, text="") #text under label
subLabel.grid(row = 3, column = 1)






window.mainloop() #GUI generator
