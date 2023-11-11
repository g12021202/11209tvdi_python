將下載資料與建置資料庫放置在  datasource.py <br>
執行介面與呼叫 datasource.py 放在 app.py <br>
datasource.py
```
import requests
import psycopg2
import password as pw
import datetime

def __download_air_data()->list[dict]:
    '''
    下載 
    https://data.moenv.gov.tw/swagger/#/%E5%A4%A7%E6%B0%A3/get_aqx_p_07
    Curl 
    curl -X GET "https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=cbb6f9c0-9c3b-4086-b464-80594cd61f78" -H "accept: */*"
    '''
    air_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=cbb6f9c0-9c3b-4086-b464-80594cd61f78'
    response = requests.get(air_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

def __create_table(conn):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 空氣品質監測站基本資料 (
            "id" SERIAL,
            "測站名稱"	TEXT,
            "測站英文名稱"	TEXT,
            "空品區"	TEXT,
            "城市"	TEXT,
            "鄉鎮"	TEXT,
            "測站地址"	TEXT,
            "經度" DECIMAL,
            "緯度" DECIMAL,
            "測站類型"	TEXT,
            "測站編號" INTEGER,
            "更新時間" TEXT,
            PRIMARY KEY("id"),
            UNIQUE(測站名稱,更新時間)
        );
        '''
    )
    conn.commit()
    cursor.close()
    print("create_table成功")

def __insert_data(conn,VALUES:list[any])->None:
    cursor = conn.cursor()
    cursor_time = datetime.datetime.utcnow()
    sql = '''
    INSERT INTO 空氣品質監測站基本資料 (測站名稱, 測站英文名稱, 空品區, 城市, 鄉鎮, 測站地址, 經度, 緯度, 測站類型, 測站編號, 更新時間)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (測站名稱,更新時間) DO NOTHING
    '''
    VALUES.append(cursor_time)
    cursor.execute(sql, VALUES) 
    conn.commit()
    # cursor.close()

def update_render_data()->None:
    # 下載並更新資料庫 
    data = __download_air_data()
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER, 
                            password=pw.PASSWORD,
                            host=pw.HOST, 
                            port="5432")
    __create_table(conn)
    for item in data["records"]:
        __insert_data(conn,[item['sitename'],item['siteengname'],item['areaname'],item['county'],item['township'],item['siteaddress'],item['twd97lon'],item['twd97lat'],item['sitetype'],item['siteid']])
    conn.close()
```
index.py
```
import datasource 
import psycopg2
import password as pw
import tkinter as tk
from tkinter import ttk
from threading import Timer

class Window(tk.Tk):
    pass


def main():
    def update_data(w:Window)->None:
        datasource.update_render_data()
        #-----------更新treeView資料---------------
        #lastest_data = datasource.lastest_datetime_data()
        #w.youbikeTreeView.update_content(lastest_data)

        # w.after(10*60*1000, update_data,w)  #每隔10分鐘
        t = Timer(60*60, update_data,args=(window,))

    window = Window()
    window.title('空氣品質監測站基本資料')
    window.geometry('600x300')
    window.resizable(width=False,height=False)
    # window.after(1000, update_data, window)
    t = Timer(1, update_data, args=(window,))
    t.start()
    window.mainloop()
    

if __name__ == "__main__":
    main()
```