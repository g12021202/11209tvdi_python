from flask import Flask,url_for,render_template
import random
import pandas as pd
from auth import auth
from bs import bootstrap

app = Flask(__name__)
app.register_blueprint(auth.bp)
app.register_blueprint(bootstrap.bp)

@app.route('/')
def index():
    name = "gary"
    dataFrame = get_dataFrame()
    return render_template('index.html',name=name, dataFrame=dataFrame)

def get_dataFrame()->pd.DataFrame:
    df = [["gary",69,70,85],
          ["mark",72,68,84],
          ["tina",95,61,70]]
    
    return pd.DataFrame(df, columns=["姓名","國文分數","英文分數","數學分數"])