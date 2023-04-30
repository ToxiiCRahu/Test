import requests
from requests.structures import CaseInsensitiveDict

url = "https://mysms.today/resend/otp"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = """
{
  "mobile": "01870027271",
  "msg": " okay"
}
"""


for i in range(1):
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

