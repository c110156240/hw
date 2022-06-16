# https://data.gov.tw/license
import csv
from http.client import responses
import json
import requests
import json
# 匯入json

data={"lang":"tw","type":"2"}
res=requests.get("https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate desc&format=json",params=data)
if res.status_code==200:
    kk=res.content.decode("utf-8")
    tmp=json.loads(kk)
    f=open("C:\\Users\\Genuine\\Desktop\\py\\hw614\\test.json","wb")
    kk1=json.dumps(tmp,indent=5,ensure_ascii=False).encode("utf8")
    f.write(kk1)
    f.close()
