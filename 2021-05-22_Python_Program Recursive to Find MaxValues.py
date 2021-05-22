#python program Recursive to find  Maximum Values
"Computer Programming Tutor, May21,2021 "

def Find_Max_Number(Data,no):
    if (no == 1):
        return Data[0]
    return max(Data[no-1],Find_Max_Number(Data,no-1))

if __name__=="__main__":
    Data = [14,4,19,-6,56,65,-72]
    no=len(Data)
    print("The Maximum Number is: "+str(Find_Max_Number(Data,no)))
    
