# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:00:27 2018

@author: rajpa
"""

f1=open("2015_raw.csv")
f2=open("2015_unique.csv")
f3=open("2015_count.csv","w")
file1=f1.read()
file2=f2.read()
station=[]
location=[]
time=[]
day=[]
count=0
counter=0
lines=file1.split("\n")
lines2=file2.split("\n")
for i in range(len(lines)-1):
    station.append(lines[i].split(",")[0])
    location.append(lines[i].split(",")[1])
    day.append(lines[i].split(",")[2])
    time.append(lines[i].split(",")[3])
counter1=0
k=0

for j in range(k,len(lines2)-1):
    st=lines2[j].split(",")[0]
    loc=lines2[j].split(",")[1]
    date=lines2[j].split(",")[2]
    tim=lines2[j].split(",")[3]
    count=0
    for i in range(counter,len(lines)-1):
        if (st==station[i]):
            if (loc==location[i]):
                if(date==day[i]):
                    if(tim==time[i]):
                        print(count)
                        count=count+1
                        counter=counter+1
                    else:
                        f3.write(str(count))
                        f3.write("\n")
                        k=k+1
                        break
                else:
                    f3.write(str(count))
                    f3.write("\n")
                    k=k+1
                    break
            else:
                f3.write(str(count))
                f3.write("\n")
                k=k+1
                break
        else:
            f3.write(str(count))
            f3.write("\n")
            k=k+1
            break
        

f1.close()
f2.close()
f3.close()                            

                
     
    
