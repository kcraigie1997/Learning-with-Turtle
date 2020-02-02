import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
import sys
import importlib

sys.path.append("Code")

title_font = ("Times", 24, "bold")

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (StartPage, TutorialSelect, Lesson1, Lesson2, Lesson3, Lesson4, Lesson5, Lesson6, Lesson7, Lesson8, Lesson9, Lesson10):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg = '#c7eaaf')
        self.grid()
        
        label = tk.Label(self, text = "Learning with turtle", font = title_font, bg = '#c7eaaf')
        label.grid(column = 1, row = 0)

        begin = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(TutorialSelect), width = 50)
        begin.grid(column = 1, row = 1)

        quit_frame = tk.Frame(self, parent, bg = '#c7eaaf')
        
        exit = ttk.Button(quit_frame, text = "Quit",
                            command = quit)
        exit.pack(side = "right")
    
        quit_frame.grid(column = 2, row = 2)
        
        self.grid_rowconfigure(1, minsize = 600)
        self.grid_rowconfigure(2, minsize = 180)
        
        self.grid_columnconfigure(1, minsize = 1720)


class TutorialSelect(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = '#c7eaaf')
        label = tk.Label(self, text = "Select lesson", font = title_font, bg = '#c7eaaf')
        label.pack(pady = 10,padx = 10)

        lesson1 = ttk.Button(self, text="Lesson 1",
                            command=lambda: controller.show_frame(Lesson1), width = 50)
        lesson1.pack(pady = 10)

        lesson2 = ttk.Button(self, text="Lesson 2",
                            command=lambda: controller.show_frame(Lesson2), width = 50)
        lesson2.pack(pady  = 10)
        
        lesson3 = ttk.Button(self, text="Lesson 3",
                            command=lambda: controller.show_frame(Lesson3), width = 50)
        lesson3.pack(pady = 10)

        lesson4 = ttk.Button(self, text="Lesson 4",
                            command=lambda: controller.show_frame(Lesson4), width = 50)
        lesson4.pack(pady = 10)

        lesson5 = ttk.Button(self, text="Lesson 5",
                            command=lambda: controller.show_frame(Lesson5), width = 50)
        lesson5.pack(pady = 10)

        lesson6 = ttk.Button(self, text="Lesson 6",
                            command=lambda: controller.show_frame(Lesson6), width = 50)
        lesson6.pack(pady = 10)

        lesson7 = ttk.Button(self, text="Lesson 7",
                            command=lambda: controller.show_frame(Lesson7), width = 50)
        lesson7.pack(pady = 10)

        lesson8 = ttk.Button(self, text="Lesson 8",
                            command=lambda: controller.show_frame(Lesson8), width = 50)
        lesson8.pack(pady = 10)

        lesson9 = ttk.Button(self, text="Lesson 9",
                            command=lambda: controller.show_frame(Lesson9), width = 50)
        lesson9.pack(pady = 10)

        lesson10 = ttk.Button(self, text="Lesson 10",
                            command = lambda: controller.show_frame(Lesson10), width = 50)
        lesson10.pack(pady = 10)
        
        quit_button = ttk.Button(self, text="Quit",
                            command = quit, width = 30)
        quit_button.pack(pady = 10)


class Lesson1(ttk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.grid()
        
        file = open("Lessons/lesson_1.txt", "r")

        label = tk.Label(self, text = "Lesson 1", font = title_font)
        label.grid(column = 1, row = 0)
        
        output = tk.Canvas(self, bg = "white", width = 500, height = 389)
        output.grid(column = 0, row = 1)

        inp = tk.Text(self)
        inp.grid(column = 1, row = 1)

        if os.path.exists("Code/lesson_1.py"):
            code = open("Code/lesson_1.py")
            inp.insert("insert", code.read())
        else:
            inp.insert("insert", "code here...")
        
        text = tk.Text(self)
        text.grid(column = 2, row = 1)
        text.insert("insert", file.read())
        
        button_frame = ttk.Frame(self)
        
        
        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")
        
        button_frame.grid(column = 1, row = 2)

        


    def save_code(self, code):
        file = open("Code/lesson_1.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
        import lesson_1
        importlib.reload(lesson_1)
        res.delete("all")
        lesson_1.test(res)
        

class Lesson2(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 2", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_2.py"):
            code = open("Code/lesson_2.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_2.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_2
       importlib.reload(lesson_2)
       res.delete("all")
       lesson_2.test(res)

class Lesson3(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 3", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_3.py"):
            code = open("Code/lesson_3.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_3.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_3
       importlib.reload(lesson_3)
       res.delete("all")
       lesson_3.test(res)

class Lesson4(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 4", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_4.py"):
            code = open("Code/lesson_4.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_4.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_4
       importlib.reload(lesson_4)
       res.delete("all")
       lesson_4.test(res)

class Lesson5(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 5", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_5.py"):
            code = open("Code/lesson_5.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_5.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_5
       importlib.reload(lesson_5)
       res.delete("all")
       lesson_5.test(res)

class Lesson6(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 6", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_6.py"):
            code = open("Code/lesson_6.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_6.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_6
       importlib.reload(lesson_6)
       res.delete("all")
       lesson_6.test(res)

class Lesson7(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 7", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_7.py"):
            code = open("Code/lesson_7.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_7.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_7
       importlib.reload(lesson_7)
       res.delete("all")
       lesson_7.test(res)

class Lesson8(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 8", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_8.py"):
            code = open("Code/lesson_8.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_8.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_8
       importlib.reload(lesson_8)
       res.delete("all")
       lesson_8.test(res)

class Lesson9(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 9", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_9.py"):
            code = open("Code/lesson_9.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_9.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_9
       importlib.reload(lesson_9)
       res.delete("all")
       lesson_9.test(res)

class Lesson10(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        file = open("Lessons/test.txt", "r")

        label = tk.Label(self, text = "Lesson 10", font = title_font)
        label.pack(pady=10,padx=10)

        output = tk.Canvas(self, height = 300, width = 300 , bg = "white")
        output.place(anchor = "n" , x = 150, y = 61)

        input = tk.Text(self, width = "100", height = "35")
        input.pack()

        if os.path.exists("Code/lesson_10.py"):
            code = open("Code/lesson_10.py")
            input.insert("insert", code.read())
        else:
            input.insert("insert", "code here...")
        
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)

        save = ttk.Button(button_frame, text = "Save code", command = lambda: self.save_code(input.get(1.0, "end")))
        save.pack(anchor = "n" ,side = "left")

        run = ttk.Button(button_frame, text = "GO!", command = lambda: self.run_code(output))
        run.pack(anchor = "n" ,side = "left")

        done = ttk.Button(button_frame, text = "Finished",
                            command = lambda: controller.show_frame(TutorialSelect))
        done.pack(anchor = "n" ,side = "right")

        text = ttk.Label(self, text = file.read())
        text.place(anchor = "n", x = 1220, y = 61)

    def save_code(self, code):
        file = open("Code/lesson_10.py", "w")
        file.write(code)
        file.close()
        messagebox.showinfo("Saved", "Code saved!")

    def run_code(self, res):
       import lesson_10
       importlib.reload(lesson_10)
       res.delete("all")
       lesson_10.test(res)


app = App()
app.resizable(width=False, height=False)
app.geometry('{}x{}'.format(1800, 750))
app.title("Learning with turtle")

app.mainloop()