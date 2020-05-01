# coding:gb2312
import argparse
import zipfile

# apk�������
pack_ijiami = ['������', ['libexec.so', 'libexecmain.so','signed.bin','ijiami.ajm','af.bin','signed.bin']],
pack_apkprotect = ['apkprotect', ['apkprotect.com', 'libAPKProtect.so']],
pack_360 = ['360�ӹ�', ['libprotectClass.so', 'libprotectClass_x86.so'
                                            'libjiagu.so', 'libjiagu_art.so', 'libjiagu.so', 'libjiagu_x86.so']],
pack_bangbang = ['���ӹ���ҵ��', ['libDexHelper.so', 'libDexHelper-x86.so','libsecexe.so','libsecmain.so','libSecShell.so','secData0.jar','libSecShell-x86.so']],
pack_tp = ['��Ѷ�ӹ�', ['libtup.so', 'libshell.so','libshella-2.3.0.so','libshellx-2.3.0.so','libTmsdk-xxx-mfr.so','libtosprotection.x86.so','libtosprotection.armeabi.so','libtosprotection.armeabi-v7a.so','libshellx-xxxx.so','libshella-xxxx.so','mix.dex','mixz.dex']],
pack_baidu = ['�ٶȼӹ�', ['libbaiduprotect.so', 'ibbaiduprotect_x86.so']],
pack_najia = ['���ȼӹ�', ['libddog.so', 'libfdog.so', 'libchaosvmp.so', 'libedog.so','libchaosvmp.so']],
pack_wangqin = ['���ؼӹ�', ['libnqshieldx86.so', 'libnqshield.so']],
pack_ali = ['����ӹ�', ['libmobisec.so', 'libmobisecx.so']],
pack_tfd = ['ͨ���ܼӹ�', ['libegis.so']],
pack_jiwei = ['��ά�ӹ�', ['Libkwscmm.so','Libkwscr.so','libkwslinker.so']],
pack_shanhu = ['ɺ������ӹ�', ['libreincp.so','libreincp_x86.so']],
pack_wangyi = ['���ּӹ�', ['libnesec.so','libnqshield.so','libx3g.so','libitsec.so','libapssec.so','librsprotect.so','libapktoolplus_jiagu.so','libuusafe.jar.so','libuusafe.so',
                           'libuusafeempty.so','dp.arm-v7.so.dat','dp.arm.so.dat','libmogosecurity.so','libmogosec_sodecrypt.so','libmogosec_dex.so','libcmvmp.so']],

pak_list = [pack_ijiami, pack_apkprotect, pack_360, pack_bangbang,
            pack_tp, pack_baidu, pack_najia, pack_wangqin, pack_ali, pack_tfd, pack_jiwei, pack_shanhu, pack_wangyi]


# ��apk��
def checkPack(zipfilename):
    for pakcket in pak_list:
        for u in zipfilename:
            if u.split('/')[-1] in pakcket[0][1]:
                return pakcket[0][0]
    return 'δ�ӿǻ���δ֪��'


# ����ѹ�ļ�����ȡ�ļ��б�
def getzipfilename(path):
    filename = []
    try:
        zipinfo = zipfile.ZipFile(path, 'r')
        zipinfolist = zipinfo.infolist()
    except:
        pass
    #for f in zipinfo.namelist():
     #   filename.append(f)
    for f in zipinfolist:
        filename.append(f.filename)
    return filename


def main():
    parser = argparse.ArgumentParser(description='apk��ǹ��� by Ken')
    parser.add_argument('-f', '--file', help='ָ���ļ�', nargs="+")
    args = parser.parse_args()
    path = args.file
    if path:
        filename = getzipfilename(path[0])
        if not filename:
            print ('���Ǳ�׼apk�ļ�')
            exit()
        print (checkPack(filename))
    else:
        print ('��ѡ���ļ�·��')


if __name__ == '__main__':
    main()
