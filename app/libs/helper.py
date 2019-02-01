import requests
from flask import current_app


def parse_data(url):
    result = {}
    try:
        if "douyin" in url or "gifshow" in url or "tiktok" in url:
            data = {"url": url}
            res = requests.post(current_app.config['APP886_URL'], data=data).json()
            if res["data"] is not None:
                result["desc"] = res["data"].get("desc", "")
                result["cover"] = res["data"].get("cover", "")
                result["url"] = res["data"].get("dlLink", "")
                return result

        data = {"url": url, "hash": "b11972b879165af4e19630b85d9493aa"}
        res = requests.post(current_app.config['PARSE_URL'], data=data).json()
        if res.get("status", "") == "ok":
            result["desc"] = res["video"][0].get("desc", "")
            result["cover"] = res["video"][0].get("thump", "")
            result["url"] = res["video"][0]["url"]
            return result
        elif "captcha" in res:
            return res

    except Exception as e:
        print("Exception: ", e)
        result = {"status": "参数错误"}
    return result

