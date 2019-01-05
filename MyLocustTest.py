from locust import HttpLocust, TaskSet, task
import time
import  json 

import GetExcl
import GetImage

import random

class MyTest(TaskSet):
    def on_start(self):
        phonedata =  GetExcl.read_excl().get_excl_data()
        self.phone = phonedata[random.randint(1,2000)]['phone']#随机获取一个手机号

        #发送验证码
        payload = {
            "lang":"ZH_CN",
            "token":"awx",
            "version":"222",
            "body":{"mobile":self.phone}
        }
        headers = {"Content-Type":"application/json"}
        r = self.client.post('awx/api/comm/dCaptcha',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.json()["success"] == 'true':
            r.success()
        else:
            r.failure(r.json()['message'])

        #登录
        payload = {
            "lang":"zh_cn",
            "token":"awx",
            "version":"222",
            "body":{
                "accessToken": "X14aerX5hqH7I5GWHPC7WsUiSAoJk0VN",
                "address": "浙江省杭州市滨江区浦沿街道伟业路294号",
                "area": "滨江区",
                "captcha": "9999",
                "city": "杭州市",
                "deviceCode": "",
                "deviceSysVer": "6.0.1",
                "deviceType": "vivo X9i",
                "lat": "30.181118",
                "lng": "120.156818",
                "loginIp": "10.192.108.157",
                "mobile": self.phone,
                "platForm": "2",
                "province": "浙江省",
                "ymToken": "Ar0JCmzzXaIX6Wmh0qwftedY1SyrZB612FZ4ct8IC0if"
            }
        }
        r = self.client.post('awx/api/login/dLogin',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.json()["success"] == 'true': 
            r.success()
            print(r.json()['value']['memberToken'],r.json()['value']['memberId'])  
        else:
            r.failure(r.json()['message'])
            


    def on_stop(self):
        """
        :return:
        """
        
    @task(2)
    def test(self):
        imagedata = GetImage.get_image().chosePic()
        print(imagedata)

    # @task(2)
    # def addclient(self):
    #     headers = {'Content-Type': "application/json",'Authorization':self.session,"Origin":'http://test.qkt.qianjifang.com.cn'}
    #     payload = {"display": "测试客户","phone": "18506826613","level":'' }
    #     r = self.client.post('api/Client', headers = headers,data = json.dumps(payload))
    #     print(r.status_code,r.json())

class BestTestIndexUser(HttpLocust):
    host = "https://api.i5show.cn/" 
    task_set = MyTest 

    min_wait = 0
    max_wait = 10000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest")