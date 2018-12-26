from locust import HttpLocust, TaskSet, task
import time
import  json  


class login(TaskSet):
    def on_start(self):
        payload = {"Phone":'18506826613',"CodeType":1,"Domain":'sss'}
        headers = {"Content-Type":"application/json"}
        self.client.post('api/SMS/Send/Code',data = json.dumps(payload),headers = headers)

        payload = {"grant_type":'phonecode', "phone": '18506826613',"code":1234}
        r = self.client.post('api/Token', data = payload)
        print(r.status_code,r.json())

    def on_stop(self):
        """
        :return:
        """
    
    @task(2)
    def index1(self):
        """
        :return:
        """

class BestTestIndexUser(HttpLocust):
    host = "http://api.qkt.qianjifang.com.cn/" 
    task_set = login 

    min_wait = 0
    max_wait = 0

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest1")