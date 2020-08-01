# _*_ coding: utf-8 _*_

import requests
import re
import time
import random

# 根据你的用户名和密码修改相应位置的值
username = '####'
password = '####'

login_url = 'https://bbs.codedy.com/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LAX1v&inajax=1'

def extract_formhash():
    home_page = 'https://bbs.codedy.com/forum.php'
    content = session.get(home_page)
    formhash = re.search(r'<input type="hidden" name="formhash" value="(.+?)" />', content.text).group(1)
    return formhash

def join_checkurl():
    t = random.random()
    url = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=draw&formhash=' +\
               extract_formhash() + '&t=' + str(t)
    return url

def join_signurl():
    t = random.random()
    url = 'https://bbs.codedy.com/plugin.php?id=k_misign:sign&operation=qiandao&formhash=' +\
              extract_formhash() + '&format=empty&inajax=1&ajaxtarget=JD_sign'
    return url

def join_refresh():
    t = random.random()
    url = 'https://bbs.codedy.com/plugin.php?id=hux_miner:hux_miner&ac=re&formhash=' +\
            extract_formhash() + '&t=' + t
    return url

def main():
    # 这行代码是用来维持cookie的，你后续操作都不用担心cookie，他会自动带上相应的cookie
    global session
    session = requests.Session()
    # 带表单的参数
    login_params = {'username': username, 'password': password}
    session.post(login_url, login_params)
    time.sleep(3)

    # 每日签到
    session.post(join_signurl())
    time.sleep(2)

    # 刷新挖矿收益
    sessiom.post(join_refresh())
    time.sleep(2)

    # 收取挖矿收益
    session.post(join_checkurl())

if __name__ == '__main__':
    main()



