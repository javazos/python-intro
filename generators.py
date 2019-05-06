def square_numbers(nums):
    # result=[]
    # for i in nums:
    #     result.append(i*i)
    # return result
    for i in nums:
        yield i*i
# my_nums = square_numbers([1,2,3,4,5])
# print(next( my_nums))
# print(next( my_nums))
# print(next( my_nums))
# print(next( my_nums))
# print(next( my_nums))

#list comprehension
my_nums = [x*x*x for x in [1,2,3,4,5]]
for num in my_nums:
    print(num)

my_nums = (x*x*x for x in [1,2,3,4,5])
print(my_nums)
print(list(my_nums))

for num in my_nums:
    print(type(num))
    print(num)

print(my_nums)
print(list(my_nums))

