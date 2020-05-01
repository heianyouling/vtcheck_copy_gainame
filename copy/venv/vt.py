import os
#import nose
import virustotal3master1.virustotal3.core
def main():
    #vt = VirusTotalPublicApi('0703c8673d85549f143f9bc0e845ba9d255bfc10a9c7140923d4a63651807a83')
    vt_key = '22c6d056f1e99b8fb4fa6c2a811178723735e9840de18fa2df83fccfd21c95a0'
    API_KEY = os.environ[vt_key]
    vt_files = virustotal3.core.Files(API_KEY)
    info = vt_files.info_file('e86d4eb1e888bd625389f2e50644be67a6bdbd77ff3bceaaf182d45860b88d80')
    print(info)
if __name__ == '__main__':
    main()