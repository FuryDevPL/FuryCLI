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

    video_url = input("Type video adress: " )
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Completed... Saved file in FuryCLI folder => {}".format(filename))



logaj("Starting FuryCLI...")


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
p = ""   
logaj("Started FuryCLI")

while txt != "exit":
    txt = input("-$ ")
    logaj("Czekam na polecenia...")
    print("")
    if txt == "cmds":
        logaj("Using " + txt)
        cmds()
        logaj("Completed " + txt)
    elif txt == "sysinfo":
        logaj("Using " + txt)
        getSystemInfo()
        logaj("Completed " + txt)
    elif txt == "exit":
        logaj("Completed " + txt)
    elif txt == "browser":
        webbrowser.open_new_tab("https://www.google.com")
        print("Done!")
        logaj("Completed " + txt)
    elif txt == "discord":
        logaj("Using " + txt)
        os.system('start Discord:')
        logaj("Completed " + txt)
        print("Done!")
    elif txt == "spotify":
        logaj("Using " + txt)
        os.system('start Spotify:')
        logaj("Completed " + txt)
        print("Done!")
    elif txt == "ytmp3":
        logaj("Using " + txt)
        jutub()
        logaj("Completed " + txt)





save_log()


































