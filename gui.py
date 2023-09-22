import tkinter as tk
from tkinter import ttk, Frame, Entry, Listbox
import csv

skin_names = []

with open("csv/skins.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        skin_names.append(row[0])
skin_names = skin_names[1:]
def checkKey(event):
    value = event.widget.get()
    if value == '':
        data = skin_names
        skinList.pack_forget()
    else:
        submitButton.pack_forget()
        skinList.pack()
        submitButton.pack(pady=30)
        data = []
        for item in skin_names:
            if value.lower() in item.lower():
                data.append(item)                
    update(data)
   
   
def update(data):
    skinList.delete(0, 'end')
    for item in data:
        skinList.insert('end', item)


def Submit():
    try:
        selectedIndex = skinList.curselection()
        selectedItem = skinList.get(selectedIndex[0])
        print("Selected item: " + selectedItem)
        errorMessage.pack_forget()
    except:
        submitButton.pack_forget()
        errorMessage.pack(pady=10)
        submitButton.pack(pady=30)

app = tk.Tk()
app.title("spToBuff")

selectFrame = Frame(app, width=300, height=400, bg="lightgray")
selectFrame.pack(side="left", fill="both", expand=True)

resultFrame = Frame(app, width=600, height=400)
resultFrame.pack(side="right", fill="both", expand=True)

label = tk.Label(selectFrame, text="Select a skin:")
label.pack(pady=10)

skinEntry = Entry(selectFrame, width=50)
skinEntry.bind("<KeyRelease>", checkKey)
skinEntry.pack()


skinList = Listbox(selectFrame, width=50)
update(skin_names)

errorMessage = tk.Label(selectFrame, text="Please select a skin.", fg="red")

submitButton = tk.Button(selectFrame, text="Submit", command=Submit)
submitButton.pack(pady=30)

app.resizable(False, False)

app.mainloop()
