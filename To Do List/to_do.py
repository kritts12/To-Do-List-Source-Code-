from tkinter import *

entry_data ={}
def get_text():
    entry_data['entry1'] = entry1.get()
    entry_data['entry2'] = entry2.get()
    entry_data['entry3'] = entry3.get()
    entry_data['entry4'] = entry4.get()
    entry_data['entry5'] = entry5.get()
    print(entry_data)

root = Tk()

root.title("To Do List")
root.geometry("500x500")

check1 = Checkbutton(root, height=4, width = 4)
check1.grid(row = 0, column=0, padx=10, pady=5)

entry1 = Entry(root, width=40)
entry1.grid(row = 0, column=1, pady=5)

check2 = Checkbutton(root, height=4, width = 4)
check2.grid(row = 1, column=0, padx=10, pady=5)

entry2 = Entry(root, width=40)
entry2.grid(row = 1, column=1, pady=5)

check3 = Checkbutton(root, height=4, width = 4)
check3.grid(row = 2, column=0, padx=10, pady=5)

entry3 = Entry(root, width=40)
entry3.grid(row = 2, column=1, pady=5)

check4 = Checkbutton(root, height=4, width = 4)
check4.grid(row = 3, column=0, padx=10, pady=5)

entry4 = Entry(root, width=40)
entry4.grid(row = 3, column=1, pady=5)

check5 = Checkbutton(root, height=4, width = 4)
check5.grid(row = 4, column=0, padx=10, pady=5)

entry5 = Entry(root, width=40)
entry5.grid(row = 4, column=1, pady=5)


button = Button(root, text = "Save", command=get_text)
button.grid(row=5, column=0)

root.mainloop()