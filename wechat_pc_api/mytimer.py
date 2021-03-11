import threading
import time
import datetime
#最好是每晚十点开始投票并且结束今日收图，开始下一天收图。早上八点结束投票。  这样对后端的逻辑要求大大提升了。
#那其实弄两个timer就没问题了。一个早八一个晚八
def time_cul(startTime,endTime):
    '''计算两个时间点之间的分钟数  '2019-07-28 00:00:00' '''
    startTime1 = startTime
    endTime1 = endTime
    startTime2 = datetime.datetime.strptime(startTime1, "%Y-%m-%d %H:%M:%S")
    endTime2 = datetime.datetime.strptime(endTime1, "%Y-%m-%d %H:%M:%S")
    total_seconds = (endTime2 - startTime2).total_seconds()
    return int(total_seconds)
def startTimer(): 
    if timer != None: 
        print("1")
        timer.finished.wait(timer.interval)
        timer.function() 

timer=threading.Timer(2,startTimer)
#timer.start()
print(time_cul('2020-07-28 00:00:00','2020-07-28 00:01:00'))