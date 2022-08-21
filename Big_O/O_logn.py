#Binary search tree
#N log n 

def binary(array, min, max, looking_for):

    middle = min+max //2
    if looking_for == array[middle]:
        return print(f'{looking_for} found in position {middle}')
    
    elif looking_for < array[middle]:
        binary(array, min, middle-1, looking_for)

    else:
        binary(array, middle, max, looking_for)
    
arr = [ 2, 3, 4, 10, 40 ]
looking_for = 10

binary(arr, 0 , len(arr), looking_for)