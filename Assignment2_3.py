def Factorial(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
        
    return fact
         
    
def main():
    print("Enter the number:")
    number=int(input())
    ret=Factorial(number)
    print("Factorial is ",ret)
    
if __name__=="__main__":
    main()  
 
 