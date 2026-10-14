import psutil 
#print(psutil.cpu_percent(interval=1)) gives current cpu percentage

#for i in range (5): checks the cpu percent 5 times loop with 1 sec of interval
   # print(psutil.cpu_percent(interval=1))

threshold = float(input("enter your threshold: ")) # takes threshold input from user and check 5 times in 1sec interval if cpu% > threshold gives unhealthy
for i in range(5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("unhealthy")
    else:
        print("healthy")