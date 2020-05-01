# coding:gb2312
import argparse
import zipfile

# apk查壳特征
pack_ijiami = ['爱加密', ['libexec.so', 'libexecmain.so','signed.bin','ijiami.ajm','af.bin','signed.bin']],
pack_apkprotect = ['apkprotect', ['apkprotect.com', 'libAPKProtect.so']],
pack_360 = ['360加固', ['libprotectClass.so', 'libprotectClass_x86.so'
                                            'libjiagu.so', 'libjiagu_art.so', 'libjiagu.so', 'libjiagu_x86.so']],
pack_bangbang = ['梆梆加固企业版', ['libDexHelper.so', 'libDexHelper-x86.so','libsecexe.so','libsecmain.so','libSecShell.so','secData0.jar','libSecShell-x86.so']],
pack_tp = ['腾讯加固', ['libtup.so', 'libshell.so','libshella-2.3.0.so','libshellx-2.3.0.so','libTmsdk-xxx-mfr.so','libtosprotection.x86.so','libtosprotection.armeabi.so','libtosprotection.armeabi-v7a.so','libshellx-xxxx.so','libshella-xxxx.so','mix.dex','mixz.dex']],
pack_baidu = ['百度加固', ['libbaiduprotect.so', 'ibbaiduprotect_x86.so']],
pack_najia = ['娜迦加固', ['libddog.so', 'libfdog.so', 'libchaosvmp.so', 'libedog.so','libchaosvmp.so']],
pack_wangqin = ['网秦加固', ['libnqshieldx86.so', 'libnqshield.so']],
pack_ali = ['阿里加固', ['libmobisec.so', 'libmobisecx.so']],
pack_tfd = ['通付盾加固', ['libegis.so']],
pack_jiwei = ['几维加固', ['Libkwscmm.so','Libkwscr.so','libkwslinker.so']],
pack_shanhu = ['珊瑚灵域加固', ['libreincp.so','libreincp_x86.so']],
pack_wangyi = ['各种加固', ['libnesec.so','libnqshield.so','libx3g.so','libitsec.so','libapssec.so','librsprotect.so','libapktoolplus_jiagu.so','libuusafe.jar.so','libuusafe.so',
                           'libuusafeempty.so','dp.arm-v7.so.dat','dp.arm.so.dat','libmogosecurity.so','libmogosec_sodecrypt.so','libmogosec_dex.so','libcmvmp.so']],

pak_list = [pack_ijiami, pack_apkprotect, pack_360, pack_bangbang,
            pack_tp, pack_baidu, pack_najia, pack_wangqin, pack_ali, pack_tfd, pack_jiwei, pack_shanhu, pack_wangyi]


# 查apk壳
def checkPack(zipfilename):
    for pakcket in pak_list:
        for u in zipfilename:
            if u.split('/')[-1] in pakcket[0][1]:
                return pakcket[0][0]
    return '未加壳或者未知壳'


# 不解压文件，获取文件列表
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
    parser = argparse.ArgumentParser(description='apk查壳工具 by Ken')
    parser.add_argument('-f', '--file', help='指定文件', nargs="+")
    args = parser.parse_args()
    path = args.file
    if path:
        filename = getzipfilename(path[0])
        if not filename:
            print ('不是标准apk文件')
            exit()
        print (checkPack(filename))
    else:
        print ('请选择文件路径')


if __name__ == '__main__':
    main()
