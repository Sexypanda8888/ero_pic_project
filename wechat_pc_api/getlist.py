from __future__ import unicode_literals

import wechat
import json
import time
from wechat import WeChatManager, MessageType
from Imgdecode import decodeing
from sqliteop import insert_db
import os 
wechat_manager = WeChatManager(libs_path='../../libs')
class LoginTipBot(wechat.CallbackHandler):

    @wechat.RECV_CALLBACK(in_class=True)
    def on_message(self, client_id, message_type, message_data):
        if message_type == MessageType.MT_USER_LOGIN:
            wechat_manager.get_chatroom_members(client_id,'24803859571@chatroom')#返回了一个Int值，不知道想干嘛
        if message_type ==11032 :
            nickname_wxid={}
            lists=message_data['member_list']
            for i in lists:
                nickname_wxid[i['nickname']]=i['wxid']
            print(nickname_wxid)
        print()
if __name__ == "__main__":
    bot = LoginTipBot()

    # 添加回调实例对象
    wechat_manager.add_callback_handler(bot)
    wechat_manager.manager_wechat(smart=True)

    # 阻塞主线程
    while True:
        time.sleep(0.5)
