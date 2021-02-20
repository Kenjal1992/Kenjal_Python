def finding_prime(number):
    count = 0

    for i in range(2, (number//2 + 1)):
        if(number % i == 0):
            count = count + 1
    return count
    
def main():
    num = int(input("enter the number: "))
    cnt = finding_prime(num)
    if (cnt == 0 and num != 1):
        print(" {} is a Prime Number".format(num))
    else:
        print(" {} is not a Prime Number".format(num))

if __name__=="__main__":
    main() 
