from tkinter import *
from PIL import Image , ImageTk

root=Tk()
root.title(" Rock Paper Scissor Game ")
root.configure(background="#9b59b6")

rock_img=ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor-user.png"))
rock_img_com=ImageTk.PhotoImage(Image.open("rock-user-com.png"))
paper_img_com=ImageTk.PhotoImage(Image.open("paper-user-com.png"))
scissor_img_com=ImageTk.PhotoImage(Image.open("scissor-user-com.png"))

user_label=Label(root,image=rock_img,bg="#9b59b6")
com_label=Label(root,image=rock_img_com,bg="#9b59b6")
user_label.grid(row=1,column=0)
com_label.grid(row=1,column=4)

playerscore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white").grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FF3E4D",fg="white").grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#FF3E4D",fg="white").grid(row=2,column=3)


root.mainloop()
