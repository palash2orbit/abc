from tkinter import *

main = Tk()
main.title("Patwari Form")
main.iconbitmap("1.ico")
main.configure(bg="#d482fa")
main.geometry("600x600")

class Calculate:   
    def __init__(self, ent, ent1):  
        self.ent = ent
        self.ent1 = ent1
    
    def add(self):
        result = float(self.ent) + float(self.ent1)
        return self.ent1.config(text=" result: {:.2f}".format(result))        

    def data_input(self):  
        lbl=Label(main,text="enter your num1",bg="black",fg="white",font=("arial",12))
        lbl.place(x=10,y=10)
        ent=Entry(main,bg="#32a852",font=("arial",10))
        ent.place(x=140,y=10)
        lbl=Label(main,text="enter your num1",bg="black",fg="white",font=("arial",12))
        lbl.place(x=10,y=60)
        ent1=Entry(main,bg="#32a852",font=("arial",10))
        ent1.place(x=140,y=60)
        btn = Button(main,text="Submit", bg="#62ccb3", font=("arial", 12), bd=3, command=self.add )
        btn.place(x=50, y=100)
        lbl1=Label(main,text="calculation result",bg="black",fg="white",font=("arial",12))
        lbl1.place(x=50,y=150)
    
obj = Calculate(5,7)
obj.data_input()
main.mainloop()