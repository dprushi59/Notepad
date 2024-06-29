import tkinter as tk
from tkinter import filedialog as fd

class Notepad(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Notepad")

        self.tx = tk.Text(self, wrap="word")
        self.tx.pack(side="top", fill="both", expand=True)

        self.mn = tk.Menu(self)
        self.config(menu=self.mn)

        mn = tk.Menu(self.mn)
        self.mn.add_cascade(label="File", menu=mn)
        mn.add_command(label="New", command=self.new_file)
        mn.add_command(label="Open", command=self.open_file)
        mn.add_command(label="Save", command=self.save_file)
        mn.add_separator()
        mn.add_command(label="Exit", command=self.quit)

        mn = tk.Menu(self.mn)
        self.mn.add_cascade(label="Edit", menu=mn)
        mn.add_command(label="Cut", command=self.cut)
        mn.add_command(label="Copy", command=self.copy)
        mn.add_command(label="Paste", command=self.paste)

    def new_file(self):
        self.tx.delete("1.0", "end")

    def open_file(self):
        file = fd.askopenfile(parent=self, mode="rb", title="Open a file")
        if file:
            contents = file.read()
            self.tx.delete("1.0", "end")
            self.tx.insert("1.0", contents)
            file.close()
            self.title(file.name + " - Notepad")

    def save_file(self):
        file = fd.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = self.tx.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name + " - Notepad")

    def cut(self):
        self.tx.event_generate("<<Cut>>")

    def copy(self):
        self.tx.event_generate("<<Copy>>")

    def paste(self):
        self.tx.event_generate("<<Paste>>")

notepad = Notepad()
notepad.mainloop()

