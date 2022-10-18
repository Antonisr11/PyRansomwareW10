# PyRansomwareW10
I created Ransomware in Python.

<ins>**Spreading a virus and infecting a foreign computer without the knowledge and permission of its owner brings legal (and not only) consequences. This project was developed for educational purposes and therefore files are decrypted without paying any ransom. In any case, use the program ONLY on your own computer and ONLY to examine how a ransomware works.**</ins>

## General

PyRansomwareW10:

1. Can work on Windows 10
2. If the user runs one exe, the virus is activated
3. It runs invisibly from the user
4. If any error appears, the virus deactivates itself
5. Uses AES-256bit encoding for files
6. Uses RSA-2048bit encoding for key
7. Encrypt 43 file types including txt, doc, xls, ppt, jpg, png, mp3, mp4, etc
8. Encrypt only files in Documents, Pictures and Videos
9. Code is obfuscated 

## Encyption

When encryption starts, PyRansomwareW10 generates decryptor.exe and saves all files it will encrypt. Then it generates AES and RSA keys and exports RSA private key to Desktop (without this key, none can decrypt files). If thus far there is not any error, PyRansomwareW10 starts the encryption (using AES algorithm).

Then it encrypts the AES key with RSA algorithm. 

![image](https://user-images.githubusercontent.com/76475823/196406429-8527dc2b-91ff-4894-b513-395a2995e1c1.png)

Lastly, user's desktop wallpaper changes with this image to scare them:

![image](https://user-images.githubusercontent.com/76475823/196401860-3619ba77-0d3a-416a-901a-4284c59a1a2f.png)

## Decryption

When encryption ends, the decryptor deletes the encryption program and shows this screen to the user:

![image](https://user-images.githubusercontent.com/76475823/196402942-09c02dea-f021-40da-a094-1f47d2d5c83d.png)

When the user clicks the green button, an explorer window appears and they have to select RSA private key. Then the encrypted AES key is decrypted with RSA private key and user's files are decrypted with the AES key.

![image](https://user-images.githubusercontent.com/76475823/196406608-641251c7-2379-42a8-ae04-57d911be032b.png)

Finally, desktop wallpaper is restored to default and every file created for ransomware is deleted.
