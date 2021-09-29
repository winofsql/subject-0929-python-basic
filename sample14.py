import tkinter as tk

def push() :
    print('クリックされた')

base = tk.Tk()
button1 = tk.Button(base, text="ボタン1", width=20, command=push).pack()

#button2 = tk.Button(base, text="ボタン2").pack(side=tk.LEFT)
#button3 = tk.Button(base, text="ボタン3").pack(side=tk.RIGHT)

base.mainloop()
