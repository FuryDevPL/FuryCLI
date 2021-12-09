import wmi
import youtube_dl
import time
import platform, socket, re, uuid, json, logging
import rich
import colorama
import os
import webbrowser
import gpuinfo
from rich import pretty
from rich.console import Console
from colorama import init
from colorama import Fore, Back, Style






init()
pretty.install()
console = Console()
computer = wmi.WMI()


#zmienne

txt = ""



#funkcja loggingu

logi = []
logfile = open('latest_log.txt', 'w+')

def logaj(msg):
    logi.append("LOG - " + time.asctime() + " => " + msg)

def save_log():
    for log in logi:
        logfile.write(log + "\n")

    logfile.close()





#yt download

def jutub():

    video_url = input("Wpisz adres URL filmu:" )
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"Download/{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Pobieranie ukończone... Zapisano w folderze FuryCLI/Download => {}".format(filename))



logaj("Uruchamianie...")


#komendy
cmd = {"cmds": " => Shows command list",
       "exit": " => Turns off FuryCLI by FuryDEV©",
       "sysinfo": " => Shows system information",
       "browser": " => Opens default web browser",
       "discord": " => Opens Discord",
       "spotify": " => Opens Spotify",
       "ytmp3": " => Youtube mp3 downloader"}


def cmds():
    print("List of commands")
    for komenda, desc in cmd.items():
        print(Fore.GREEN + komenda + Fore.BLUE + desc + "\n")




 

def getSystemInfo():
        print("="*40, "System Information", "="*40)
        uname = platform.uname()
        print(f"Computer's name: {uname.node}")
        uname = platform.uname()
        print(f"System: {uname.system}", )
        print(f"Computer's name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"CPU: {uname.processor}")
        print(f"GPU: {computer.Win32_VideoController()[0].name}" )






#pętla poleceń

print(
    Fore.CYAN + """

__________                     ______________________
___  ____/___  _____________  ___  ____/__  /____  _/ 
__  /_   _  / / /_  ___/_  / / /  /    __  /  __  /
_  __/   / /_/ /_  /   _  /_/ // /___  _  /____/ /
/_/      \__,_/ /_/    _\__, / \____/  /_____/___/
                       /____/
By FuryDEV©
For help, type <cmds>
""")

print("")
print("")
print("")

logaj("Uruchomiono")

while txt != "exit":
    txt = input("-$ ")
    logaj("Czekam na polecenia...")
    print("")
    if txt == "cmds":
        logaj("Typed cmds...")
        cmds()
        logaj("cmds command completed")
    elif txt == "sysinfo":
        getSystemInfo()
        logaj("Wykonano sysinfo")
    elif txt == "exit":
        logaj("Zamknięto program (komenda exit)")
    elif txt == "browser":
        webbrowser.open_new_tab("https://www.google.com")
    elif txt == "discord":
        logaj("Wywołano discord")
        os.system('start Discord:')
        logaj("Wykonano discord")
    elif txt == "spotify":
        logaj("Wywołano spotify")
        os.system('start Spotify:')
        logaj("Wykonano spotify")
    elif txt == "ytmp3":
        logaj("Wywołano ytmp3")
        jutub()
        logaj("Wykonano ytmp3")





save_log()


































