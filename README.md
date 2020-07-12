# CodeyMining
 自动领取神仙影视社区矿场收益

### Usage
* 修改**CodeyMining.py**文件里面的邮箱和密码，即**username**和**password**参数
* 利用**crontab**来设定每天定时执行一次脚本，在终端输入以下命令：
> crontab -e
* 在打开的文件末尾添加如下指令，命令的含义为：在每天六点零一分的时候运行一次sign.py脚本：
>  01 06 * * * python3 CodeyMining.py

### Contribute
You are welcome to make code contributions.
