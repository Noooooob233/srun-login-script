import os
import time
from BitSrunLogin.LoginManager import LoginManager

def is_connect_internet(testip):
    status = os.system(u"ping {} -c 5".format(testip))
    return status == 0
        
if __name__ == "__main__":
    username = "username"
    password = "password"
    testip = "www.baidu.com" # IP to test whether the Internet is connected

    lm = LoginManager()

    if not is_connect_internet(testip):
            print("internet_is_not_connect!")
            try:
                print("try_to_login!")
                lm.login(username, password)
            except Exception:
                pass
    else :
        print("internet_is_connected!")
