import subprocess
import http.server
import socketserver



def dwn():
    print ("Shunting Down")
    subprocess.call("sudo reboot", shell=True)
def newmeth():
    print("Hello World")
def startServer():
    PORT = 8080
    Handler = http.server.TCPServer(("",PORT),Handler) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
