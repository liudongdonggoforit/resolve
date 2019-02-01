from app.web import web
from flask import request, jsonify
from app.libs.helper import parse_data
import redis
from resolve import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()

r = redis.StrictRedis(host=current_app.config["REDIS_HOST"], port=current_app.config["REDIS_PORT"], password=current_app.config["REDIS_PASSWORD"], db=current_app.config["REDIS_DB"], socket_timeout=3000)


@web.route("/v1.0/resolve/")
def get_parse():
    ip = request.remote_addr
    print(ip)
    ip_count = r.get(ip)
    print(ip_count)
    if not ip_count:
        r.set(ip, 1)
        r.expire(ip, current_app.config["TIME_LIMIT"])
    else:
        r.incr(ip)
        if int(ip_count) > current_app.config["IP_LIMIT"]:
            return jsonify({'code': 401, 'status': "reach the ip limit", 'message': 'error'})
    url = request.args.get("url")
    result = parse_data(url)
    return jsonify(result)
