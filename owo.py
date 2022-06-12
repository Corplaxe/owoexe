import pyautogui
import time 
import random

print('''
OwO Para Kasma botuna hoşgeldin.
Kullanmak için tek yapman gereken şey programı başlattıktan sonra 3 adet değer girip discorddaki konuşma kutucuğunu seçmek.
Otomatikman yazı yazılmaya başladığını göreceksin :)
Çıkmak için Ctrl + C
''')

a = int(input('Random zaman değer aralığından birincisini seçin (önerilen = 4) :  '))
b = int(input('Random zaman değer aralığından ikincisini seçin (önerilen = 15) :  '))
c = int(input('Programın yazdığı yazıyı kaç saniyede göndermesi gerektiğini girin (önerilen = 5):  '))
time.sleep(a)

text = 'owo hunt'
text2 = 'owo battle'


while True:

    ft= random.uniform(b,c)

    pyautogui.typewrite(text)
    time.sleep(ft)
    pyautogui.press('enter')

    pyautogui.typewrite(text2)
    time.sleep(ft)
    pyautogui.press('enter')

    print(ft)