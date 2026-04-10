numbers=[1,2,3,4,5,6,7,8,9,10]

#collect all even numbers in new list - using filter

def check_num(number):
    return number%2 ==0 

filter_obj=filter(check_num,numbers)
even_numbers=list(filter_obj)

print(even_numbers)