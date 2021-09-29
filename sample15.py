import tkinter as tk
import tkinter.messagebox as msg

base = tk.Tk()
base.withdraw()

# OK / キャンセル
res = msg.askokcancel('大変!!!', '大丈夫ですか？')

# はい/いいえ
res = msg.askquestion('大変!!!', '大丈夫ですか？')

# はい/いいえ
res = msg.askyesno('大変!!!', '大丈夫ですか？')

# 再試行/キャンセル
res = msg.askretrycancel('大変!!!', '大丈夫ですか？')

# はい/いいえ/キャンセル
res = msg.askyesnocancel('大変!!!', '大丈夫ですか？')

if(res == True):
    print('大丈夫です')
else :
    print('大丈夫ではない')

base.mainloop()
