import tkinter as tk

win = tk.Tk()
win.title("Master")
win.iconbitmap("1.ico")
win.configure(bg="#03a1fc")

win.geometry("600x600")

lbl = tk.Label(win, text="Student name", bg="green", fg="white", font=("arial", 12))
lbl.place(x=10, y=10)

ent = tk.Entry(win, bg="#fc9803", font=("arial", 12))
ent.place(x=150, y=10)

lbl = tk.Label(win, text="Student age", bg="green", fg="white", font=("arial", 12))
lbl.place(x=10, y=40)

ent = tk.Entry(win, bg="#fc9803", font=("arial", 12))
ent.place(x=150, y=40)

lbl = tk.Label(win, text="Father name", bg="green", fg="white", font=("arial", 12))
lbl.place(x=10, y=80)

ent = tk.Entry(win, bg="#fc9803", font=("arial", 12))
ent.place(x=150, y=80)

btn = tk.Button(win,text="Submit", bg="#62ccb3", font=("arial", 12), bd=10 )
btn.place(x=50, y=120)

win.mainloop()