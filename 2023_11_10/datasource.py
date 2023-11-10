import requests
import psycopg2
import password as pw

def download_air_data()->list[dict]:
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

def create_table(conn):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 觀測站(
            "測站編號"	INTEGER,
            "城市"	TEXT NOT NULL,
            "測站名稱"	TEXT NOT NULL,
            "空品區"	TEXT NOT NULL,
            "測站類型"	TEXT NOT NULL,
            "測站地址"	TEXT NOT NULL,
            "資料更新時間" DATETIME NOT NULL,
            PRIMARY KEY(測站編號),
            UNIQUE(城市,測站名稱) ON CONFLICT REPLACE
        );
        '''
    )
    con.commit()

def insert_data(conn,values:list[any])->None:
    cursor = conn.cursor()
    sql = '''
    REPLACE INTO 觀測站(測站編號, 城市, 測站名稱, 空品區, 測站類型, 測站地址, 資料更新時間)
        VALUES(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)    
    conn.commit()
    cursor.close()