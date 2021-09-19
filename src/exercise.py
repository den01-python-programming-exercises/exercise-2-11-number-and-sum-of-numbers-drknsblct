def main():
    #write your code below this line
    sum = 0
    count = 0
    
    while True:
        num = int(input('Give a number:'))
        
        if num == 0:
            break
            
        count += 1
        sum += num
        
    print('Number of numbers: ' + str(count))
    print('Sum of numbers: ' + str(sum))
    

if __name__ == '__main__':
    main()
