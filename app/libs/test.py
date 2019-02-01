import requests

data = {"url": "http://v.douyin.com/demDKa/", "hash": "b11972b879165af4e19630b85d9493aa"}
data2 = {"url": "http://www.gifshow.com/s/7pmVRpsi"}
# res = requests.post("https://www.parsevideo.com/api.php", data=data).json()
for i in range(100):
    res = requests.post("https://video.app886.cn/api/v1/single", data=data2).json()
    print(res)
