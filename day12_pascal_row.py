# Pascal's Triangle Row
# Given an integer n, return the nth row of Pascal's triangle as an array.

# In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it.

# Here's the first 5 rows of the triangle:

#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
def pascal_row(n):
    row = [1]
    
    for i in range(1, n):
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(row[j-1] + row[j])
        
        new_row.append(1)
        row = new_row
    
    return row
print(pascal_row(5))
print(pascal_row(3))
print(pascal_row(1))
print(pascal_row(10))