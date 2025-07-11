number = [40 , 30, 20, 10  , 50]  # list
my_info = ['John', 25, 'Engineer',28.8]
my_info1 = ['John', 25, 'Engineer',28.8,[40 , 30, 20, 10  , 50]]  # list


# print(number)  # [40, 30, 20, 10, 50]
# print(type(number))  # <class 'list'>   

# buitin functions for list
# print(len(number))  # 5
# print(max(number))  # 50
# print(min(number))  # 10
# print(sum(number))  # 150
# print(sorted(number))  # [10, 20, 30, 40, 50]
# print(sorted(number, reverse=True))  # [50, 40, 30, 20, 10]



# indexing 
# print(number[0])  # 40
# print(number[-1])  # 50
# print(my_info1[4][0])  # 40  

# slicing
# print(number[0:3])  # [40, 30, 20]
# print(number[1:])  # [30, 20, 10, 50]
# print(number[:3])  # [40, 30, 20]
# print(number[-2:])  # [10, 50]

# list methods
# number.append(60)  # add 60 to the end of the list
# print(number)  # [40, 30, 20, 10, 50, 60]
# number.insert(2, 25)  # insert 25 at index 2
# print(number)  # [40, 30, 25, 20, 10, 50, 60]
# # number.insert(6,my_info)  # insert my_info at index 6
# # print(number)  # [40, 30, 25, 20, 10, 50, ['John', 25, 'Engineer', 28.8], 60]
# number.extend(my_info)  # extend the list with my_info
# # print(number)
# number.remove(30)  # remove 30 from the list
# print(number)  # # [40, 20, 10, 50]
# number.pop(0)  # remove the last element from the list
# print(number)  # [20, 10, 50]
# number.clear() # clear the list
# print(number)  # []
# del number[0]  # delete the first element from the list
# print(number)  # [30, 20, 10, 50]
# number.reverse()  # reverse the list
# print(number)  # [50, 10, 20, 30]
# number.sort()   # sort the list
# print(number)  # [10, 20, 30, 50]

# number.index(20)  # find the index of 20 in the list
# print(number)  # 2

# number1 = '-'.join(map(str, number))  # join the list with '-'
# print(number1)  # '10-20-30-50'