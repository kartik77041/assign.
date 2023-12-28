#time complexity is O(n)
#space comlexity is O(n)
def separate_duplicates(nums):
    d = {}
    duplicates = []
    non_duplicates = []

    for num in nums:
        if d.get(num):
            duplicates.append(num)
            d[num] = d[num] + 1
        else:
            non_duplicates.append(num)
            d[num] = 1

    return duplicates, non_duplicates

integer_list = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 1, 9, 10, 10]
duplicates, non_duplicates = separate_duplicates(integer_list)
non_duplicates =  set(non_duplicates).difference(set(duplicates))

print("Duplicates:", duplicates)
print("Non-duplicates:", non_duplicates)

#time complexity is O(nlog(n))
#space complexity is O(1)
i_lt = [1, 2, 3, 2, 4, 5, 3, 6, 7, 8, 1, 9, 10, 10]
i_lt.sort()
a = integer_list[0]
d = [] #duplicate
n_d = [] #nonduplicate element
for i in range(1,len(integer_list)-1):
    if(i_lt[i] == i_lt[i-1] or i_lt[i+1] == i_lt[i]):
        d.append(i_lt[i])
n_d = list(set(i_lt).difference(set(d)))
print(d)
print(n_d)