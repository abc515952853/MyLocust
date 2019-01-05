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
            "body":{"mobile":self.phone}
        }
        headers = {"Content-Type":"application/json"}
        r = self.client.post('awx/api/comm/dCaptcha',data = json.dumps(payload),headers = headers)


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