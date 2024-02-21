import requests
import random
import tkinter as tk
class quotes:
    def screen(self):
        self.win=tk.Tk()
        self.win.geometry("600x400")
        self.win.resizable(0,0)
        self.win.configure(bg="#C8A2C8")
        self.req=requests.get("https://api.quotable.io/random")
        self.data=self.req.json()
        self.text=tk.Text(self.win,bg="#C8A2C8",fg="#add8e6",borderwidth=0,font=("Elephant",17))
        self.author=tk.Label(self.win,bg="#C8A2C8",text=self.data['author'],fg="#add8e6",font=("sans-serif",14))
        if len(self.data['content'])<200:
            self.author.place(x=400,y=150,height=40,width=200)
        else:
            self.author.place(x=400,y=235,height=40,width=200)
        self.text.place(x=20,y=30,height=200,width=560)
        self.b1=tk.Button(self.win,bg="#add8e6",command=self.change,text="Change quote")
        self.b1.place(x=250,y=300,width=100,height=50)
        if len(self.data['content'])<150:
            self.text.insert(1.0,self.data['content'])
        else:
            self.change()
        print(len(self.data['content']))
        self.win.mainloop()
    def change(self):
        self.req=requests.get("https://api.quotable.io/random")
        self.data=self.req.json()
        self.text.delete(1.0,tk.END)
        self.text.insert(1.0,self.data['content'])
        self.author.config(text=self.data['author'])
        print(len(self.data['content']))

q1=quotes()
q1.screen()


