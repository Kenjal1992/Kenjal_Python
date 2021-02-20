def CountNumber(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
    
def main():
    print("Enter the number:")
    number=int(input())
    ret=CountNumber(number)
    print("Total Digits are:",ret)
    
if __name__=="__main__":
    main()    
                   