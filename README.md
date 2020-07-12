# CodeyMining
 自动领取神仙影视社区矿场收益

### Usage
使用之前必须先修改**CodeyMining.py**的用户名和密码，即**username**和**password**参数。之后便可以利用**crontab**来设定每天定时执行一次脚本，例如每天六点零一分的时候运行一次脚本：
> crontab -e
* 在打开的文件末尾添加如下指令
>  01 06 * * * python3 CodeyMining.py

### Contribute
欢迎贡献你的代码。
