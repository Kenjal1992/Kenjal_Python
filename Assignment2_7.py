def NumberPattern(no):
    for i in range(1,no+1):
        for i in range(1,no+1):
            print(i,end = '  ')
        print()
                
def main():
    print("Enter the number:")
    number=int(input())
    NumberPattern(number)
    
if __name__=="__main__":
    main()    
                    
            