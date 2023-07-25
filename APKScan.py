#!/usr/bin/env python3
# coding=utf-8
# python version 3.7 by 6time
#
import sys
import zipfile



markNameMap = {}
markNameMap["libchaosvmp.so"] = "娜迦"
markNameMap["libddog.so"] = "娜迦"
markNameMap["libfdog.so"] = "娜迦"
markNameMap["libedog.so"] = "娜迦企业版"


markNameMap["libexecmain.so"] = "爱加密"
markNameMap["libexec.so"] = "爱加密"
markNameMap["ijiami.dat"] = "爱加密"
markNameMap["ijiami.ajm"] = "爱加密企业版"
markNameMap["af.bin"] = "爱加密企业版"

markNameMap["libsecexe.so"] = "梆梆免费版"
markNameMap["libsecmain.so"] = "梆梆免费版"
markNameMap["libSecShell.so"] = "梆梆免费版"
markNameMap["libDexHelper.so"] = "梆梆企业版"
markNameMap["libDexHelper-x86.so"] = "梆梆企业版"



markNameMap["libprotectClass.so"] = "360"
markNameMap["libjiagu.so"] = "360"
markNameMap["libjiagu_art.so"] = "360"
markNameMap["libjiagu_x86.so"] = "360"

markNameMap["libjiagu_ls.so"] = "360"

markNameMap["libjiagu_a64.so"] = "360"

markNameMap["libjiagu_x64.so"] = "360"

markNameMap["libjgdtc.so"] = "360"

markNameMap["libjgdtc_x86.so"] = "360"

markNameMap["libjgdtc_a64.so"] = "360"

markNameMap["libjgdtc_x64.so"] = "360"

markNameMap["libjgdtc_art.so"] = "360"
markNameMap[".appkey"] = "360"

markNameMap["libmanxi.so"] = "蛮犀"
markNameMap["libegis.so"] = "通付盾"
markNameMap["libNSaferOnly.so"] = "通付盾"

markNameMap["libvenSec.so"] = "启明星辰"
markNameMap["libvenustech.so"] = "启明星辰"

markNameMap["libnqshield.so"] = "网秦"

markNameMap["libbaiduprotect.so"] = "百度"
markNameMap["libbaiduprotect_x86.so"] = "百度"
markNameMap["libbaiduprotect_art.so"] = "百度"
markNameMap["baiduprotect1.jar"] = "百度"

markNameMap["aliprotect.dat"] = "阿里聚安全"
markNameMap["libsgmain.so"] = "阿里聚安全"
markNameMap["libsgsecuritybody.so"] = "阿里聚安全"
markNameMap["libmobisec.so"] = "阿里聚安全"

markNameMap["libfakejni.so"] = "阿里聚安全"

markNameMap["libzumadata.so"] = "阿里聚安全"

markNameMap["libzuma.so"] = "阿里聚安全"
markNameMap["libpreverify1.so"] = "阿里聚安全"
markNameMap["libdemolishdata.so"] = "阿里聚安全"
markNameMap["libdemolish.so"] = "阿里聚安全"

markNameMap["libtup.so"] = "腾讯乐固"
markNameMap["libshell.so"] = "腾讯乐固"
markNameMap["liblegudb.so"] = "腾讯乐固"
markNameMap["mix.dex"] = "腾讯乐固"
markNameMap["lib/armeabi/mix.dex"] = "腾讯乐固"
markNameMap["lib/armeabi/mixz.dex"] = "腾讯乐固"
markNameMap["lib/armeabi-v7a/libxgVipSecurity.so"] = "腾讯乐固VMP"
markNameMap["lib/arm64-v8a/libxgVipSecurity.so"] = "腾讯乐固VMP"



markNameMap["tencent_sub"] = "腾讯御安全"
markNameMap["tosversion"] = "腾讯御安全"
markNameMap["lib/armeabi/libshell-super.2019.so"] = "腾讯御安全"
markNameMap["lib/armeabi/libshellx-super.2019.so"] = "腾讯御安全"

markNameMap["lib/armeabi/libshell-super.2020.so"] = "腾讯御安全"

markNameMap["lib/armeabi/libshell-super.2021.so"] = "腾讯御安全"

markNameMap["lib/armeabi/libBugly-yaq.so"] = "腾讯御安全"


markNameMap["assets/libshellx-super.2021.so"] = "腾讯御安全"


markNameMap["libtosprotection.armeabi.so"] = "腾讯御安全"
markNameMap["libtosprotection.armeabi-v7a.so"] = "腾讯御安全"
markNameMap["libtosprotection.x86.so"] = "腾讯御安全"

markNameMap["libnesec.so"] = "网易易盾"

markNameMap["libAPKProtect.so"] = "APKProtect"

markNameMap["libkwscmm.so"] = "几维安全"
markNameMap["libkwscr.so"] = "几维安全"
markNameMap["libkwslinker.so"] = "几维安全"

markNameMap["libx3g.so"] = "顶像科技"

markNameMap["libapssec.so"] = "盛大"

markNameMap["librsprotect.so"] = "瑞星"

markNameMap["libuusafe.jar.so"] = "UU安全"
markNameMap["libuusafe.so"] = "UU安全"
markNameMap["libuusafeempty.so"] = "UU安全"

markNameMap["libitsec.so"] = "海云安"


markNameMap["libreincp.so"] = "珊瑚灵御"
markNameMap["libreincp_x86.so"] = "珊瑚灵御"

markNameMap["libapktoolplus_jiagu.so"] = "apktoolplus"



markNameMap["libcmvmp.so"] = "中国移动"
markNameMap["libmogosec_dex.so"] = "中国移动"

markNameMap["libmogosec_sodecrypt.so"] = "中国移动"
markNameMap["libmogosecurity.so"] = "中国移动"

markNameMap["mogosec_classes"] = "中国移动"
markNameMap["mogosec_data"] = "中国移动"
markNameMap["mogosec_march"] = "中国移动"
markNameMap["mogosec_dexinfo"] = "中国移动"


weijiagu=("此apk未采用加固或为未知加固厂商！")

def check_jiagu(filename):
    azip = zipfile.ZipFile(filename)  # 默认模式r,读
    # print(azip.namelist()) # 返回所有文件夹和文件
    # print(azip.filename)# 返回该zip的文件名
    for zippath in azip.namelist():
        # if 'lib' in zippath:
        #     print(zippath)
        for mark in markNameMap.keys():
            if mark in zippath:
                print(u"检测到 【{}】 加固\n匹配特征:{}->{}\n".format(markNameMap[mark], zippath, mark))
                return

    print(weijiagu)




if __name__ == '__main__':
    print(u'基于 "ApkScan-PKID查壳工具" 的规则 添加\修改 by avenue-le\n\n')
    
    help = ("""目前支持的厂商：
        娜迦、梆梆、爱加密、通付盾、360、
        百度、阿里、腾讯、 网易易盾
        盛大、瑞星、网秦、
        国信灵通、几维安全、顶像科技、
        apkprotect、等常规厂商
用法:        
    python3 APKScan.py D:\\android\\app.apk
        """)

    if len(sys.argv) != 2:
        print(help)
    else:
        check_jiagu(sys.argv[1])  # sys.argv[1]
