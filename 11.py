#python lists

grocery=["powder","toothpaste","dal","chawal","oil"]

print(grocery)
print(grocery[4])
print(grocery[0])

numbers=[2,4,6,8,9,1]

numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[4])


#append
numbers.append(26)
print(numbers)

#inserting
numbers.insert(1,29)
print(numbers)


#remove
numbers.remove(1)
print(numbers)

#pop remove last number
numbers.pop()
print(numbers)