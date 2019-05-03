import subprocess
def dwn():
    print ("Shunting Down")
    subprocess.call("reboot.sh", shell=True)
def newmeth():
    print("Hello World")
