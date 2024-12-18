# For Arbitary Arguments in the Function.
def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num
    
    print(f"Numbers Additions Are: {result}")
    

find_sum(4, 6, 8)
find_sum(8, 7)