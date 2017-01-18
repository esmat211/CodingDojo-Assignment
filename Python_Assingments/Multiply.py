


array = [2,4,10,16]
def multiply(array):
    for i in range(len(array)):
        array[i] = array[i] * 5
    return array

newarray = multiply(array)
print newarray
