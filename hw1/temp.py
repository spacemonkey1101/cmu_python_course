
def digitCount(n):
    count = 0
    while n > 0:
        n = n//10
        count=count+1
    return count

def main():
    print( digitCount(9))
    print( digitCount(149))
    print( digitCount(14))

if __name__ == "__main__":
    main()


