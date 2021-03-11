import os
import time
import judgement
import hashlib
def GetFileMd5(opened_file):
    myhash = hashlib.md5()
    while True:
        b = opened_file.read(8096)
        if not b :
            break
        myhash.update(b)  #md5算法本身就是分块的，因此可以多次更新  可以先读，最后再输出
    return myhash.hexdigest()


pic_head = {'jpg':0xffd8, 'png':0x8950, 'gif':0x4749}  #jpg png gif
pic_tail = {'jpg':0xffd9, 'png':0x6082, 'gif':0x003B}
#该函数功能为对一张图片进行解码并放入指定文件夹,返回其名字
def decodeing(imgurl,xor_key,store_url):
    #先判断文件是否存在，不在时等待； 之后判断文件是否下载完全；完全以后继续操作
    k=0
    while not os.path.exists(imgurl):
        time.sleep(1)
        print("not exist")
        k+=1
        if k >60:
            return ['网络不好或者撤回太早',False]
            
    dat_file = open(imgurl, "rb") 
    dat_read = dat_file.read(2)
    dat_file.seek(0,0)
    idt= dat_read[0]
    idt=idt*16*16+ dat_read[1]
    #如果还没加密好，就不需要解密了
    print(dat_read,idt)
    flag=1
    if idt == pic_head['jpg']:
        pic_id = '.jpg'
    elif idt == pic_head['png']:
        pic_id = '.png'
    elif idt == pic_head['gif']:
        pic_id = '.gif'
    else:
        flag=0
        #说明该文件可能是已经加密好了。
        idt= dat_read[0] ^ xor_key
        idt=idt*16*16+ dat_read[1] ^ xor_key
        if idt == pic_head['jpg']:
            pic_id = '.jpg'
        elif idt == pic_head['png']:
            pic_id = '.png'
        elif idt == pic_head['gif']:
            pic_id = '.gif'
        else :
            #不是正常文件
            return ['Wrong File',False]
    count = 0 
    while True:
        #通过重复读取
        if count >500:
            return ['网络不好或者撤回太早',False]
        dat_file.seek(-2,2)
        dat_read = dat_file.read(2)
        if flag==0:
            idt= dat_read[0] ^ xor_key
            idt=idt*16*16+ dat_read[1] ^ xor_key
        else:
            idt= dat_read[0]
            idt=idt*16*16+ dat_read[1]
        
        if idt == pic_tail['jpg']:
            break
        elif idt == pic_tail['png']:
            break
        elif idt == pic_tail['gif']:
            break
        count+=1
        print(idt)
        time.sleep(1)
    time_now=str(int(time.time()))
    pic_name = store_url + '/' + time_now + pic_id   #需要测试同一时间发出图片会如何应对，按照这个来改命名方式
    pic_write = open(pic_name, "wb")
    dat_file.seek(0,0)
    for dat_data in dat_file:
        for dat_byte in dat_data:
            if flag==0:
                pic_data = dat_byte ^ xor_key
                pic_write.write(bytes((pic_data,)))   #此处为什么要加括号？不明白
            else:
                pic_write.write(bytes((dat_byte,)))
    dat_file.close()
    pic_write.close()
    res=judgement.judge(pic_name)
    return  [time_now + pic_id,res]

# img_url="C:\\Users\\17197\\Desktop\\robot\\6d11b2cc1b4b14daa8b0c39a07c8cb75.dat"
# xor_key=228
# store_url='C:\\Users\\17197\\Desktop\\robot'
# decode(imgurl=img_url,xor_key=228,store_url=store_url)
