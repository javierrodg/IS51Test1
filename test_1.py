
"""
This program is determining which payment option is better.
The first option is $100 per day for 10 days.
The second option is $1 dollar a day with it being dopubled each day for 10 days.
Two functions will be used to calcluate the pay rate.
Function 1 will calculate the amount for the first option, function 2 will calcluate the amount for the second option.

Function 1 will output 100 * 10 days.
Function 2 will loop 10 times, with each time doubling the amount while adding the amount to the total.

If option 1 is better it will output that option 1 is better.
If option 2 is better it will outout that option 2 is better.

"""

"""
option 1
    return 100 * 1

option 2 
amount = 1
list1 = []
    loop 10 times
    add amount to list1
    amount *= 2
    sum = sum of all items in loop
    return sum

main
var 1 = option1
var2 = option2

if var1 = var2
    "option 1 and option 2 pays the same"
if var1 < var2
    "option 2 is better" 
else
    "Option 1 is better"

main

"""


def option1():
    return 100 * 10


def option2():
    amount = 1
    list1 = []
    for i in range(0, 10):
        list1.append(amount)
        amount *= 2
    total = sum(list1)
    return total


def main():
    answer = ""
    var1 = option1()
    var2 = option2()
    if var1 == var2:
        answer = "Option 1 and Option 2 pays the same."
    elif var1 < var2:
        answer = "Option 2 is better."
    else:
        answer = "Option 1 is better."
    print(answer)


main()
