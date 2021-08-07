from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as cn

def View(): 
    
    n=0.9
    root1=Toplevel()
    root1.resizable(0,0)
    background_image1 =Image.open("bg1.jpg")              ## Opened the image
    [imageSizeWidth, imageSizeHeight] = background_image1.size  ## Putting width and length from original image

    newImageSizeWidth = int(imageSizeWidth*n)               ## multipy width by 0.9                  
    newImageSizeHeight = int(imageSizeHeight*n)             ## multiply height by 0.9

    background_image1 = background_image1.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(background_image1)

    Canvas2= Canvas(root1)
    Canvas2.create_image(540,310,image = img2)           ## Centre of the image  
    Canvas2.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas2.pack(expand=True,fill=BOTH)

    db=cn.connect(host="localhost",user="root",passwd="hardik123",database="hardik")  ## Connecting to MySQL
    cr=db.cursor()
    cr.execute("select id,title,author,status from final")

    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Rockwell',20,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    scrollbar = Scrollbar(root1,command=Canvas2.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
  


    headingFrame2 = Frame(root1,bg="deep sky blue",bd=5)
    headingFrame2.place(relx=0.143,rely=0.3,relwidth=0.714,relheight=0.513)

    mylist = Listbox(headingFrame2,bg='tan4',fg="gold",font="Arial 18 bold" )
    mylist.place(relx=0.005,rely=0.01,relwidth=0.99,relheight=0.15)
    mylist.insert(END," "*6+"%-25s%-35s%-20s%-20s"%('ID','Title','Author','Status'))

    
    def scroll(x, y):
        textbox1.yview(x,y)
        textbox2.yview(x,y)
        textbox3.yview(x,y)
        textbox4.yview(x,y)

    scrollbar.config( command = scroll )
    

    textbox1 = Text(root1,bg="hot pink",fg="white", yscrollcommand = scrollbar.set)
    textbox1.config(font = ('Consolas',16,'bold'))
    
    textbox1.place(relx=0.15,rely=0.4,relwidth=0.1,relheight=0.4)

    textbox2 = Text(root1,bg="hot pink",fg="white", yscrollcommand = scrollbar.set)
    textbox2.config(font = ('Consolas',16,'bold'))
    textbox2.place(relx=0.25,rely=0.4,relwidth=0.25,relheight=0.4)

    textbox3 = Text(root1,bg="hot pink",fg="white", yscrollcommand = scrollbar.set)
    textbox3.config(font = ('Consolas',16,'bold'))
    textbox3.place(relx=0.5,rely=0.4,relwidth=0.25,relheight=0.4)

    textbox4 = Text(root1,bg="hot pink",fg="white", yscrollcommand = scrollbar.set)
    textbox4.config(font = ('Consolas',16,'bold'))
    textbox4.place(relx=0.75,rely=0.4,relwidth=0.1,relheight=0.4)

    for i in cr:
        if(len(str(i[0]))==1):    
            textbox1.insert(INSERT, " "*(2-len(str(i[0]))//2)+"000%s"%(str(i[0]))+"\n")
        elif(len(str(i[0]))==2):    
            textbox1.insert(INSERT, " "*(2-len(str(i[0]))//2)+"00%s"%(str(i[0]))+"\n")
        elif(len(str(i[0]))==3):    
            textbox1.insert(INSERT, " "*(2-len(str(i[0]))//2)+"0%s"%(str(i[0]))+"\n")
        else:
            textbox1.insert(INSERT, " "*(2-len(str(i[0]))//2)+"%s"%(str(i[0]))+"\n")
        textbox2.insert(INSERT, " "*(11-len(i[1])//2)+"%s"%(i[1])+"\n")
        textbox3.insert(INSERT, " "*(11-len(i[2])//2)+"%s"%(i[2])+"\n")
        textbox4.insert(INSERT, " "*(4-len(i[3])//2)+"%s"%(i[3])+"\n")

    textbox1.config(state= DISABLED)
    textbox2.config(state= DISABLED)
    textbox3.config(state= DISABLED)
    textbox4.config(state= DISABLED)
    
    quitBtn = Button(root1,text="Quit",bg='white', fg='black',font=('Arial',12,'bold'), command=root1.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    root1.geometry("1080x620")
    root1.mainloop()
