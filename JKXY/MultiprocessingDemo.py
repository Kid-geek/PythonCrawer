from multiprocessing.dummy import Pool as ThreadPool
import threading
import requests
import time

def getsource(url):
    global hasViewed
    print(url)
    html=requests.get(url)
    hasViewed.append(url)

def threadGetSource(url):
    print(url)
    x=threading.Thread(target=getsource,args=(url,))
    x.start()

urls=[]
hasViewed=[]

for i in range(1,21):
    newpage='http://tieba.baidu.com/p/3522395718?pn={}'.format(i)
    urls.append(newpage)

#  =======单线程=======
time1=time.time()
hasViewed=[]
for i in urls:
    getsource(i)
print('单线程耗时:{}'.format(time.time()-time1))


# ========Multiprocessing.dumpy多线程========
pool =ThreadPool(20)
time2=time.time()
hasViewed=[]
results=pool.map(getsource,urls)
pool.close()
pool.join()
print('并行耗时:{}'.format(time.time()-time2))
