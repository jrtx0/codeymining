# _*_ coding: utf-8 _*_

import requests
import re
import time
import random


# 根据你的用户名和密码修改相应位置的值
username = '####'
password = '####'
loginurl = 'https://bbs.codedy.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LAX1v&inajax=1'
minerurl = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner'
mainurl = 'https://bbs.codedy.com/forum.php'
checkurl = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=d9d2a125&t=0.33848210890214014'

# 这行代码是用来维持cookie的，你后续操作都不用担心cookie，他会自动带上相应的cookie
s = requests.Session()
# 带表单的参数
loginparams = {'username':username, 'password':password}
# post数据实现登录
s.post(loginurl, data = loginparams)
r = s.get(mainurl)
formhash = re.search(r'<input type="hidden" name="formhash" value="(.+?)" />', r.text).group(1)
t = random.random()
checkurl = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=' + formhash + '&t=' + str(t)
# post数据实现收取金币
s.post(checkurl)
print(checkurl)


