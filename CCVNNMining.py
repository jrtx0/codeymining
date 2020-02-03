# _*_ coding: utf-8 _*_

import requests

# 根据你的用户名和密码修改相应位置的值
username = 'JRTx'
password = '19960321'
loginurl = 'http://bbs.codedy.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'

# 这行代码是用来维持cookie的，你后续操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
# 带表单的参数
loginparams = {'username':username, 'password':password, 'quickforward':'yes'}
# post数据实现登录
r = s.post(loginurl, data = loginparams)
# 验证是否登录成功，抓取首页看看内容
r = s.get(loginurl)
print(r.text)
withdrawUrl = 'http://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=d4c771c8&t=0.7761234471790155'
r = s.post(withdrawUrl)
print("领取收益成功")
