def CheckNum(no): # Always make use of return statement in function
    if no%2==0:
       return True
    else:
       return False
                        
def main():
    print("Enter the number:")
    n=int(input())
    res=CheckNum(n)
    if res==True :
        print("{} is even number".format(n))
    elif res==False:
        print("{} is odd number".format(n))

if __name__=="__main__":
    main()
    
                    