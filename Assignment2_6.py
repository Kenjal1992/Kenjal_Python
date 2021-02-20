def StarPattern(no):
    for i in range(no+1, 0,-1):    
        for j in range(0, i - 1):  
            print('*', end=' ')  
        print(" ")  
                
def main():
    print("Enter the number:")
    number=int(input())
    StarPattern(number)
    
if __name__=="__main__":
    main()    
          