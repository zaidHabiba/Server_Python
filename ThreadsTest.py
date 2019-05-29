import threading,time


class Counter(threading.Thread):

    def __init__(self,Couter):
        threading.Thread.__init__(self)
        self.Couter=Couter
    def run(self):
        while(True):
            print("From Thread :"+str(self.Couter))
            self.Couter+=1
            time.sleep(1.5)


count=Counter(10)
count.start()
Couter=0
i=0
while(i<10):
    print("Main :"+str(Couter))
    Couter+=1
    time.sleep(1.5)
    i+=1