from tkinter import*

window= Tk()


label=Label(window,text="hello rahul",
                                    font=("Arial",20,"bold"),	
                                    fg="#00ff00",	
                                    bg="black",	
                                    relief=RAISED,	
                                    bd=20,	
                                    padx=10,	
                                    pady=10)
label.place(x=1000,y=500)




window.mainloop()