# 3. Find all of the numbers from 1-1000 that are divisible by 7

elem_divisible_by_seven = [elem for elem in range(1, 1001) if elem % 7 == 0]
print(elem_divisible_by_seven)

# 4. Find all of the numbers from 1-1000 that have a 3 in them

elem_has_three = [elem for elem in range(1, 1001) if "3" in str(elem)]
print(elem_has_three)