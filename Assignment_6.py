def CheckNumber(no):
    if no>0:
        print("{} is Positive Number".format(no))
        
    elif no<0:
        print("{} is Negative Number".format(no))
        
    else:
        print("{} is Zero".format(no))
        
def main():
    print("Enter the number:")
    n=int(input())   
    CheckNumber(n)

if __name__=="__main__":
    main()    