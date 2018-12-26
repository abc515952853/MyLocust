from locust import HttpLocust, TaskSet, task
import time


class login(TaskSet):
    def on_start(self):
        self.a = 1

    def on_stop(self):
        print('aaaaaaaaaaaaaaaa')
    
    def getphone(self):
        print('1850368265')

    @task(2)
    def index1(self):
        self.client.get('/')
        print(self.a)
        print(self.locust.b)
        self.a = self.a+1

    @task(1)
    def index2(self):
        self.client.get('/')
        print('2222222222222')

  
class BestTestIndexUser(HttpLocust):
    host = "https://wwww.baidu.com" 
    #这个类继承了HttpLocust，代表每个并发里面的每个用户
    b ='111'
    print('hahahah')
    task_set = login #这个是每个用户都去干什么，指定了BestTest这个类，它就会每个用户去运行besttest这个类里面的方法

    min_wait = 0
    max_wait = 0

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocustTest")