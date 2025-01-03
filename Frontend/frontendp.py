import sys
import os
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

# Add Backend folder to the Python module search path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Backend"))
sys.path.append(backend_path)

# Debug: Print the current Python path
print(f"Current Python path: {sys.path}")

# Import dbbackend from Backend folder
try:
    import dbbackend
except ModuleNotFoundError as e:
    messagebox.showerror("Error", f"Could not import dbbackend. Please ensure the file exists in the Backend folder.\nError: {e}")
    sys.exit(1)

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#2c3e50")

        # Custom Fonts
        self.title_font = tkFont.Font(family="Helvetica", size=28, weight="bold")
        self.label_font = tkFont.Font(family="Helvetica", size=14)
        self.button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

        # Variables
        self.StdID = StringVar()
        self.Firstname = StringVar()
        self.Surname = StringVar()
        self.DoB = StringVar()
        self.Age = StringVar()
        self.Gender = StringVar()
        self.Address = StringVar()
        self.Mobile = StringVar()

        # --------------------------------------FUNCTIONS-----------------------------------------------------------
        def iExit():
            confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
            if confirm:
                root.destroy()

        def clearData():
            for entry in [self.txtStdID, self.txtfna, self.txtSna, self.txtDoB, self.txtAge, self.txtGender, self.txtAdr, self.txtMobile]:
                entry.delete(0, END)

        def addData():
            if self.StdID.get():
                dbbackend.addStdRec(self.StdID.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (self.StdID.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()))
                messagebox.showinfo("Success", "Record Added Successfully")

        def DisplayData():
            studentlist.delete(0, END)
            for row in dbbackend.viewData():
                studentlist.insert(END, row)

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            for i, entry in enumerate([self.txtStdID, self.txtfna, self.txtSna, self.txtDoB, self.txtAge, self.txtGender, self.txtAdr, self.txtMobile]):
                entry.delete(0, END)
                entry.insert(END, sd[i + 1])

        def DeleteData():
            if self.StdID.get():
                dbbackend.deleteRec(sd[0])
                clearData()
                DisplayData()
                messagebox.showinfo("Success", "Record Deleted Successfully")

        def searchDatabase():
            studentlist.delete(0, END)
            for row in dbbackend.searchData(self.StdID.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()):
                studentlist.insert(END, row)

        def update():
            if self.StdID.get():
                dbbackend.deleteRec(sd[0])
                dbbackend.addStdRec(self.StdID.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (self.StdID.get(), self.Firstname.get(), self.Surname.get(), self.DoB.get(), self.Age.get(), self.Gender.get(), self.Address.get(), self.Mobile.get()))
                messagebox.showinfo("Success", "Record Updated Successfully")

        # --------------------------------------Frames---------------------------------------------------------------
        MainFrame = Frame(self.root, bg="#2c3e50")
        MainFrame.pack(fill=BOTH, expand=True)

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="#34495e", relief=RIDGE)
        TitFrame.pack(side=TOP, fill=X)
        self.lblTit = Label(TitFrame, font=self.title_font, text="Student Database Management System", bg="#34495e", fg="white")
        self.lblTit.pack()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg="#34495e", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM, fill=X)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="#2c3e50")
        DataFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="#34495e", font=self.label_font, text="Student Info", fg="white")
        DataFrameLEFT.pack(side=LEFT, fill=BOTH, expand=True)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="#34495e", font=self.label_font, text="Student Details", fg="white")
        DataFrameRIGHT.pack(side=RIGHT, fill=BOTH, expand=True)

        # --------------------------------------Entries-------------------------------------------------------------
        # Initialize Entry widgets as attributes of the class
        self.txtStdID = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.StdID, width=30)
        self.txtfna = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Firstname, width=30)
        self.txtSna = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Surname, width=30)
        self.txtDoB = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.DoB, width=30)
        self.txtAge = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Age, width=30)
        self.txtGender = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Gender, width=30)
        self.txtAdr = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Address, width=30)
        self.txtMobile = Entry(DataFrameLEFT, font=self.label_font, textvariable=self.Mobile, width=30)

        # Place the Entry widgets in the grid
        labels = ["Student ID:", "Firstname:", "Surname:", "Date of Birth:", "Age:", "Gender:", "Address:", "Mobile:"]
        entries = [self.txtStdID, self.txtfna, self.txtSna, self.txtDoB, self.txtAge, self.txtGender, self.txtAdr, self.txtMobile]

        for i, (label_text, entry) in enumerate(zip(labels, entries)):
            Label(DataFrameLEFT, font=self.label_font, text=label_text, bg="#34495e", fg="white").grid(row=i, column=0, sticky=W, padx=10, pady=10)
            entry.grid(row=i, column=1, padx=10, pady=10)

        # --------------------------------------Listbox and Scrollbar-----------------------------------------------
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.pack(side=RIGHT, fill=Y)

        studentlist = Listbox(DataFrameRIGHT, width=50, height=16, font=self.label_font, yscrollcommand=scrollbar.set, bg="#34495e", fg="white")
        studentlist.pack(fill=BOTH, expand=True)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        scrollbar.config(command=studentlist.yview)

        # --------------------------------------Buttons-------------------------------------------------------------
        buttons = [
            ("Add New", addData),
            ("Display", DisplayData),
            ("Clear", clearData),
            ("Delete", DeleteData),
            ("Search", searchDatabase),
            ("Update", update),
            ("Exit", iExit)
        ]
        for i, (text, command) in enumerate(buttons):
            Button(ButtonFrame, text=text, font=self.button_font, height=1, width=10, bd=4, bg="#3498db", fg="white", command=command).grid(row=0, column=i, padx=5, pady=5)

if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()