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
        errorMessage.pack_forget()
        try:
            sp = s.getSkinportPrice(selectedItem)
            buff = b.getBuffPrice(selectedItem)
            print(buff)
            afterFees = round((buff - (buff * 0.025)),2) #after fees Buff
            profit = round(afterFees - sp,2)
            gain = round((profit / sp) * 100,6)
            results = [selectedItem, '$'+str(sp), '$'+str(buff), '$'+str(afterFees), '$'+str(profit), str(gain)+'%']
            updateResults(results)
        except:
            displayError("Please try another skin. Value not found")
    except:
        displayError("Please enter a skin")


def updateResults(results):
    skinName.config(text=results[0])
    spPrice.config(text=f"Skinport: {results[1]}")
    buffPrice.config(text=f"Buff: {results[2]}")
    afterFees.config(text=f"After Fees: {results[3]}")
    profit.config(text=f"Profit: {results[4]}")
    gain.config(text=f"Gain: {results[5]}")
    skinName.pack()
    spPrice.pack()
    buffPrice.pack()
    afterFees.pack()
    profit.pack()
    gain.pack()



app = tk.Tk()
app.title("spToBuff")
app.resizable(False, False)
app.geometry("800x400")
app.configure(bg="lightgray")
selectFrame = Frame(app, width=400, height=400, bg="lightgray")
selectFrame.pack(side="left", fill="both", expand=True,pady=30)

resultFrame = Frame(app, width=400, height=400,  bg="lightgray")
resultFrame.pack(side="right", fill="both", expand=True, pady=30, padx=30)

label = tk.Label(selectFrame, text="Select a skin:", font=("Arial", 12))
label.pack(pady=10)

skinEntry = Entry(selectFrame, width=50)
skinEntry.bind("<KeyRelease>", checkKey)
skinEntry.pack(padx = 10)

skinList = Listbox(selectFrame, width=50)
update(skin_names)

errorMessage = tk.Label(selectFrame, fg="red")

submitButton = tk.Button(selectFrame, text="Submit", font=("Arial", 12), command=Submit)
submitButton.pack(pady=30)


skinName = tk.Label(resultFrame, font=("Arial", 12))
spPrice = tk.Label(resultFrame, font=("Arial", 12))
buffPrice = tk.Label(resultFrame, font=("Arial", 12))
afterFees = tk.Label(resultFrame, font=("Arial", 12))
profit = tk.Label(resultFrame, font=("Arial", 12))
gain = tk.Label(resultFrame, font=("Arial", 12))

app.mainloop()
