from locust import HttpLocust, TaskSet, task,TaskSequence,seq_task
import time
import  json 

import GetExcl
import GetImage

import random

class MyTest(TaskSequence):
    def on_start(self):
        userdata = self.locust.userdatas.pop(-1)
        self.phone = str(userdata["phone"])
        self.mpno = str(userdata["mpno"])
        self.memberToken = ''
        self.userid = ''
        self.yonghu = 1
        self.ncdw = 1
        self.sqnr = 1
        self.pinglun = 1
        self.activityphontophontoid = ''
        self.activityid = ''
        self.photolistId = ''
        self.photoid = ''
        self.manpai = 1
        self.delphotoimgphotoid = ''
        self.delphotoimgvalue = {}

        self.dddzzz = []

        self.currentPage = 1

        self.dianzan = 99

        self.num = 1
        # memberinfodata = self.locust.memberinfo1.pop(0)
        # self.memberToken = memberinfodata["memberToken"]
        # self.memberid = memberinfodata["memberId"]

        # # # #登录
        # self.LogIn()

    # #登录
    # @task(1)
    # def test_LogIn(self):
    #     self.LogIn()

    # ##########################################################基础接口###########################################################
    # #验证验证码
    # @task(1)
    # def test_CheckCaptcha(self):
    #     self.CheckCaptcha()

    # #获取基础数据    
    # @task(1)
    # def test_BaseData(self):
    #     self.BaseData()


    # #慢拍号列表
    # @task(1)
    # def test_Number(self):
    #     self.Number()

    # #获取用户基本信息
    # @task(1)
    # def test_UserInfo(self):
    #     self.UserInfo()

    # #系统礼物数据接口
    # @task(1)
    # def test_Gift(self):
    #     self.Gift()

    # #版本检测接口
    # @task(1)
    # def test_CheckAccess(self):
    #     self.CheckAccess()

    # #查询闪新闻-慢动态的消息数据
    # @task(1)
    # def test_Message(self):
    #     self.Message()


    # #删除消息数据（红点/黄点）
    # @task(1)
    # def test_CancelMessage(self):
    #     self.CancelMessage()

    # ##########################################################健康检测###########################################################
    # #添加成员
    # @seq_task(1)
    # @task(1)
    # def test_AddUser(self):
    #     self.AddUser()

    # #选择成员列表
    # @seq_task(2)
    # @task(1)
    # def test_UserList(self):
    #     self.UserList()


    # # #同步检测报告
    # # @seq_task(3)
    # # @task(1)
    # # def test_SyncReport(self):
    # #     self.SyncReport()

    # #报告列表
    # @seq_task(4)
    # @task(1)
    # def test_ReportList(self):
    #     self.ReportList()

    # #成员告列表
    # @seq_task(3)
    # @task(1)
    # def test_UserReportList(self):
    #     self.UserReportList()

    # ##########################################################个人中心###########################################################
    # #我的慢拍
    # @task(1)
    # def test_MyPhoto(self):
    #     self.MyPhoto()

    # #我的更多慢拍
    # @task(1)
    # def test_MyPhotoMore(self):
    #     self.MyPhotoMore()

    # #慢拍和粉丝统计
    # @task(1)
    # def test_MyPhotoStatistics(self):
    #     self.MyPhotoStatistics()

    # #消息列表
    # @task(1)
    # def test_MessageList(self):
    #     self.MessageList()  

    # #修改我的资料
    # @task(1)
    # def test_ModifyMyInfo(self):
    #     self.ModifyMyInfo()  

    # ##########################################################活动###########################################################

    # #活动列表
    # @seq_task(2)
    # @task(1)
    # def test_ActivityList(self):
    #     self.ActivityList()

    # #活动详情-慢拍列表
    # @seq_task(3)
    # @task(1)
    # def test_ActivityPhotos(self):
    #     self.ActivityPhotos()

    # #活动详情-慢拍投票
    # @seq_task(4)
    # @task(1)
    # def test_PhotoVote(self):
    #     self.PhotoVote()

    # #活动详情-h5
    # @seq_task(3)
    # @task(1)
    # def test_ActivityDetailH5(self):
    #     self.ActivityDetailH5()

    # #活动慢拍详情-h5
    # @seq_task(3)
    # @task(1)
    # def test_ActivityPhotosH5(self):
    #     self.ActivityPhotosH5()

    # #活动列表
    # @task(1)
    # def test_Apply(self):
    #     self.Apply()

    #########################################################相册###########################################################
    # #首页-慢拍列表
    # @task(1)
    # def test_PhotoList(self):
    #     self.PhotoList()

    # #慢拍详情
    # @task(1)
    # def test_PhotoDetail(self):
    #     self.PhotoDetail()

    # #慢拍的图片列表
    # @task(2)
    # def test_PhotoImgs(self):
    #     self.PhotoImgs()

    # #点赞
    # @task(1)
    # def test_PhotoParise(self):
    #     self.PhotoParise()

    # #评论
    # @task(1)
    # def test_PhotoComment(self):
    #     self.PhotoComment()

    # #评论列表
    # @task(1)
    # def test_CommentList(self):
    #     self.CommentList()

    # #记录用户浏览的慢拍
    # @task(1)
    # def test_Browse(self):
    #     self.Browse()

    #创建慢拍
    @task(2)
    def test_CreatePhoto(self):
        self.CreatePhoto()
    
    # #删除慢拍
    # @task(1)
    # def test_DelPhoto(self):
    #     self.DelPhoto()

    # #删除慢拍图片
    # @task(1)
    # def test_DelPhotoImg(self):
    #     self.DelPhotoImg()

    # #修改图片
    # @task(1)
    # def test_ModifyCover(self):
    #     self.ModifyCover()

    # #修改图片标题
    # @task(1)
    # def test_ModifyImgTitle(self):
    #     self.ModifyImgTitle()


    # @task(1)
    # def test_test(self):
    #     print("111")


    ##########################################################实现函数###########################################################
    #修改图片标题
    def ModifyImgTitle(self):
        if len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "photoId":self.photolistId,
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "img":self.delphotoimgvalue
                }
            }
            r = self.client.post('api/photo/dModifyImgTitle',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #修改图片
    def ModifyCover(self):
        if len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "coverSecond":"第二句话"+str(self.manpai),
                    "photoId":self.photolistId,
                    "coverThree":"第三句话"+str(self.manpai),
                    "province":"浙江",
                    "deviceType":"iPhone 6s",
                    "title":"一个标题"+str(self.manpai),
                    "memberId":self.memberid,
                    "city":"杭州",
                    "cover":"test/BinTest/D1.jpg",
                    "coverFirst":"第一句话"+str(self.manpai),
                    "memberToken":self.memberToken,
                }
            }
            r = self.client.post('api/photo/dModifyCover',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
        
    #删除慢拍图片
    def DelPhotoImg(self):
        if len(self.delphotoimgphotoid)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "photoId":self.delphotoimgphotoid,
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "img":self.delphotoimgvalue
                }
            }
            r = self.client.post('api/photo/dDelImg',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #删除慢拍
    def DelPhoto(self):
        if len(self.photoid)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken, 
                    "memberId":self.memberid,
                    "photoId":self.photoid
                }
            }
            r = self.client.post('api/photo/dDelPhoto',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #创建慢拍
    def CreatePhoto(self):
        if self.num <= 30:#len(self.memberToken)>0 and self.num <= 30:
            headers = {"Content-Type":"application/json"}
            img = [
                    {
                        "img":"default/photo/D3.jpg",
                        "title":"",
                        "width":"100",
                        "height":"102",
                        "deviceType":"iPhone 6s"
                    },
                    {
                        "img":"default/photo/D4.jpg",
                        "title":"",
                        "width":"100",
                        "height":"102",
                        "deviceType":"iPhone 6s"
                    },
                    {
                        "img":"default/photo/D5.jpg",
                        "title":"",
                        "width":"100",
                        "height":"102",
                        "deviceType":"iPhone 6s"
                    },
                    {
                        "img":"default/photo/D6.jpg",
                        "title":"",
                        "width":"100",
                        "height":"102",
                        "deviceType":"iPhone 6s"
                    },
                    {
                        "img":"default/photo/D7.jpg",
                        "title":"",
                        "width":"100",
                        "height":"102",
                        "deviceType":"iPhone 6s"
                    }
                ]
            imgs = []
            for i in range(100):
                for ii in range(len(img)):
                    imgs.append(img[ii])
            area = ['杭州','宁波','温州','绍兴','湖州','嘉兴','金华','衢州','台州','丽水','舟山']
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "coverSecond":"第二句话"+str(self.manpai),
                    "photoId":"",
                    "coverThree":"第三句话"+str(self.manpai),
                    "province":"浙江",
                    "link":"",
                    "deviceType":"iPhone 6s",
                    "title":"一个标题"+str(self.manpai)+"#最美家乡评选#",
                    "memberId":'10606',#self.memberid,
                    "city":area[random.randint(0,10)],
                    "cover":"default/photo/D6.jpg",
                    "coverFirst":"第一句话"+str(self.manpai),
                    "memberToken":'d420ed9442b948172544ab70c1e44fb0',#self.memberToken,
                    "imgs":imgs
                }
            }
            r = self.client.post('api/photo/dCreatePhoto',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.manpai = self.manpai + 1
                    self.num = self.num +1
                    self.photoid = r.json()["value"]["photoId"]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
            


    #记录用户浏览的慢拍
    def Browse(self):
        if len(self.photolistId)>0:
            photolistIds = []
            photolistIds.append(self.photolistId)
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "photoIds":self.photolistId,
                    "memberId":self.memberid
                }
            }
            r = self.client.post('api/photo/dBrowse',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success() 
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #评论列表
    def CommentList(self):
        if len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "currentPage":"1",
                    "photoId":self.photolistId
                }
            }
            r = self.client.post('api/photo/qCommentList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success() 
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
        
    #评论
    def PhotoComment(self):
        if self.num <2:#len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "photoId":'455251',#self.photolistId,
                    "comments":"评论"+str(self.pinglun)
                }
            }
            r = self.client.post('api/photo/dComment',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success() 
                    self.pinglun = self.pinglun + 1
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #点赞
    def PhotoParise(self):
        if  self.num <2:#len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            memberid = self.memberid
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":memberid,
                    "photoId":'455251'#self.photolistId
                }
            }
            r = self.client.post('api/photo/dParise',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
    
    #慢拍的图片列表
    def PhotoImgs(self):
        if len(self.photolistId)>0:
            photolistId = self.photolistId
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "currentPage":"",
                    "photoId":photolistId

                }
            }
            r = self.client.post('api/photo/qImgs',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.delphotoimgphotoid = photolistId
                    self.delphotoimgvalue= r.json()["value"][0]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #慢拍详情   
    def PhotoDetail(self):
        if len(self.photolistId)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "photoId":self.photolistId,
                }
            }
            r = self.client.post('api/photo/qDetail',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))


    #首页-慢拍列表
    def PhotoList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "city":"台州",
                    "currentPage":"100"#str(random.randint(1,100))
                }
            }
            r = self.client.post('api/photo/qList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    if len(r.json()["value"])>0:
                        self.locust.photo=r.json()["value"]  
                        num = random.randint(0,len(self.locust.photo)-1)
                        self.photolistId = self.locust.photo[num]["photoId"]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
    
    def Apply(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "content":"测试申请内容"+str(self.sqnr),
                    "mobile":self.phone
                }
            }
            r = self.client.post('api/activity/dApply',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.sqnr = self.sqnr + 1
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    def ActivityPhotosH5(self):
        if len(self.activityid) > 0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "activityId":self.activityid,
                }
            }
            r = self.client.post('api/activity/qPhotosH5',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
            
    #活动详情-h5
    def ActivityDetailH5(self):
        if len(self.activityid) > 0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "activityId":self.activityid,
                }
            }
            r = self.client.post('api/activity/qDetailH5',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #活动详情-慢拍投票
    def PhotoVote(self):
        if self.num<=1:#len(self.activityphontophontoid) > 0,:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "activityId":'2',#self.activityphontoactivityid,
                    "photoId":'455240'#self.activityphontophontoid
                }
            }
            r = self.client.post('api/activity/dPhotoVote',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.num = self.num + 1
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #活动详情-慢拍列表
    def ActivityPhotos(self):
        if len(self.activityid) > 0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "activityId":self.activityid,
                    "search":"",
                    "currentPage":""
                }
            }
            r = self.client.post('api/activity/qPhotos',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.locust.activityphonto=r.json()["value"]
                    if len(self.locust.activityphonto)>0:
                        num = random.randint(0,len(self.locust.activityphonto)-1)
                        self.activityphontoactivityid = self.locust.activityphonto[num]["activityId"]
                        self.activityphontophontoid = self.locust.activityphonto[num]["photoId"]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #活动列表
    def ActivityList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "accessToken":self.locust.accessToken,
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "search":"",
                    "currentPage":""
                }
            }
            r = self.client.post('api/activity/qList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.locust.activity=r.json()["value"]  
                    num = random.randint(0,len(self.locust.activity)-1)
                    self.activityid = self.locust.activity[num]["activityId"]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #修改我的资料
    def ModifyMyInfo(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "avatar":"2",
                    "nickName":"昵称"+str(self.ncdw),
                    "family":"地位"+str(self.ncdw),
                    "ymToken":"751cecb07399dfc426d57903b299997cc2405abd06e8338fb6b4247762b449f1"
                }
            }
            r = self.client.post('api/member/dModifyMyInfo',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.ncdw = self.ncdw +1
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #消息列表
    def MessageList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "type":"2"
                }
            }
            r = self.client.post('api/member/qMessage',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #慢拍和粉丝统计
    def MyPhotoStatistics(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "currentPage":""
                }
            }
            r = self.client.post('api/member/qMyPhotoStatistics',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
    


    #我的更多慢拍
    def MyPhotoMore(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "currentPage":""
                }
            }
            r = self.client.post('api/member/qMyPhotoMore',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #我的慢拍
    def MyPhoto(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                }
            }
            r = self.client.post('api/member/qMyPhoto',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
        

    #成员告列表
    def UserReportList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "currentPage":""
                }
            }
            r = self.client.post('api/health/qUserReportList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))


    #报告列表
    def ReportList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "userId":self.userid,
                    "currentPage":""
                }
            }
            r = self.client.post('api/health/qReportList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))
        
    #同步成员检测报告
    def SyncReport(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "body":{
                    "userId":self.userid,
                    "link":"http://qianketong.cd641dc781add4bc6b8ed119cee669cb7.cn-hangzhou.alicontainer.com/testingResult/79276e015f804122a0796c9551b5a2ad"
                }
            }
            r = self.client.post('api/health/dSyncReport',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))


    #选择成员列表
    def UserList(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "currentPage":""
                }
            }
            r = self.client.post('api/health/qUserList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.locust.user=r.json()["value"]
                    num = random.randint(0,len(self.locust.user)-1)
                    self.userid = self.locust.user[num]["userId"]
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #添加成员
    def AddUser(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "name":'测试用户'+str(self.yonghu),
                    "sex":"1",
                    "birth":"2018-11-11"
                }
            }
            r = self.client.post('api/health/dAddUser',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    self.yonghu = self.yonghu + 1
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #删除消息数据（红点/黄点）
    def CancelMessage(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberId":self.memberid,
                    "type":1
                }
            }
            r = self.client.post('api/comm/dCancelMessage',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #查询闪新闻-慢动态的消息数据
    def Message(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberId":self.memberid
                }
            }
            r = self.client.post('api/comm/qMessage',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #版本检测接口
    def CheckAccess(self):
        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"ZH_CN",
            "token":"slowshot",
            "version":"1.0.0",
            "body":{
                "accessToken":self.locust.accessToken,
                "platForm":"ios"
            }
        }
        r = self.client.post('api/comm/dCheckAccess',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                r.success()
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))

    #系统礼物数据接口
    def Gift(self):
        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"ZH_CN",
            "token":"slowshot",
            "version":"1.0.0",
            "body":{}
        }
        r = self.client.post('api/comm/qGift',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                r.success()
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))

    #获取用户基本信息
    def UserInfo(self):
        if len(self.memberToken)>0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "accessToken":self.locust.accessToken,
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                }
            }
            r = self.client.post('api/comm/qUserInfo',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                else:
                    r.failure(r.json()['code']+','+r.json()['message'])
            else:
                r.failure("HTTP状态码"+str(r.status_code))

    #慢拍号列表 
    def Number(self):
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
        r = self.client.post('api/comm/qNumber',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                r.success()
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))
        
    #获取基础数据    
    def BaseData(self):
        headers = {"Content-Type":"application/json"}
        payload = {
            "lang":"ZH_CN",
            "token":"slowshot",
            "version":"1.0.0",
            "body":{
                "type":"family"
            }
        }
        r = self.client.post('api/comm/qBaseData',data = json.dumps(payload),headers = headers,catch_response = True)
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功':
                r.success()
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))

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
                r.failure(r.json()['code']+','+r.json()['message'])
                
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
                "accessToken":self.locust.accessToken,
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
        self.locust.num1.append('1')
        print(len(self.locust.num1))
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功':
                r.success()
                userdata = {"memberToken":r.json()['value']['memberToken'],"memberId":r.json()['value']['memberId']}
                self.locust.memberinfo.append(userdata)

                # #随机获取手机号
                # num = random.randint(0,len(self.locust.memberinfo)-1)
                # self.memberToken = self.locust.memberinfo[num]["memberToken"]
                # self.memberid = self.locust.memberinfo[num]["memberId"]

                # 不重复获取
                memberinfo = self.locust.memberinfo.pop(0)
                self.memberToken = memberinfo["memberToken"]
                self.memberid = memberinfo["memberId"]

                # print(self.phone,self.memberToken)
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
                # print(self.phone,self.mpno,self.memberToken,self.memberToken)       
        else:
            r.failure("HTTP状态码"+str(r.status_code))
            

class BestTestIndexUser(HttpLocust):
    host = "https://api.manpai.club/slowshot/" 
    accessToken = 'db20a5ccf7ab11e886e8ec0d9a2fab3e'

    data =  GetExcl.read_excl().get_excl_data()
    memberinfo = []
    userdatas = []
    user = []
    activity = []
    activityphonto = []
    photo = []

    num1 = []

    memberinfo1 = [
        {"memberToken":"264642847ed57f6f3c14a476f6b666bc","memberId":"3030"},
    ]

    for i in range(len(data)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        userdatas.append(data[i])

    task_set = MyTest 

    min_wait = 2000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f LocustForMp")