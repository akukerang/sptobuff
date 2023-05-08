from classes.skinport import Skinport
from classes.buff import Buff
from flask import Flask, render_template, request
import pandas as pd
import json

with open("config.json", "r") as f:
    config = json.load(f)

b = Buff(config["Cookies"])
spClass = Skinport()

app = Flask(__name__)
app.config['SECRET_KEY'] = "amogusVR" #this doesn't really matter, just need it to run

@app.route('/',methods=['GET','POST'])
def mainpage():
    skins = pd.read_csv('csv/skins.csv') #list for dropdown
    results = []    
    error = ""
    if request.method == 'POST':
        skin = str(request.form.get('skinName'))
        if(skin): #if input not empty run
            try:
                sp = spClass.getSkinportPrice(skin)
            except:
                sp = 0;
            try:
                buff = b.getBuffPrice(skin)
            except:
                buff = 0;
            afterFees = round((buff - (buff * 0.025)),2) #after fees Buff
            profit = round(afterFees - sp,2)
            gain = round((profit / sp) * 100,6)
            results = [skin, '$'+str(sp), '$'+str(buff), '$'+str(afterFees), '$'+str(profit), str(gain)+'%']
        else:
            error = "Please enter a value"
    return render_template('index.html',skinNames=skins.skinNames.values.tolist(), results = results, error = error)

if(config["Cookies"] == ""):
    print("enter cookie in config.json")
else:
    app.run()
