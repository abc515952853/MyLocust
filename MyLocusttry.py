from locust import HttpLocust, TaskSequence, task,TaskSet,seq_task
 
class ForumPage(TaskSequence):
    @seq_task(1)
    @task(1)
    def read_thread(self):
        print('444')

    @seq_task(2)
    @task(1)
    def new_thread(self):
        print('555')

    @seq_task(3)
    @task(1)
    def stop(self):
        self.interrupt()

class MyTaskSequence(TaskSequence):
    tasks = {ForumPage:1}

    @seq_task(1)
    @task(1)
    def first_task(self):
        for i in range(10):
            self.client.get("/blog?id=%i" % i)

    @seq_task(2)
    @task(1)
    def second_task(self):
        print('222')

    @seq_task(3)
    @task(2)
    def third_task(self):
        print('333')
        
class BestTestIndexUser(HttpLocust):
    host = "https://www.baidu.com/" 

    task_set = MyTaskSequence 

    min_wait = 1000 
    max_wait = 1000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocusttry.py --csv=example --no-web -t1m")