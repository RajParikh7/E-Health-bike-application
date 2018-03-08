# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:42:26 2018

@author: rajpa
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:36:44 2018

@author: rajpa
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:00:27 2018

@author: rajpa
"""

f1=open("2015_raw.csv")
fn=open("2015_unique_2.csv")
f3=open("2015_count.csv","w")
file1=f1.read()
filex=fn.read()
station=[]
location=[]
time=[]
day=[]
count=0
counter=0
lines=file1.split("\n")
linesx=filex.split("\n")
for i in range(len(lines)-1):
    station.append(lines[i].split(",")[0])
    location.append(lines[i].split(",")[1])
    day.append(lines[i].split(",")[2])
    time.append(lines[i].split(",")[3])
counter1=0
k=0

for j in range(len(linesx)-1):
    st=linesx[j].split(",")[0]
    loc=linesx[j].split(",")[1]
    date=linesx[j].split(",")[2]
    tim=linesx[j].split(",")[3]
    count=0
    for i in range(counter,len(lines)-1):
        if (st==station[i]):
            if (loc==location[i]):
                if(date==day[i]):
                    if(tim==time[i]):
                        #print(count)
                        count=count+1
                        counter=counter+1
                    else:
                        f3.write(str(count))
                        f3.write("\n")
                        k=k+1
                        print("inner1")
                        break
                else:
                    f3.write(str(count))
                    f3.write("\n")
                    k=k+1
                    print("inner2")
                    break
            else:
                f3.write(str(count))
                f3.write("\n")
                k=k+1
                print("inner3")
                break
        else:
            f3.write(str(count))
            f3.write("\n")
            k=k+1
            print("inner4")
            break
        
f3.write(str(count))
f1.close()
f2.close()
f3.close()                            

                
     
    
