man1 = {
    1000: 70, 2000: 87, 3000: 64, 4000: 89
}
man2 = {
    9000: 68, 8000: 76
}
man3 = {
    1:30, 4: 90, 5:40
}

man1.update(man2) # update the dictionary of man2 in man1
print(man1)

man3.clear() # clear the selected dictionary and print the blank dictionary
print(man3)

empt = {} #create a empty dictionary
print(empt)

man3.pop(4) # will clear the key value pair of 4. { marked # clear method to check this}
print(man3)