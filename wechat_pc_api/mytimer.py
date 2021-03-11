import threading
import time
import datetime
#最好是每晚十点开始投票并且结束今日收图，开始下一天收图。早上八点结束投票。  这样对后端的逻辑要求大大提升了。
#那其实弄两个timer就没问题了。一个早八一个晚八
def get_time_distanse(date,time_setting):
    #获得现在与下一个设定时间的秒数距离
    if not date:
        return 0
    date_setting = datetime.datetime.now().replace(year=date.year, month=date.month,
        day=date.day, hour=time_setting, minute=0, second=0)
    if date.__ge__(date_setting):
        date_setting=date_setting+datetime.timedelta(days=1)
    seconds=(date_setting-date).total_seconds()
    return int(seconds)

def startTimer(): 
    if timer != None: 
        print("1")
        timer.finished.wait(get_time_distanse(datetime.datetime.now(),22))
        timer.function()
if __name__== "__main__":
    timer=threading.Timer(2,startTimer)
    #timer.start()
    print(get_time_distanse(datetime.datetime.now(),13))
    