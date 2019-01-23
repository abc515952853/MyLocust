from locust import HttpLocust, TaskSet, task
import time
import  json 

import GetExcl
import GetImage

import random

class MyTest(TaskSet):
    def on_start(self):
        userdata = self.locust.userdatas.pop(1)
        self.phone = str(userdata["phone"])
        self.mpno = str(userdata["mpno"])
        self.memberToken = ''
        self.LogIn()

    #创建说说
    @task(1)
    def test_CheckCaptcha(self):
        self.CheckCaptcha()


    #验证验证码
    def CheckCaptcha(self):
        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"ZH_CN",
            "token":"slowshot",
            "version":"1.0.0",
            "body":{
                "mobile":self.phone,
                "captcha":"9999"
            }
        }
        r = self.client.post('api/comm/dCheckCaptcha',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功':
                r.success()
            else:
                r.failure(r.json()['message'])
                
        else:
            r.failure("HTTP状态码"+str(r.status_code))


    #登录  
    def LogIn(self):
        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"zh_cn",
            "token":"slowshot",
            "version":"1.0.0",
            "body":{
                "accessToken":"db20a5ccf7ab11e886e8ec0d9a2fab3e",
                "deviceSysVer":"12.0",
                "mobile":self.phone,
                "province":"浙江省",
                "area":"滨江区",
                "platForm":"1",
                "deviceType":"iPhone 6s",
                "lat":"30.180773",
                "address":"浙江省杭州市滨江区伟业路靠近杭州高新软件园",
                "city":"杭州市",
                "mpNo":self.mpno,
                "loginIp":"127.0.0.1",
                "lng":"120.157041",
                "ymToken":"751cecb07399dfc426d57903b299997cc2405abd06e8338fb6b4247762b449f1",
                "deviceCode":"B2D75656-7718-48F4-A5D2-9D1C0AFCB418"
            }
        }
        r = self.client.post('api/login/dLogin',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功':
                r.success()
                self.memberToken = r.json()['value']['memberToken']
            else:
                r.failure(r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))

class BestTestIndexUser(HttpLocust):
    host = "https://apit.lutuapp.com/slowshot-api/" 

    data =  GetExcl.read_excl().get_excl_data()
    userdatas = []
    for i in range(len(data)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        userdatas.append(data[i])

    task_set = MyTest 

    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f LocustForMp")