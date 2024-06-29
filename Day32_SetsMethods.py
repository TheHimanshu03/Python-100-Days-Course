s1 = {1,2,3,4}
s2 = {4,5,6,7}
s5 = {4,5}

print(s1.union(s2)) #-> for combining the two sets.
print(s1.intersection(s2)) #-> for finding common values the two sets.
print(s1.symmetric_difference(s2))  #-> for finding the values that are not common.
print(s1.difference(s2)) # for find the values that present in first set but not present in second set.
print(s1.isdisjoint(s2)) # True/False will be given on the basis of common values. ( false = common value) (ture = no common value)
print(s1.issuperset(s2)) #True/False will be given on the basis of all vlaue of s2 is present in s1 or not. 
'''Vice Versa'''

print(s5.issubset(s2)) #True/False will be given on the basis of all vlaue of s2 is present in s1 or not.
s5.add("Himanshu") # to add a value in a set
print(s5)

s5.remove("Himanshu") # to remove a vlaue from set.
print(s5)

s5.discard("Himanshu") 
print(s5)
''' we can use discard also > if the value is not present in set it will not throw error where
remove will throw error'''

s1.update(s2)  #-> update the values of s2 in s1
print(s1)





s3 = {7, 8, 9, 10}
s4 = {5, 6, 7, 8}
print(s4)
print(s4.intersection(s3))  #-> Intersection will not change the value in the default set.
print(s4) 

print(s4.intersection_update(s3))  #-> Intersection_update will  change the value in the default set.
print(s4)


