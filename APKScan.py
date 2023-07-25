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

markNameMap["libexec.so"] = "爱加密"
markNameMap["libexecmain.so"] = "爱加密"
markNameMap["ijiami.dat"] = "爱加密"
markNameMap["ijiami.ajm"] = "爱加密企业版"
markNameMap["af.bin"] = "爱加密企业版"

markNameMap["libsecexe.so"] = "梆梆免费版"
markNameMap["libsecmain.so"] = "梆梆免费版"
markNameMap["libSecShell.so"] = "梆梆免费版"
markNameMap["libDexHelper.so"] = "梆梆企业版"
markNameMap["libDexHelper-x86.so"] = "梆梆企业版"


markNameMap["libSecShel1.so"] = "梆梆企业版"

markNameMap["libprotectClass.so"] = "360"
markNameMap["libjiagu_ls.so"] = "360"
markNameMap["libjiagu.so"] = "360"
markNameMap["libjiagu_art.so"] = "360"
markNameMap["libjiagu_x86.so"] = "360"
markNameMap["libjiagu_a64.so"] = "360"
markNameMap["libjiagu_x64.so"] = "360"
markNameMap["libjgdtc.so"] = "360"
markNameMap["libjgdtc_x86.so"] = "360"
markNameMap["libjgdtc_a64.so"] = "360"
markNameMap["libjgdtc_x64.so"] = "360"
markNameMap["libjgdtc_art.so"] = "360"
markNameMap[".appkey"] = "360"


markNameMap["libegis.so"] = "通付盾"
markNameMap["libNSaferOnly.so"] = "通付盾"

markNameMap["libvenSec.so"] = "启明星辰"
markNameMap["libvenustech.so"] = "启明星辰"

markNameMap["libnqshield.so"] = "网秦加固"

markNameMap["libbaiduprotect.so"] = "百度加固"
markNameMap["libbaiduprotect_x86.so"] = "百度加固"
markNameMap["libbaiduprotect_art.so"] = "百度加固"

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

markNameMap["libtup.so"] = "腾讯"
markNameMap["libshell.so"] = "腾讯"
markNameMap["liblegudb.so"] = "腾讯"
markNameMap["mix.dex"] = "腾讯"
markNameMap["lib/armeabi/mix.dex"] = "腾讯"
markNameMap["lib/armeabi/mixz.dex"] = "腾讯"

markNameMap["tencent_sub"] = "腾讯云"
markNameMap["tosversion"] = "腾讯云"
markNameMap["lib/armeabi/libshell-super.2019.so"] = "腾讯云"
markNameMap["lib/armeabi/libshellx-super.2019.so"] = "腾讯云"
markNameMap["lib/armeabi/libshell-super.2020.so"] = "腾讯云"
markNameMap["lib/armeabi/libshell-super.2021.so"] = "腾讯云"
markNameMap["lib/armeabi/libBugly-yaq.so"] = "腾讯云"
markNameMap["assets/libshellx-super.2021.so"] = "腾讯云"
markNameMap["lib/armeabi-v7a/libxgVipSecurity.so"] = "腾讯乐固（VMP）"
markNameMap["lib/arm64-v8a/libxgVipSecurity.so"] = "腾讯乐固（VMP）"

markNameMap["libtosprotection.armeabi.so"] = "腾讯御安全"
markNameMap["libtosprotection.armeabi-v7a.so"] = "腾讯御安全"
markNameMap["libtosprotection.x86.so"] = "腾讯御安全"

markNameMap["libnesec.so"] = "网易易盾"

markNameMap["libAPKProtect.so"] = "APKProtect"

markNameMap["libkwscmm.so"] = "几维安全加固"
markNameMap["libkwscr.so"] = "几维安全加固"
markNameMap["libkwslinker.so"] = "几维安全加固"

markNameMap["libx3g.so"] = "顶像科技加固"

markNameMap["libapssec.so"] = "盛大加固"

markNameMap["librsprotect.so"] = "瑞星加固"

markNameMap["libuusafe.jar.so"] = "UU安全加固"
markNameMap["libuusafe.so"] = "UU安全加固"
markNameMap["libuusafeempty.so"] = "UU安全加固"

markNameMap["libitsec.so"] = "海云安加固"


markNameMap["libreincp.so"] = "珊瑚灵御"
markNameMap["libreincp_x86.so"] = "珊瑚灵御"

markNameMap["libapktoolplus_jiagu.so"] = "apktoolplus"



markNameMap["libcmvmp.so"] = "中国移动加固"
markNameMap["libmogosec_dex.so"] = "中国移动加固"

markNameMap["libmogosec_sodecrypt.so"] = "中国移动加固"
markNameMap["llibmogosecurity.so"] = "中国移动加固"
markNameMap["libmogosec_dex.so"] = "中国移动加固"
markNameMap["libcmvmp.so"] = "中国移动加固"

def check_jiagu(filename):
    azip = zipfile.ZipFile(filename)  # 默认模式r,读
    # print(azip.namelist()) # 返回所有文件夹和文件
    # print(azip.filename)# 返回该zip的文件名
    for zippath in azip.namelist():
            # print(zippath)
            for mark in markNameMap.keys():
                if mark in zippath:
                    print(u"检测到 【{}】 加固\n匹配特征:{}->{}\n".format(markNameMap[mark], zippath, mark))
                    return





if __name__ == '__main__':
    print(u'基于 "ApkScan-PKID查壳工具" 的规则 添加\修改 by avenue\n\n\n')
    
    help = ("""目前支持的加固厂商：
        娜迦、梆梆、爱加密、通付盾、360加固、
        百度加固、阿里加固、腾讯加固、 网易易盾
        盛大加固、瑞星加固、网秦加固、
        国信灵通加固、几维安全加固、顶像科技加固、
        apkprotect加固、等常规厂商
用法:        
    python3 apkscan-pkid.py D:\\android\\app.apk
        """)

    if len(sys.argv) != 2:
        print(help)
    else:
        check_jiagu(sys.argv[1])  # sys.argv[1]
