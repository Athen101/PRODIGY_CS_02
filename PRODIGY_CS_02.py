from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("300x300")

def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        print(file1)
        file_name=file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        file2=open(file_name,'wb')
        file2.write(image)
        file2.close()


b1=Button(root,text="encrypt", command=encrypt_image)
b1.place(x=70,y=10)

entry1=Text(root,height=3,width=25)
entry1.place(x=50,y=50)

root.mainloop()

