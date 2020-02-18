import re
import pandas as pd
import numpy as np

ipaddress,date,request,status,size,refer,info = [],[],[],[],[],[],[]
Wrongline = 0
path = r'E:\log\localhost_access_log..2019-02-01.txt'
with open(path, 'r') as f:
    for Eachline in f.readlines():
        if Eachline != '':
            line = re.match(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}|-) - - \[(\d{2}/[A-Za-z]*/\d{4}):(\d{2}:\d{2}:\d{2}) \+\d{4}\] "(.*)" (\d{3}) (\d*|-) "([a-zA-z]+://*|[A-Z0-9\.]*|blank|-)" "(.*)"',Eachline) 
            if line:
                ipaddress.extend([line.group(1)])
                date.extend([line.group(2) + ' ' + line.group(3)])#pd.to_datetime()
                request.extend([line.group(4)])
                status.extend([line.group(5)])
                size.extend([line.group(6)])
                refer.extend([line.group(7)])
                info.extend([line.group(8)])
            else:
                #print(Eachline)
                Wrongline  = Wrongline + 1
res = pd.DataFrame({'ip': ipaddress, 'time': date, 'request': request, 'status': status, 'size': size, 'refer': refer, 'info': info})
print(res)
print(Wrongline)
print(res['ip'].value_counts())
                
                
