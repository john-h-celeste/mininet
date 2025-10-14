# pandas is the r/matlab of python
# of pandas, matplotlib, and numpy,
# the only one i don't know is pandas

import pandas

df = pandas.DataFrame({
    'Name': [
        'vail, bobby c',
        'celeste, jonathan',
        'march, yan f',
    ],
    'Age': [18, 32, 27],
    'Gender': ['male', 'male', 'female'],
})

print(df) # so coo
print(df['Age'])
print(df['Age'].max())
print(max(df['Age']))
#print(df[0]) # No.
# probably is better to import from csv
# because you don't have to
#   1: repeat field names for every record
#   2: remember field order
#   3: have one array per field

import numpy

arr = numpy.array([[[1, 2, 3],
                    [3, 2, 4]],
                   [[0, 6, 7],
                    [2, 8, 1]]])

print(arr.ndim)
print(arr)
print(arr.shape)

ones = numpy.ones(arr.shape)

s1 = arr + ones
s2 = arr - ones

print(ones)
print(s1)
print(s2)

# how hard would it be for excel to expose graph drawing capabilities?

import matplotlib.pyplot

fig,ax = matplotlib.pyplot.subplots()
ax.plot([1, 2, 3, 4], [1, 3, 4, 2])
matplotlib.pyplot.show()