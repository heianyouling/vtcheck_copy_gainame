import os
#import pandas
#import nose
import hashlib
import virustotal3.core
import argparse
import pyperclip
import shutil
# encoding:utf-8
def CalcMD5(filepath):
   with open(filepath,'rb') as f:
        md5obj = hashlib.sha1()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        print(hash)
        return hash

def create_dir_not_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='', nargs="+")
    args = parser.parse_args()
    path2 = "".join(args.file)
    print(path2)
    a=[]
    m=0
    path3=path2+'\\'+'white'
    path4 = path2 + '\\' + 'virus'
    path5 = path2 + '\\' + 'notfount'
    create_dir_not_exist(path3)
    create_dir_not_exist(path4)
    create_dir_not_exist(path5)
    # 7eb39d6072609109725bcf27b40c82b76491abcbeb189c4ac3e67b16e0db4fa4
    vt_key = '7eb39d6072609109725bcf27b40c82b76491abcbeb189c4ac3e67b16e0db4fa4'
    for derName, subfolders, filenames in os.walk(path2):
        for i in range(len(filenames)):
            file_path = derName +'\\'+ filenames[i]
            hash1 = CalcMD5(file_path)
            #filenames[i].append(hash1)
            print(filenames[i])
            vt_files = virustotal3.core.Files(vt_key)
            info = vt_files.info_file(hash1)
            print(info)
            for x in info :
                print(x)
            if x=='error':
                new_path2 = path2 + '\\' + 'notfount' + '\\' + filenames[i]
                shutil.move(file_path, new_path2)
            else:
                j = 0
                m=m+1
                print(m)
                for k, v in info['data']['attributes']['last_analysis_results'].items():
                    # print(v['result'])
                    # s=v['result']
                    # print(type(s))

                    if v['result'] != None:
                        j=j+1
                print(j)
                if j <= 4:
                    new_path = path2 + '\\' + 'white'+'\\'+filenames[i]
                    shutil.move(file_path, new_path)
                else:
                    new_path1 = path2 + '\\' + 'virus' + '\\' + filenames[i]
                    shutil.move(file_path,new_path1)
        return
    #print(info['virustotal3.errors.VirusTotalApiError']['error']['message'])
    #result = info.split("},")








    #print(info['data']['attributes']['last_analysis_results'].keys())
if __name__ == '__main__':
    main()