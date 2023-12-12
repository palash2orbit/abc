import tkinter as tk

main = tk.Tk()
main.title("Patwari Form")
main.iconbitmap("1.ico")
main.configure(bg="#d482fa")

main.geometry("600x600")

def add(num1,num2):
    result=num1+num2
    return result
# num1=int(input("enter your number"))
# num2=int(input("enter your number"))
# calu=add(num1,num2)
# print(calu)
# num1=float(num1.get())
# num2=float(num2.get())
# result_label=num1+num2
# result_label.config(text=result_label)

lbl=tk.Label(main,text="enter your num1",bg="black",fg="white",font=("arial",12))
lbl.place(x=10,y=10)
ent=tk.Entry(main,bg="#32a852",font=("arial",10))
ent.place(x=120,y=100)


# lbl=tk.Label(main,text="Condidate Name", bg="black", fg="white", font=("arial" ,10))
# lbl.place(x=10,y=10)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=10)

# lbl=tk.Label(main,text="Last Name", bg="black", fg="white", font=("arial" , 10))
# lbl.place(x=10,y=50)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=50)

# lbl=tk.Label(main,text="Candidate age",bg="black" ,fg="white",font=("arial",10))
# lbl.place(x=10,y=100)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=100)

# lbl=tk.Label(main,text="Father Name",bg="black",fg="white",font=("arial",10))
# lbl.place(x=10,y=150)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=150)

# lbl=tk.Label(main,text="Last Name",bg="black",fg="white",font=("arial",10))
# lbl.place(x=10,y=200)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=200)

# lbl=tk.Label(main,text="mother Name",bg="black",fg="white",font=("arial",10))
# lbl.place(x=10,y=250)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=250)

# lbl=tk.Label(main,text="Last Name",bg="black",fg="white",font=("arial",10))
# lbl.place(x=10,y=300)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=120,y=300)

# lbl=tk.Label(main,text="Higher Qualification",bg="black",fg="white",font=("arial",10))
# lbl.place(x=400,y=10)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=530,y=10)

# lbl=tk.Label(main,text="Passing Year",bg="black",fg="white",font=("arial",10))
# lbl.place(x=400,y=50)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=530,y=50)

# lbl=tk.Label(main,text="Passing Year",bg="black",fg="white",font=("arial",10))
# lbl.place(x=400,y=100)
# ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
# ent.place(x=530,y=100)

lbl=tk.Label(main,text="Passing Year",bg="black",fg="white",font=("arial",10))
lbl.place(x=400,y=150)
ent=tk.Entry(main,bg="#d8ecf2",font=("arial",10))
ent.place(x=530,y=150)

main.mainloop()

