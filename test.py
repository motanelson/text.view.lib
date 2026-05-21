from tkinter import filedialog
import txtview




f1=filedialog.askopenfile(mode="r",defaultextension="*.*",title="open file")
a=f1.read()
txtview.views(tittle="text view",text=a)

