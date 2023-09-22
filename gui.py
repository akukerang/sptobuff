import tkinter as tk
from tkinter import Frame, Entry, Listbox
import csv
import json
from classes.skinport import skinport
from classes.buff import Buff

skin_names = []

with open("csv/skins.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        skin_names.append(row[0])
skin_names = skin_names[1:]

with open("config.json", "r") as f:
    config = json.load(f)

b = Buff(config["Cookies"])
s = skinport()



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

def displayError(text):
    submitButton.pack_forget()
    errorMessage.config(text=text)
    errorMessage.pack(pady=10)
    submitButton.pack(pady=30)

def Submit():
    try:
        selectedIndex = skinList.curselection()
        selectedItem = skinList.get(selectedIndex[0])
        print("Selected item: " + selectedItem)
        errorMessage.pack_forget()
        try:
            print('here0')
            sp = s.getSkinportPrice(selectedItem)
            print('here1')
            if isinstance(sp, str):
                displayError("No listing for that skin found on Skinport")
            print(f'{sp} SP')
            buff = b.getBuffPrice(selectedItem)
            print(f'{buff} buff')
            afterFees = round((buff - (buff * 0.025)),2) #after fees Buff
            profit = round(afterFees - sp,2)
            gain = round((profit / sp) * 100,6)
            results = [selectedItem, '$'+str(sp), '$'+str(buff), '$'+str(afterFees), '$'+str(profit), str(gain)+'%']
            updateResults(results)
            print(results)
        except:
            displayError("Please try another skin. Value not found")
                
    except:
        displayError("Please enter a skin")


def updateResults(results):
    pass



app = tk.Tk()
app.title("spToBuff")
app.resizable(False, False)


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

errorMessage = tk.Label(selectFrame, fg="red")

submitButton = tk.Button(selectFrame, text="Submit", command=Submit)
submitButton.pack(pady=30)








app.mainloop()
