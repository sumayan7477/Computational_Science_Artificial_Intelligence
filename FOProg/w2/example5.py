word = "progsamming" # this contains a mistake

begin = word[:4] # 'prog'
end = word[5:] # 'amming'

new_word = begin + "r" + end

print(new_word)


s1 = input("Enter the first string:")
s2 = input("Enter the Second string:")

#Full logic

# lengthS1 = len(s1)
# halfL = int(lengthS1/2)

# begin = s1[:halfL]
# end = s1[halfL:]

# newWord = begin + s2 + end
# print(newWord)


# Short hand for faster result
mid = int(len(s1)//2)
print(f"{s1[:mid]}{s2}{s1[mid:]}")
