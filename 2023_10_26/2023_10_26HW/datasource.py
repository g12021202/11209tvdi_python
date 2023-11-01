import requests
import sqlite3
def __download_air_data()->list[dict]:
    '''
    下載 
    https://data.moenv.gov.tw/swagger/#/%E5%A4%A7%E6%B0%A3/get_aqx_p_07
    curl -X GET "https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=cbb6f9c0-9c3b-4086-b464-80594cd61f78" -H "accept: */*"
    '''
    air_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_07?api_key=cbb6f9c0-9c3b-4086-b464-80594cd61f78'
    response = requests.get(air_url)
    print("下載成功")
    return response.json()

def __create_table(conn:sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 空氣品質監測站基本資料 (
            "id" INTEGER,
            "測站代碼" TEXT NOT NULL,
            "測站名稱" TEXT NOT NULL,
            "縣市" TEXT NOT NULL,
            "測項代碼" TEXT NOT NULL,
            "測項名稱" TEXT NOT NULL,
            "測項英文名稱" TEXT NOT NULL,
            "測項單位" TEXT NOT NULL,
            "監測日期" TEXT NOT NULL,
            "數值" TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
            UNIQUE(測站代碼,測項代碼,監測日期) ON CONFLICT REPLACE
        );
        '''
    )
    conn.commit()

def update_sqlite_data():
    '''
    下載,並更新資料庫
    '''
    data = download_air_data()
    conn = sqlite3.connect("air.db")
    print(type(conn))
    __create_table(conn)
    for item in data:
        __insert_data(conn,[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
    conn.close()