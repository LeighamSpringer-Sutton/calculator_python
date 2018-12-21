from tkinter import Tk, Label, Button,Entry
from tkinter import ttk
from ttkthemes import ThemedTk


from PIL import Image, ImageTk



class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.col =0
        self.row =3
        self.to_calculate =[]
        self.funcs = [self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine,self.zero]
        self.symfuncs = [self.add,self.subtract,self.multiply,self.divide,self.compute,self.deci,self.clear,self.sign]
        self.symnames = ["+","-","*","/","=",".","clear","+/-"]
        self.operations = ["p", "d", "s", "m"]
        self.output = Label(self.master,relief = "sunken",height =1,width =50)
        self.create_calcnums()
        self.create_symbuttons()
        self.output.grid(row=0,column = 0,columnspan = 10)
        self.computed = 0

    def create_symbuttons(self):
        self.row = 3
        self.col = 4
        for symname, func in zip(self.symnames, self.symfuncs):
            if symname == "clear":
                self.button = ttk.Button(self.master, text=symname, command=func, width=10)
                self.button.grid(row=7, column=1)
            else:

                self.button = ttk.Button(self.master, text=symname, command=func, width=10)
                self.button.grid(row=self.row, column=self.col)
                self.row += 1
                if self.row % 6 == 0:
                    self.row=3
                    self.col+=1


    def create_calcnums(self):
        for num, func in zip(range(1, 11), self.funcs):
            if num == 10:
                self.button = ttk.Button(self.master, text="0", width=10, command=func)
                self.button.grid(row=7, column=0)
            else:
                self.button = ttk.Button(self.master, text=str(num), command=func, width=10)
                self.button.grid(row=self.row, column=self.col)
                self.col += 1
                if num % 3 == 0 and num != 0: self.row, self.col = self.row + 1, 0

    def one(self):
        if self.computed: self.output["text"], self.to_calculate = "", []

        self.computed = 0
        self.to_calculate.append("1")
        self.output["text"] += "1"

    def two(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("2")
        self.output["text"] += "2"

    def three(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("3")
        self.output["text"] += "3"

    def four(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("4")
        self.output["text"] += "4"

    def five(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("5")
        self.output["text"] += "5"

    def six(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("6")
        self.output["text"] += "6"

    def seven(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("7")
        self.output["text"] += "7"

    def eight(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("8")
        self.output["text"] += "8"

    def nine(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("9")
        self.output["text"] += "9"

    def zero(self):
        if self.computed: self.output["text"], self.to_calculate = "", []
        self.computed = 0
        self.to_calculate.append("0")
        self.output["text"] += "0"

    "Symbol functions"

    def add(self):
        if "p" in self.to_calculate:
            self.to_calculate.remove("p")
            self.output["text"] = self.output["text"].replace("+", "")

        alreadysym = [i for i in self.to_calculate if i in self.operations ]
        if alreadysym:
            return 0
        self.computed = 0
        self.to_calculate.append(str("p"))
        self.output["text"] += "+"

    def subtract(self):
        if "s" in self.to_calculate:
            self.to_calculate.remove("s")
            self.output["text"] = self.output["text"].replace("-", "")
        alreadysym = [i for i in self.to_calculate if i in self.operations ]
        if alreadysym:
            return 0
        self.computed = 0
        self.to_calculate.append(str("s"))
        self.output["text"] += "-"

    def divide(self):
        if "d" in self.to_calculate:
            self.to_calculate.remove("d")
            self.output["text"] = self.output["text"].replace("/", "")
        alreadysym = [i for i in self.to_calculate if i in self.operations ]
        if alreadysym:
            return 0
        self.computed = 0
        self.to_calculate.append(str("d"))
        self.output["text"] += "/"

    def multiply(self):
        if "m" in self.to_calculate:
            self.to_calculate.remove("m")
            self.output["text"] = self.output["text"].replace("*", "")
        alreadysym = [i for i in self.to_calculate if i in self.operations ]
        if alreadysym:
            return 0
        self.computed = 0
        self.to_calculate.append(str("m"))
        self.output["text"] += "*"

    def deci(self):
        if "." in self.to_calculate:
            self.to_calculate.remove(".")
            self.output["text"] = self.output["text"].replace(".", "")
        alreadysym = [i for i in self.to_calculate if i in self.operations ]
        if alreadysym:
            return 0
        self.computed = 0
        self.to_calculate.append(str("."))
        self.output["text"] += "."

    def clear(self):
        self.computed = 0
        self.output["text"] = ""
        self.to_calculate = []
    def sign(self):
        if '-' not in self.output["text"] :
            self.to_calculate.insert(0,'-')

            self.output["text"] = '-' + self.output["text"]
        elif '-' in  self.output["text"] :
            self.to_calculate.remove('-')
            self.output["text"] = self.output["text"].replace('-','')





    def compute(self):
        self.computed = 0
        self.to_calculate = "".join(self.to_calculate)
        splitter = [self.to_calculate.index(i) for i in self.to_calculate if i in self.operations][0]

        if self.to_calculate[splitter] == "p":
            total = str(sum([float(i) for i in self.to_calculate.split(self.to_calculate[splitter])]))

        elif self.to_calculate[splitter] == "s":
            self.to_calculate = [float(i) for i in self.to_calculate.split(self.to_calculate[splitter])]
            total = str(self.to_calculate[0] - self.to_calculate[1])
        elif self.to_calculate[splitter] == "m":
            self.to_calculate = [float(i) for i in self.to_calculate.split(self.to_calculate[splitter])]
            total = str(self.to_calculate[0] * self.to_calculate[1])
        elif self.to_calculate[splitter] == "d":
            self.to_calculate = [float(i) for i in self.to_calculate.split(self.to_calculate[splitter])]
            try:
                total = str(self.to_calculate[0] / self.to_calculate[1])
            except ZeroDivisionError:
                print("Can't divide by zero")
                total = '0'
        self.output["text"] = total
        self.computed = 1

        self.to_calculate = [total]




def main():
    root = ThemedTk()
    pixmap_themes = [
        "arc",
        "blue",
        "clearlooks",
        "elegance",
        "kroc",
        "plastik",
        "radiance",
        "winxpblue"
    ]

    root.set_theme(pixmap_themes[6])

    my_gui = MyFirstGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()

