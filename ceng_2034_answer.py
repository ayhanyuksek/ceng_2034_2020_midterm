#! /usr/bin/python3
import os, threading,requests

print("PID of script is: ",os.getpid())



def url_arr(aList):
    
    avg = os.getloadavg()
    print("loadavg is: ",avg)
    
    cpu= os.cpu_count()
    print("5 min loadavg value and cpu core count are: ",avg[1],"and",cpu )
    if((cpu - avg[1])<1):
        exit()


    r = requests.get(aList, auth=("user","pass"))
    r.status_code
    print("Status of url: ",r.status_code)    
    if(r.status_code == 200):
        print("url is working.")
    else:
        print("url is not working.")
    
    


arr = ["https://api.github.com​"," http://bilgisayar.mu.edu.tr/​","https://www.python.org/​","http://akrepnalan.com/ceng2034​","https://github.com/caesarsalad/wow​"]







thread1 = threading.Thread(target=url_arr, args=(arr[0],))
thread2 = threading.Thread(target=url_arr, args=(arr[1],))
thread3 = threading.Thread(target=url_arr, args=(arr[2],))
thread4 = threading.Thread(target=url_arr, args=(arr[3],))
thread5 = threading.Thread(target=url_arr, args=(arr[4],))
    

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()



