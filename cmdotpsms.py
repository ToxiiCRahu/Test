import requests
from requests.structures import CaseInsensitiveDict

number=str(input("Number:- "))
msg=input(" messege:- ")


url = "https://api.hishabexpress.com/login/status"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "msisdn="+number+"&hash="+msg+" verification code. Don't Shear with Anyone"


for i in range(1):
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

