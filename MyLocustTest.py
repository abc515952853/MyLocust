from locust import HttpLocust, TaskSet, task
import time
import  json 

import GetExcl
import GetImage

import random

class login(TaskSet):
    def on_start(self):
        phonedata =  GetExcl.read_excl().get_excl_data()
        phone = phonedata[random.randint(1,2000)]['phone']#随机获取一个手机号
        # payload = {"Phone":'18506826613',"CodeType":1,"Domain":'sss'}
        # headers = {"Content-Type":"application/json"}
        # self.client.post('api/SMS/Send/Code',data = json.dumps(payload),headers = headers)

        # payload = {"grant_type":'phonecode', "phone": '18506826613',"code":1234}
        # r = self.client.post('api/Token', data = payload)
        # self.session = r.json()["token_type"]+" "+r.json()["access_token"]

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
    host = "http://api.qkt.qianjifang.com.cn/" 
    task_set = login 

    min_wait = 0
    max_wait = 10000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest")