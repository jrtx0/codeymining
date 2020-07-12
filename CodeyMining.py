# _*_ coding: utf-8 _*_

import requests
import re
import time
import random


# 根据你的用户名和密码修改相应位置的值
username = '####'
password = '####'

def get_formhash():
    mainurl = 'https://bbs.codedy.com/forum.php'
    content = s.get(mainurl) 
    formhash = re.search(r'<input type="hidden" name="formhash" value="(.+?)" />', content.text).group(1)
    return formhash

def get_checkurl():
    t = random.random()
    checkurl = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=' + get_formhash() + '&t=' + str(t)
    return checkurl

def get_signurl():
    t = random.random()
    signurl = 'https://bbs.codedy.com/plugin.php?id=k_misign:sign&operation=qiandao&formhash=' + get_formhash() + '&format=empty&inajax=1&ajaxtarget=JD_sign'
    return signurl

if __name__ == '__main__':
    loginurl = 'https://bbs.codedy.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LAX1v&inajax=1'
    # 这行代码是用来维持cookie的，你后续操作都不用担心cookie，他会自动带上相应的cookie
    s = requests.Session()
    # 带表单的参数
    loginparams = {'username':username, 'password':password}
    s.post(loginurl, data = loginparams)
    # 每日签到
    s.post(get_signurl())
    # 收取挖矿收益
    s.post(get_checkurl())



