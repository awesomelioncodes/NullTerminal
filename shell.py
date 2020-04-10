import subprocess
import time
def inputsection():
    while True:
         terminalinput = str(input("Command> "))
         if (terminalinput == "ls"):
          print("shell.py")
          
         if (terminalinput == "about"):
          print("NullTerminal is a terminal program")

         if (terminalinput == "ipshow"):
          subprocess.call('ipconfig /all', shell=True)

         if (terminalinput == "wifishow"):
          subprocess.call('netsh wlan show all', shell=True)

         if (terminalinput == "help"):
          print("Help")
          print("ipshow: Displays IP Addresses")
          print("wifishow: Shows Network Information")
          print("ls: Show all files and Directorys in the current folder")
          print("about: Tells you about NullTerminal")
          print("ping google: Check Google's Ping")
          print("ping youtube: Check YouTube's Ping")
          print("ping facebook: Check Facebook's Ping")
          print("ping instagram: Check Instagram's Ping")
          print("chkdsk: Run Check Disk")
          print("project init: make a package.json file")
          print("shutdown -s: shutdown your pc")
          print("git init: make a git repository")
          print("time.sleep(5): sleeps for 5 seconds")

         if (terminalinput == "ping google"):
          subprocess.call('ping www.google.com', shell=True)
         if (terminalinput == "ping youtube"):
             subprocess.call('ping www.youtube.com', shell=True)

         if (terminalinput == "ping facebook"):
             subprocess.call('ping www.facebook.com', shell=True)
         if (terminalinput == "ping instagram"):
             subprocess.call('ping www.instagram.com', shell=True)
         if (terminalinput == "chkdsk"):
             subprocess.call('chkdsk', shell=True)
         if (terminalinput == "project init"):
             subprocess.call('npm init', shell=True)
         if (terminalinput == "shutdown -now"):
             subprocess.call('shutdown -s')
         if (terminalinput == "git init"):
             subprocess.call('git init')
         if (terminalinput == "sleep(5sec)"):
             time.sleep(5)

inputsection() 
