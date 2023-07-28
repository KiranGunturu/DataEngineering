# List
# lists are slow
# lists occupy more memory as they store datatype, data value , reference and size
# values stored in memory are not contiguous because we can append values to the list
# the reason why it is not contiguous is; lets say have three values in the list and if we want to add 4th element, there is no assurance that someone didnt occupy the memory next to third element
# we can have diff type of values

# Numpy
#  array are faster
# values stored in memory are contiguous
# we cannot alter numpy array rather should create new array
# homogeneous values ; all values should be of same type
# we can try creating array with diff type of values, but all will be converted to higher data type
# ex: a = [[1,2.0,3],[4,5,6]] now the data type of a is float as float can accomdate int too but int cannot accomdate floats
# we can overwrite the elements in array

