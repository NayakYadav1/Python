def area_of_rectangle(length = 1, width = 1):
    return length * width

no_arg = area_of_rectangle()
len_arg = area_of_rectangle(length=5)
wid_arg = area_of_rectangle(width=4)
rectangle = area_of_rectangle(length=5, width=4)

print('No argument:', no_arg)
print('Length argument:', len_arg)
print('Width argument:', wid_arg)
print('Length and width arguments:', rectangle)