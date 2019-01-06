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
            self.memberToken = r.json()['value']['memberToken']
            self.memberId = r.json()['value']['memberId']
        else:
            r.failure(r.json()['message'])

        self.shuoshuo = 1
        self.xiangce = 1
            


    def on_stop(self):
        """
        :return:
        """
        
    # @task(2)
    # def test(self):
    #     imagedata = GetImage.get_image().chosePic()
    #     print(imagedata)

    # #创建说说
    # @task(2)
    # def HomePublish(self):
    #     img = ''
    #     for i in range(random.randint(1,9)):
    #         img = img+ "http://i5show.oss-cn-beijing.aliyuncs.com/test/BinTest/D{0}.jpg,".format(random.randint(1,9))

    #     headers = {"Content-Type":"application/json"}
    #     payload = {
    #         "lang":"zh_cn",
    #         "token":"awx",
    #         "version":"222",
    #         "body":{
    #             "memberToken": self.memberToken,
    #             "memberId":self.memberId,
    #             "content":"说说"+str(self.shuoshuo),
    #             "imgs":img,
    #             "city":"杭州",
    #             "area":"上城"

    #         }
    #     }
    #     r = self.client.post('awx/api/home/dHomePublish',data = json.dumps(payload),headers = headers,catch_response = True)
    #     if r.json()["success"] == 'true': 
    #         r.success()
    #         self.shuoshuo = self.shuoshuo +1
    #     else:
    #         r.failure(r.json()['message'])

    @task(1)
    def PhotoPublish(self):
        Photo = [{"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=1&json=i5show/user/data/502022/491028329057.json","shareImg":"https://thirdwx.qlogo.cn/mmopen/vi_32/IsGYtTAciawr1iaQMuSAicZ1Ptdib7ujGroJ9rVZMZKamo2wRqTVfS6gB2RXDXS36d5jBZBD7N04drqo8EWjia7WF6A/132?x-oss-process=image/resize,m_fill,h_80,w_80"},
        {"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=3&json=i5show/user/data/502022/426442241.json","shareImg":"https://h5.i5show.cn/i5show/user/album/502022/803436953973.jpg?x-oss-process=image/resize,m_fill,h_80,w_80"},
        {"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=2&json=i5show/user/data/502022/201567293432.json","shareImg":"https://h5.i5show.cn/i5show/user/album/502022/12702501352.jpg?x-oss-process=image/resize,m_fill,h_80,w_80"}]

        Pohotoinfo = Photo[random.randint(0,2)]

        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"zh_cn",
            "token":"awx",
            "version":"222",
            "body":{
                "memberToken": self.memberToken,
                "memberId":self.memberId,
                "title":"相册"+str(self.xiangce),
                "link":Pohotoinfo["link"],
                "city":"杭州",
                "area":"上城",
                "shareImg":Pohotoinfo["shareImg"]
            }
        }
        r = self.client.post('awx/api/photo/dPhotoPublish',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.json()["success"] == 'true': 
            r.success()
            self.xiangce = self.xiangce +1
        else:
            r.failure(r.json()['message'])
   

class BestTestIndexUser(HttpLocust):
    host = "https://api.i5show.cn/" 
    task_set = MyTest 

    min_wait = 0
    max_wait = 10000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest")