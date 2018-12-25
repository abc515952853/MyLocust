from locust import HttpLocust, TaskSet, task
 
class BestTest(TaskSet):
    def on_start(self):
        self.a = 1
    #自己定义的类，继承TaskSet，也就是这个类是实现咱们要去请求什么的
    @task(1)#用task装饰器把这个函数装饰成一个咱们要执行的性能任务
    def index(self):#这个函数里面定义的是咱们要具体做的操作
        self.client.get('/')#请求这个url里面的哪个路径，如果是接口的话，就是哪个接口
        print(self.a)
        print(self.locust.b)
        self.a = self.a+1
  
class BestTestIndexUser(HttpLocust):
    host = "https://wwww.baidu.com" 
    #这个类继承了HttpLocust，代表每个并发里面的每个用户
    b ='111'
    print('hahahah')
    task_set = BestTest #这个是每个用户都去干什么，指定了BestTest这个类，它就会每个用户去运行besttest这个类里面的方法

    min_wait = 0
    max_wait = 1000