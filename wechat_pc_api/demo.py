# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wechat
import json
import time
from wechat import WeChatManager, MessageType
from Imgdecode import decodeing
from sqliteop import insert_db
wechat_manager = WeChatManager(libs_path='./libs')
sqlite_url="../Web/db.sqlite3"
imgstore_url="../Web/media/img"
chatroom='24803859571@chatroom'

# 这里测试函数回调
@wechat.CONNECT_CALLBACK(in_class=False)
def on_connect(client_id):
    print('[on_connect] client_id: {0}'.format(client_id))

@wechat.RECV_CALLBACK(in_class=False)
def on_recv(client_id, message_type, message_data):
    print('[on_recv] client_id: {0}, message_type: {1}, message:{2}'.format(client_id,
                                                                            message_type, json.dumps(message_data)))


@wechat.CLOSE_CALLBACK(in_class=False)
def on_close(client_id):
    print('[on_close] client_id: {0}'.format(client_id))


# 这里测试类回调， 函数回调与类回调可以混合使用
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        if message_type == MessageType.MT_RECV_PICTURE_MSG and (message_data["room_wxid"] == chatroom  or message_data["room_wxid"]==''):
            #这里有报错的需要修改一下啊
            imgurl=message_data["image"]
            time.sleep(1)
            pic_name,res=decodeing(imgurl,message_data['xor_key'],imgstore_url)
            print(pic_name,res)
            if pic_name!='Wrong File' and res:
                #第一层验证，图片大于100KB
                wechat_manager.send_text(client_id,'wxid_pkfm888mt7zd22','收到 请前往127.0.0.1进行查看')
                #这里加重复性验证，就不用修改数据库！通过查阅数据库得到当日图片url，然后一个个对比，如果有相同的就删除掉现在的那个
                #问题1：通过pic_name得到大小信息 二：通过数据库查找得到今天日期的图片url 
                # 三：去掉img/  让图片搜索对齐  四：遍历比较大小 五：如果有一样的就删掉
                insert_db(pic_name,sqlite_url,message_data['from_wxid'])
            elif pic_name=='网络不好或者撤回太早':
                wechat_manager.send_text(client_id,'wxid_pkfm888mt7zd22',pic_name)
    def on_time(self,client_id):
        date=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        a=1
        wechat_manager.send_text(client_id,'wxid_pkfm888mt7zd22','时间到了')


if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
