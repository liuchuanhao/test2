#encoding: utf-8
from flask import jsonify

class HttpCode(object):
    ok = 200
    unautherror = 401
    paramserror = 400
    servererror = 500

def restful_result(code,message,data):
    return jsonify({"code":code,"message":message,"data":data or {}})

def success(message="",data=None):
    return restful_result(code=HttpCode.ok,message=message,data=data)

def unauth_error(message=""):
    return restful_result(code=HttpCode.unautherror,message=message,data=None)

def params_error(message=""):
    return restful_result(code=HttpCode.paramserror,message=message,data=None)

def server_error(message=""):
    return restful_result(code=HttpCode.servererror,message=message or '服务器内部错误',data=None)


"""## 返回值的规范：
```json
{
    "code":200,
    "message": "",
    "data":{
        "name":'xxx',
        "age":'xxx'
    }
}
```

## 状态码的规范：
1. 200：成功。
2. 401：没有授权。
3. 400：参数错误。
4. 500：服务器错误。"""