def SumOfDigits(n):
    sum = 0
    while (n != 0):  
        sum = sum + (n % 10) 
        n = n//10
    return sum
    
def main():
    print("Enter the number:")
    number=int(input())
    ret=SumOfDigits(number)
    print("Sum of Digits is:",ret)
    
if __name__=="__main__":
    main()    
            