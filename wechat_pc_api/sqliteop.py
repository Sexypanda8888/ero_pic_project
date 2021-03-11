import sqlite3
import time
import pytz
import datetime
#我只需要插入操作
def insert_db(pic_name,sqlite_url,update_person):
      conn = sqlite3.connect(sqlite_url)
      tz=pytz.timezone('Asia/Shanghai')
      date=datetime.datetime.now(tz=tz).strftime("%Y-%m-%d %H:%M:%S")
      c = conn.cursor()
      url='img/'+pic_name
      c.execute("INSERT INTO app1_img (img_url,date,vote,update_person,delete_vote) \
            VALUES ('%s',datetime('%s'), 0 ,'%s',0)"% (url,date,update_person))
      conn.commit()
      conn.close()
      return 
# insert_db('dsade',"../../../Web/db.sqlite3",'panda')

#后面还需要查询操作！