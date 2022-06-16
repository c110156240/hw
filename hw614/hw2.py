import pandas as pd
import json
f=open("C:\\Users\\Genuine\\Desktop\\py\\hw614\\test.json","r",encoding="utf-8")
data=json.load(f)
f.close()
tmp=data["records"]
df=pd.DataFrame(tmp)
df2=df[["sitename","pm2.5","aqi","status"]]
gtmp=df2[df2["status"]=="良好"]
a=(gtmp.groupby("status").count()['pm2.5'])
print(a.sort_values())
gtmp1=df2[df2["status"]=="普通"]
a1=(gtmp1.groupby("status").count()['pm2.5'])
print(a1.sort_values())
gtmp2=df2[df2["status"]=="對敏感族群不健康"]
a2=(gtmp2.groupby("status").count()['pm2.5'])
print(a2.sort_values())
gtmp3=df2[df2["status"]=="所有族群不健康"]
a3=(gtmp3.groupby("status").count()['pm2.5'])
print(a3.sort_values())
gtmp4=df2[df2["status"]=="非常不健康"]
a4=(gtmp4.groupby("status").count()['pm2.5'])
print(a4.sort_values())



# print(df2.shape)
