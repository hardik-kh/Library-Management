from tkinter import *
from PIL import ImageTk,Image
from addbooks import *
from viewbooks import *
from issuebooks import *
from returnbook import *
from deleteBook import *



def main():
    
    n=0.9
    root=Tk()
    root.resizable(0,0) 
    background_image =Image.open("bg.jpg")              ## Opened the image
    [imageSizeWidth, imageSizeHeight] = background_image.size  ## Putting width and length from original image

    newImageSizeWidth = int(imageSizeWidth*n)               ## multipy width by 0.9                  
    newImageSizeHeight = int(imageSizeHeight*n)             ## multiply height by 0.9

    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)
    Canvas1.create_image(540,310,image = img)           ## Centre of the image  
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="yellow",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Welcome To\nLook Inna Books", bg='black', fg='white', font=('Rockwell',20,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    def hideadd():
        #root.iconify()
        addBook()

    def hideview():
        #root.iconify()
        View()

    def hideissue():
        issue()

    def hidereturn():
        returnbook()

    def hidedelete():
        delete()
        

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white',font="Arial 12 bold",command= hideadd)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.08)            ## Button to add book details
        
    btn2 = Button(root,text="Delete Book",bg='black', fg='white',font="Arial 12 bold",command= hidedelete)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.08)            ## Button to delete book details
        
    btn3 = Button(root,text="View Book List",bg='black', fg='white',font="Arial 12 bold",command= hideview)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.08)            ## Button to View book details
        
    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white',font="Arial 12 bold",command= hideissue)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.08)            ## Button to Issue book 
        
    btn5 = Button(root,text="Return Book",bg='black', fg='white',font="Arial 12 bold",command= hidereturn)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.08)            ## Button to Return book
    root.geometry("1080x620")
    root.mainloop()


main()





    
