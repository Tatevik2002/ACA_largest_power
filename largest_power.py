number = int(input())

def number_try(number):
    if number %3 == 0:
        number = number / 3
        if number == 1:
            return(True)
        else:
            number_try(number)
    
    else:
        return(None)

while number != 0:
    copy_of_number = number
    if number_try(number) == True:
        print(copy_of_number)
        break
    else:
        number= number -1
 
