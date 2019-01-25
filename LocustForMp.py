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
        self.activityphontophontoid = ''
        self.activityid = ''
        #登录
        self.LogIn()

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


    # #同步检测报告
    # @seq_task(3)
    # @task(1)
    # def test_SyncReport(self):
    #     self.SyncReport()

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

    # ##########################################################相册###########################################################
    #首页-慢拍列表
    @task(1)
    def test_PhotoList(self):
        self.PhotoList()

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
                    "city":"杭州市",
                    "currentPage":""
                }
            }
            r = self.client.post('api/photo/qList',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
                    print(r.json())
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
        if len(self.activityphontophontoid) > 0:
            headers = {"Content-Type":"application/json"}
            payload = {
                "lang":"ZH_CN",
                "token":"slowshot",
                "version":"1.0.0",
                "body":{
                    "memberToken":self.memberToken,
                    "memberId":self.memberid,
                    "activityId":self.activityphontoactivityid,
                    "photoId":self.activityphontophontoid
                }
            }
            r = self.client.post('api/activity/dPhotoVote',data = json.dumps(payload),headers = headers,catch_response = True)
            if r.status_code == 200:
                if r.json()["code"] == '200' and r.json()["message"] == '成功': 
                    r.success()
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
            "body":""
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
        if r.status_code == 200:
            if r.json()["code"] == '200' and r.json()["message"] == '成功':
                r.success()
                userdata = {"memberToken":r.json()['value']['memberToken'],"memberId":r.json()['value']['memberId']}
                self.locust.memberinfo.append(userdata)
                num = random.randint(0,len(self.locust.memberinfo)-1)
                self.memberToken = self.locust.memberinfo[num]["memberToken"]
                self.memberid = self.locust.memberinfo[num]["memberId"]
                print(self.memberToken,self.memberid,self.phone)
            else:
                r.failure(r.json()['code']+','+r.json()['message'])
        else:
            r.failure("HTTP状态码"+str(r.status_code))

class BestTestIndexUser(HttpLocust):
    host = "https://apit.lutuapp.com/slowshot-api/" 
    accessToken = 'db20a5ccf7ab11e886e8ec0d9a2fab3e'

    data =  GetExcl.read_excl().get_excl_data()
    memberinfo = []
    userdatas = []
    user = []
    activity = []
    activityphonto = []
    for i in range(len(data)):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        userdatas.append(data[i])

    task_set = MyTest 

    min_wait = 1000
    max_wait = 3000

if __name__ == "__main__":
    import os
    os.system("locust -f LocustForMp")