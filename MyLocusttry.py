from locust import HttpLocust, Locust, TaskSequence, task,TaskSet,seq_task
 
class MyTaskSequence(TaskSequence):
    @seq_task(1)
    @task(1)
    def first_task(self):
        print('111')

    @seq_task(2)
    @task(1)
    def second_task(self):
        print('222')

 
    @seq_task(3)
    @task(1)
    def third_task(self):
        print('333')
        



class BestTestIndexUser(HttpLocust):
    host = "https://www.baidu.com/" 

    task_set = MyTaskSequence 


    min_wait = 1000 
    max_wait = 1000

if __name__ == "__main__":
    import os
    os.system("locust -f MyLocusttry")