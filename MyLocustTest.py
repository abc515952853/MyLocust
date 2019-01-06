from locust import HttpLocust, TaskSet, task
import time
import  json 

import GetExcl
import GetImage

import random

class MyTest(TaskSet):
    def on_start(self):
        self.phone = self.locust.phones.pop(1)#获取一个手机号

        # #发送验证码
        # payload = {
        #     "lang":"ZH_CN",
        #     "token":"awx",
        #     "version":"222",
        #     "body":{"mobile":self.phone}
        # }
        # headers = {"Content-Type":"application/json"}
        # r = self.client.post('awx/api/comm/dCaptcha',data = json.dumps(payload),headers = headers,catch_response = True)
        # if r.json()["success"] == 'true':
        #     r.success()
        # else:
        #     r.failure(r.json()['message'])

        #登录
        headers = {"Content-Type":"application/json"}
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
            member = {"memberToken":r.json()['value']['memberToken'],"memberId":r.json()['value']['memberId']}
            self.locust.memberinfo.append(member)
        else:
            r.failure(r.json()['message'])
            print(self.phone)

        self.shuoshuo = 1
        self.xiangce = 1
            


    # def on_stop(self):
    #     """
    #     :return:
    #     """
        
    # @task(1)
    # def test(self):
    #     imagedata = GetImage.get_image().chosePic()
    #     print(imagedata)

    # #创建说说
    # @task(1)
    # def HomePublish(self):
    #     img = ''
    #     for i in range(random.randint(1,9)):
    #         img = img+ "http://i5show.oss-cn-beijing.aliyuncs.com/test/BinTest/D{0}.jpg,".format(random.randint(1,9))

    #     num = random.randint(0,len(self.locust.memberinfo)-1)
    #     headers = {"Content-Type":"application/json"}
    #     payload = {
    #         "lang":"zh_cn",
    #         "token":"awx",
    #         "version":"222",
    #         "body":{
    #             "memberToken": self.locust.memberinfo[num]["memberToken"],
    #             "memberId":self.locust.memberinfo[num]["memberId"],
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

    # #创建相册
    # @task(1)
    # def PhotoPublish(self):
    #     Photo = [{"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=1&json=i5show/user/data/502022/491028329057.json","shareImg":"https://thirdwx.qlogo.cn/mmopen/vi_32/IsGYtTAciawr1iaQMuSAicZ1Ptdib7ujGroJ9rVZMZKamo2wRqTVfS6gB2RXDXS36d5jBZBD7N04drqo8EWjia7WF6A/132?x-oss-process=image/resize,m_fill,h_80,w_80"},
    #     {"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=3&json=i5show/user/data/502022/426442241.json","shareImg":"https://h5.i5show.cn/i5show/user/album/502022/803436953973.jpg?x-oss-process=image/resize,m_fill,h_80,w_80"},
    #     {"link":"https://h5.i5show.cn/test/H5/pages/album/album.html?templateId=2&json=i5show/user/data/502022/201567293432.json","shareImg":"https://h5.i5show.cn/i5show/user/album/502022/12702501352.jpg?x-oss-process=image/resize,m_fill,h_80,w_80"}]

    #     Pohotoinfo = Photo[random.randint(0,2)]
                        
    #     num = random.randint(0,len(self.locust.memberinfo)-1)
    #     headers = {"Content-Type":"application/json"}
    #     payload = {
    #         "lang":"zh_cn",
    #         "token":"awx",
    #         "version":"222",
    #         "body":{
    #             "memberToken": self.locust.memberinfo[num]["memberToken"],
    #             "memberId":self.locust.memberinfo[num]["memberId"],
    #             "title":"相册"+str(self.xiangce),
    #             "link":Pohotoinfo["link"],
    #             "city":"杭州",
    #             "area":"上城",
    #             "shareImg":Pohotoinfo["shareImg"]
    #         }
    #     }
    #     r = self.client.post('awx/api/photo/dPhotoPublish',data = json.dumps(payload),headers = headers,catch_response = True)
    #     if r.json()["success"] == 'true': 
    #         r.success()
    #         self.xiangce = self.xiangce +1
    #     else:
    #         r.failure(r.json()['message'])

    #家人圈列表
    @task(1)
    def HomeList(self):
        num = random.randint(0,len(self.locust.memberinfo)-1)

        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"zh_cn",
            "token":"awx",
            "version":"222",
            "body":{
                "type":random.randint(1,3),
                "memberId":self.locust.memberinfo[num]["memberId"],
                "currentPage":""
            }
        }
        r = self.client.post('awx/api/home/qHomeList',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.json()["success"] == 'true': 
            r.success()
            self.homeids = []
            for i in range(len(r.json()["value"])):
                self.homeids.append(r.json()["value"][i]["homeId"])
            print(self.homeids)
               
        else:
            r.failure(r.json()['message'])
   

class BestTestIndexUser(HttpLocust):
    host = "https://api.i5show.cn/" 
    
    phonedata =  GetExcl.read_excl().get_excl_data()
    phones = []
    memberinfo = []
    for i in range(len(phonedata)):
        phones.append(str(phonedata[i]["phone"]))
    task_set = MyTest 


    min_wait = 5000
    max_wait = 10000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest")