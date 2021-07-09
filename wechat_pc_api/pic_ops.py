from PIL import Image
import os
import itertools
def get_size(file):
    # 获取文件大小:KB
    size = os.path.getsize(file)
    return size / 1024

def get_outfile(infile, outfile):
    if outfile:
        return outfile
    dir, suffix = os.path.splitext(infile)
    outfile = '{}-out{}'.format(dir, suffix)
    return outfile

def resize_image(infile, outfile='', x_s=142):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    outfile = get_outfile(infile, outfile)
    out.save(outfile)


def image_join(png1, png2, save_path, flag='lateral'):
    """
    :param png1: path
    :param png2: path
    :param flag: lateral or vertical
    :return:
    """
    img1, img2 = Image.open(png1), Image.open(png2)
    size1, size2 = img1.size, img2.size
    if flag == 'lateral': # 横向
        join_image = Image.new('RGB', (size1[0] + size2[0], size1[1])) # 创建一个2原图合并后大小的空白图
        loc1, loc2 = (0, 0), (size1[0], 0)
        join_image.paste(img1, loc1) # 将原图1黏贴到指定位置
        join_image.paste(img2, loc2) # 将原图2黏贴到指定位置
        join_image.save(save_path)
        return save_path
    elif flag == 'vertical': # 纵向
        join_image = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        join_image.paste(img1, loc1)
        join_image.paste(img2, loc2)
        join_image.save(save_path)
        return save_path
if __name__=="__main__":
    save_path1="./thumb/0.jpg"
    save_path2="./thumb/1.jpg"
    save_path3="./thumb/join.jpg"
    image_join(save_path1, save_path2, save_path3, flag='vertical')
    image_join("./thumb/join.jpg","./thumb/2.jpg","./thumb/joinjoin.jpg",flag='vertical')