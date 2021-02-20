def Addition(no1,no2): # Always make use of return statement in function
    return no1+no2
    
                        
def main():
    print("Enter the first number:")
    n1=int(input())
    print("Enter the second number:")
    n2=int(input())
    res=Addition(n1,n2)
    print("Addition is:",res)
   
if __name__=="__main__":
    main()