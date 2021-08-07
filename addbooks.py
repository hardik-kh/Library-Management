from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as cn
from tkinter import messagebox

def register():
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = CheckVar1.get()
    if(status==0):
        status="Avail"
        issued = "Nobody"
    else:
        status="Issued"
        issued = (bookInfo1.get())
    #status = status.lower()
    insertBooks = "insert into "+bookTable+"(title,author,status,issuedto) values ('"+title+"','"+author+"','"+status+"','"+issued+"')"
    try:
        cr.execute(insertBooks)
        db.commit()
        messagebox.showinfo('Success',"Book added successfully")
        bookInfo1.delete(0, END)
        bookInfo2.delete(0, END)
        bookInfo3.delete(0, END)
    except:
        messagebox.showinfo("Error","Can't add data into Database")
        bookInfo1.delete(0, END)
        bookInfo2.delete(0, END)
        bookInfo3.delete(0, END)
           
   
def addBook():
    global bookInfo1 ,bookInfo2, bookInfo3,cr,db,bookTable,C1,C2,CheckVar1,lb1

    db=cn.connect(host="localhost",user="root",passwd="hardik123",database="hardik")
    cr=db.cursor()
    bookTable = "final"
    
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

        
    headingFrame1 = Frame(root1,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier',22,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    labelFrame = Frame(root1,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
        
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white', font=('Arial',12,'bold'))
    lb2.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame,font='Arial')
    bookInfo2.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.1)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='black', fg='white', font=('Arial',12,'bold'))
    lb3.place(relx=0.05,rely=0.350, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame,font='Arial')
    bookInfo3.place(relx=0.3,rely=0.350, relwidth=0.62, relheight=0.1)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status(Avail/Issued) : ", bg='black', fg='white', font=('Arial',12,'bold'))
    lb4.place(relx=0.05,rely=0.5, relheight=0.08)

    lb1 = Label(labelFrame,text="Issued To : ", bg='black', fg='white', font=('Arial',12,'bold'))
    bookInfo1 = Entry(labelFrame,font='Arial')

    def avail():
        lb1.destroy()
        bookInfo1.destroy()

    def issuedto():
    # Issued to
        global lb1,bookInfo1
        lb1 = Label(labelFrame,text="Issued To : ", bg='black', fg='white', font=('Arial',12,'bold'))
        lb1.place(relx=0.05,rely=0.65, relheight=0.08)
            
        bookInfo1 = Entry(labelFrame,font='Arial')
        bookInfo1.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.1)
        

    # Check Boxes
    CheckVar1 = IntVar()
    cb=[]
    cb.append(Checkbutton(labelFrame, onvalue = 0,offvalue = 0, variable = CheckVar1, width=15, text = "Avail", font=('Arial',12,'bold'),fg='deep sky blue',command=avail))
    cb[0].place(relx=0.35,rely=0.5, relheight=0.1)

    cb.append(Checkbutton(labelFrame, onvalue = 1,offvalue = 0, variable = CheckVar1, width=15, text = "Issued", font=('Arial',12,'bold'),fg='deep sky blue',command=issuedto))
    cb[1].place(relx=0.65,rely=0.5, relheight=0.1)


        
        
    #Submit Button
    SubmitBtn = Button(root1,text="SUBMIT",bg='white', fg='black', font=('Rockwell',12,'bold'),command=register)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root1,text="Quit",bg='white', fg='black', font=('Rockwell',12,'bold'),command=root1.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root1.geometry("1080x620")
    root1.mainloop()
    

