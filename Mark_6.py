import random   #randomly genenrated number
import time     #time for showing the result


#generate list of non-repeated numbers
def generate_result (number, max_input):
    result = []
    i = 0
    
    while (i < number):
        repeated = 0
        result.append(random.randint(1, max_input))
        
        for j in range(0, i):
            if (result[i] == result[j]):
                repeated = 1
                break
                
        if(repeated):
            result.pop(i)
            continue
        
        i += 1

    result.sort()
    return result


#ask for user input, check for repeated or larger than maximum or wrong type
def input_number (number, max_input):
    input_number = []
    i = 0
    repeated = 0
    

    while (i < number):
        repeated = 0
        print("Please enter", i+1, "of", number, "number ( 1 ~", max_input, ")")

        wrong_type = 1
        while (wrong_type):
            try:
                input_number.append(int(input()))
                wrong_type = 0
            except ValueError:
                print("**Please enter a number within 1 ~", max_input,"\n")
        
        for j in range(0, i):
            if (input_number[i] == input_number[j]):
                repeated = 1
                break

        if(repeated):
            input_number.pop(i)
            print("**The number you've entered is in the list already!\n")
            continue

        if(input_number[i] > max_input or input_number[i] < 1):
            input_number.pop(i)
            print("**Please enter a number within 1 ~", max_input,"\n")
            continue
        
        print("\n")
        i += 1
        
    input_number.sort()
    return input_number


#check and return number of match(es)
def result_checking (input_number, result, input_amount, draw_amount):

    match = 0

    for i in range(0,input_amount):
        for j in range(0, draw_amount):
            if(input_number[i] == result[j]):
                match += 1

    return match


#main body
def main():

    input_amount = 6
    draw_amount = input_amount
    maximum_number = 49
    
    input_no = []
    result = []
    
    input_no = input_number(input_amount, maximum_number)
    result = generate_result(draw_amount, maximum_number)

    print("You've chosen:", input_no)
    print("Numbers drawn:", result)
    print("Number of matches:",result_checking(input_no, result, input_amount, draw_amount))

    time.sleep(5)


main()
