import Arithmatic

def main():
    print("Enter 1st number:")
    n1=int(input())
    print("Enter 2nd number:")
    n2=int(input())
    ret=Arithmatic.Addition(n1,n2)
    print("Addition is:",ret)
    ret1=Arithmatic.Subtraction(n1,n2)
    print("Subtraction is:",ret1)   
    ret2=Arithmatic.Multiplication(n1,n2)
    print("Multiplication is:",ret2)    
    ret3=Arithmatic.Division(n1,n2)
    print("Division is:",ret3)    
    
#code starter
if __name__=="__main__":
  main()    