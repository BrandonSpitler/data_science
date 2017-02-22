import csv
import numpy

def type_convert(type,value):
    if (type == 's'):
        return (value)
    elif (value == 'NA'):
        return(None)
    elif (type == 'i'):
        return int(value)
    elif (type == 'f'):
        return float(value)
    return 1

housing_data_file = open('../train.csv')
housing_Data = csv.reader(housing_data_file)
i = 0
header = next(housing_Data)
data = list(housing_Data)
header_length = len(header)

rows_to_keep = [4,12,80,77]
length_of_rows_to_keep = len(rows_to_keep)
conversion_array = ['i','s','i','s']
length_of_data = len(data)

data_file = numpy.empty((length_of_data,length_of_rows_to_keep), dtype = numpy.object)

for i in range(0,length_of_data):
    for n in range(0,length_of_rows_to_keep):
       index = rows_to_keep[n]
       converter = type_convert(conversion_array[n],data[i][index])
       data_file[i][n] = converter

print("done")

