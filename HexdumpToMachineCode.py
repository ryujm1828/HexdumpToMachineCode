with open("dump.txt",'r') as file:
    dump = file.readlines()

s = 0
for i in dump:
    for j in range(len(i)):
        k = j-9
        if(j>=50):
            break
        if((j >=0 and j <=9) or (k%5 == 0)):
            continue
        
        if(s == 0):
            print("\\x"+i[j],end='')
            s = 1
        else:
            print(i[j], end ='')
            s = 0
