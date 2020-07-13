# Calculate the sum of an array which contains integers and other arrays with integers. For example:
#
# array_sum([1,2,[3,4,[5]]])
# would return 15.


def calculate_sum(array):
    sum = 0
    for element in array:
        if isinstance(element, list):
            sum = sum + calculate_sum(element)
        else:
            sum += element

    return sum


print(calculate_sum([1,2,[3,4,[5]]]))