2023.10.18作業
建立一個台積電的資料庫#在資料庫內建立資料表
將台積電.csv整理為json格式
把json格式的資料進入資料表

[data.py](./data.py)
```
import yfinance as yf
import csv
import json

data = yf.download("2330.TW", start = '2023-01-01')
data.to_csv('tsmc.csv')

def make_json(csvFilePath, jsonFilePath):
    data_dict = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
             
            # Add this python dict to json array
            key = rows['Date']
            data_dict[key] = rows
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data_dict, indent=4))

csvFilePath = r'tsmc.csv'
jsonFilePath = r'tsmc.json'
 
make_json(csvFilePath, jsonFilePath)
```

[main.py](./main.py)
```
import sqlite3
import json

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 台積電 (
            "id"    INTEGER NOT NULL,
            "日期"	INTEGER NOT NULL,
            "開市"	INTEGER NOT NULL,
            "最高"	INTEGER NOT NULL,
            "最低"	INTEGER NOT NULL,
            "收市"	INTEGER NOT NULL,
            "經調整收市價"	INTEGER NOT NULL,
            "成交量"	INTEGER,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
        '''
    )
    conn.commit()
def insert_data(conn,values):
    cursor = conn.cursor()
    sql = '''
        INSERT INTO 台積電 (日期, 開市, 最高, 最低, 收市, 經調整收市價, 成交量)
        VALUES(?,?,?,?,?,?,?)
        '''
    cursor.execute(sql, values)
    conn.commit()

conn = sqlite3.connect("stock.db")
create_table(conn)
conn.commit()

with open("tsmc.json",mode="r") as file:
    data = json.load(file)
    for item in data:
        # print(type(item))
        insert_data(conn,(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
        # insert_data(conn,(item['Date'], item['Open'], item['High'], item['Low'], item['Close'], item['Adj Close'], item['Volume']))
```