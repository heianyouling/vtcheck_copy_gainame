import argparse
import shutil
import shutil, os
import pyperclip
# encoding:utf-8
def main():
     parser = argparse.ArgumentParser()
     parser.add_argument('-f', '--file', help='', nargs="+")
     args = parser.parse_args()

     path2 = "".join(args.file)
     file_name(path2)
#
#     path3 = path2.split('\\')
#
#     path1 = ""
#     log_name = '_' + path1.join(path3[-1])
#
#     if os.path.isdir(path2):
#
#         shutil.copytree(path2, log_name)
#     elif os.path.isfile(path2):
#
#         shutil.copyfile(path2, log_name)
#     exit()



def file_name(path2):
    text = []
    text1=[]
    for root, dirs, files in os.walk(path2):
        #print(root)  # 当前目录路径
        #print(dirs)  # 当前路径下所有子目录
        text.append(files)
    for name in text:
        for i in name:
            text1.append(i)
    #print(text)  # 当前路径下所有非目录子文件
    str = '\r\n'.join('%s' %id for id in text1)
    print(str)
    pyperclip.copy(str)


#pyperclip.copy(text)


if __name__ == '__main__':
    main()
