import tkinter as tk

class myapp:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("hello world")
        self.root.configure(background="black")
        self.root.bt1=tk.Button(root,anchor="center",background="black",command =self.hello,foreground="white",text="hello")
        self.root.bt1.pack(pady=10,padx=10)
    def hello(self):
        print("hello world....\n")


root= tk.Tk()
apps=myapp(root)
root.mainloop()