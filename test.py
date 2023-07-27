# 读取address.txt中的内容，按行分割为ethereum地址，之后从etherscan.io上获取地址的余额，最后将地址与余额写入到result.csv中
import requests
import csv
import time
import random

# 读取secret.txt中内容充当apikey备用
with open('secret.txt', 'r') as f:
    apikey = f.readline()
    # 关闭文件
    f.close()
# 读取address.txt中的内容，按行分割为ethereum地址
with open('address.txt', 'r') as f:
    data = f.readlines()
    # 之后从bscscan.com上获取地址的BNB余额
    for i in data:
        address = i.strip('\n')
        url = 'https://api.bscscan.com/api?module=account&action=balance&address=' + address + '&tag=latest&apikey=' + apikey
        r = requests.get(url)
        # 取出余额
        r = r.json()['result']
        # 将余额转换为BNB
        r = int(r) / 1000000000000000000
        # 最后将地址与余额写入到result.csv中，如果余额大于零则同时写入到result2.csv中
        with open('result.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([address, r])
        # 关闭文件
        f.close()
        if r > 0:
            with open('result2.csv', 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([address, r])
            
            f.close()
        # 随机睡眠
        time.sleep(random.randint(1, 3))