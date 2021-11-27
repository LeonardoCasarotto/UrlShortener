import pyshorteners as ps
import tkinter as tk

main = tk.Tk()
title = tk.Label(main, text="Welcome, insert the link you want to shorten")
label1 = tk.Label(main, text="Insert here the link")
label2 = tk.Label(main, text="Shortened link")
entry1 = tk.Entry(main, width=35)
entry2 = tk.Entry(main, width=35, state="disabled")


def shortening():
    s = ps.Shortener()
    g = s.dagd.short(entry1.get())
    entry2.configure(state="normal")
    entry2.insert(0, g)
    entry2.configure(state="readonly")


btn = tk.Button(main, command=shortening, text="Shorten the link")
title.grid(row=0, column=1)
label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)
label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)
btn.grid(row=3, column=1)

main.mainloop()
