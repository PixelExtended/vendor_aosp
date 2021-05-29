# Authored By : @https://t.me/Immanuel_Raj

# Imports
import os
import sys
from os import path
import os.path
import time

# OTA
def ota():
    print ("\nMoving to OTA repository\n")
    os.chdir("OTA")
    print("\nUnshallowing the repository\n")
    os.system("git fetch pex --unshallow")
    os.system("git checkout eleven")
    os.system("git pull")
    print ("")
    os.chdir("builds")
    if os.path.isfile('%s.json'%codename)!=True:
        print("\nCreating the device specific necessary stuffs... xd\n")
        os.mknod("%s.json"%codename)
        os.chdir("..")
        os.chdir("changelogs")
        os.system("mkdir %s"%codename)
        os.chdir("%s"%codename)
        os.mknod("temp.txt")
        os.chdir("..")
        os.chdir("..")
        os.chdir("..")
        print("\nCreating the necessary files completed succesfully... xd\n")
        print("\nHey new maintainer!!! welcome to the Pixel Extended Project hope you have a great time here\n")
        print("\nContinuing the script....xd\n")
        os.system("bash ota.sh %s %s %s %s"%(codename,name,tgname,xda))
        os.chdir("OTA")
        os.system("git add .")
        os.system("git commit -m 'OTA:Latest update for %s'"%codename)
        os.system("git push")
    else:
        os.chdir("..")
        os.chdir("..")
        print("\nContinuing the script....xd\n")
        os.system("bash ota.sh %s %s %s %s"%(codename,name,tgname,xda))
        os.chdir("OTA")
        os.system("git add .")
        os.system("git commit -m 'OTA:Latest update for %s'"%codename)
        os.system("git push")
        print ("")

# Sync
print("\n Hold Tight while we sync our sources\n ")
os.system("repo init -u https://github.com/PixelExtended/manifest -b eleven --depth=1")
os.system("rm -rf OTA frameworks/base packages/apps/Settings vendor/aosp packages/apps/RavenLair")
os.system("repo sync -c --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j$(nproc --all)")

# Requirements
os.system("sudo apt-get install sshpass -y")
print("\nIf the Above step failed do install it manually and run the script again Packagname :- sshpass \n")

# Banner
print ("")
print ("")
print ("")
print("""
█▀█ █ ▀▄▀ █▀▀ █░░ ▄▄ █▀▀ ▀▄▀ ▀█▀ █▀▀ █▄░█ █▀▄ █▀▀ █▀▄
█▀▀ █ █░█ ██▄ █▄▄ ░░ ██▄ █░█ ░█░ ██▄ █░▀█ █▄▀ ██▄ █▄▀""")
print ("")
print ("")
print ("")
print ("ONLY FOR OFFICIAL BUILDS/USE")
print ("")
print ("")
print ("")

# Variant & Building & Upload+OTA
name=input("\nEnter your name :- eg Aryan_Gupta : ")
tgname=input("\nEnter Your telegram username [Without '@'] : ")
codename=input("\nEnter your device code name :- eg miatoll/laurel_sprout : ")
xda=input("\nEnter Your device's XDA post link : '")
btype=input("\nEnter the type of build u want [user/eng/userdebug] : ")
sfun=input("\nEnter your sourceforge username :-  ")
sfpass=input("\nEnter your sourceforge password : ")

os.system("bash build.sh %s %s"%(codename,btype))
os.system("sshpass -p '%s' rsync --progress out/target/product/%s/PixelExtended*.zip %s@frs.sourceforge.net:/home/frs/project/pixelextended/%s/"%(sfpass,codename,sfun,codename))
ota()
