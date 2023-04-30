import requests
from requests.structures import CaseInsensitiveDict

Number=str(input("Enter Your Number-: "))
messege=input(" Enter Your Messege:- ")

url = "https://mysms.today/resend/otp"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = '{"mobile": "'+Number+'","msg": "'+messege+'"}'




for i in range(1):
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

