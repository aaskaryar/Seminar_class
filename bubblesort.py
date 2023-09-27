import time

def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        print(list)
        time.sleep(1)

list = [14,46,43,27,57,41,45,21,70]
print("Original list:", list)
bubbleSort(list)
print("Sorted list:", list)
