import tkinter as tk

main = tk.Tk()
main.title("Patwari Form")
main.iconbitmap("1.ico")
main.configure(bg="#d482fa")

main.geometry("600x600")

def add():
    result=float(ent.get())+float(ent1.get())
    return lbl1.config(text="calculation result{:.2f}".format(result))

lbl=tk.Label(main,text="enter your num1",bg="black",fg="white",font=("arial",12))
lbl.place(x=10,y=10)
ent=tk.Entry(main,bg="#32a852",font=("arial",10))
ent.place(x=140,y=10)

lbl=tk.Label(main,text="enter your num1",bg="black",fg="white",font=("arial",12))
lbl.place(x=10,y=60)
ent1=tk.Entry(main,bg="#32a852",font=("arial",10))
ent1.place(x=140,y=60)

btn = tk.Button(main,text="Submit", bg="#62ccb3", font=("arial", 12), bd=3, command=add )
btn.place(x=50, y=100)

lbl1=tk.Label(main,text="calculation result",bg="black",fg="white",font=("arial",12))
lbl1.place(x=50,y=150)

main.mainloop()

