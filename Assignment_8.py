def Divisibility(no): # Always make use of return statement in function
    if no%5==0:
       return True
    else:
       return False
                        
def main():
    print("Enter the number:")
    n=int(input())
    res=Divisibility(n)
    if res==True :
        print("{} is divisible by 5".format(n))
    elif res==False:
        print("{} is not divisible by 5".format(n))

if __name__=="__main__":
    main()
    
    