def StarPattern(no):
    for i in range(no):
        for i in range(no):
            print('*',end = '  ')
        print()
                
def main():
    print("Enter the number:")
    number=int(input())
    StarPattern(number)
    
if __name__=="__main__":
    main()    
                    
                