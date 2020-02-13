# _*_ coding: utf-8 _*_

import requests
import re
import time


# 根据你的用户名和密码修改相应位置的值
username = 'JRTx'
password = '19960321'
loginurl = 'http://bbs.codedy.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

# 这行代码是用来维持cookie的，你后续操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
# 带表单的参数
loginparams = {'username':username, 'password':password}
# post数据实现登录
s.post(loginurl, data = loginparams)
# 验证是否登录成功，抓取首页看看内容
r = s.get(loginurl)
print(r.text)
time.sleep(1)
# withdrawUrl = 'http://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=d4c771c8&t=0.11143162409816232'

# withdrawUrl = 'http://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=c30ada4a&t=0.4462692100109882'

# withdrawUrl = 'http://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=c30ada4a&t=0.3032894840180431'
withdrawUrl = 'http://bbs.codedy.com/plugin.php''
# r = s.post(withdrawUrl)
# print(r.content)
