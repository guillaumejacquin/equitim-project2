
from pandas import array


initial = 100
pas = 0.5
debut = 4
total = 100
max = 64

array_month = []
array_value = []
for i  in range(0, total):
    array_month.append(i)
    if (i >= debut):
        value_total = total - pas * (i - debut)

        if (value_total >= max):
            array_value.append(value_total)
        else:
            array_value.append(max)
    else:
        array_value.append("/NA")


print(array_month)
print(array_value)