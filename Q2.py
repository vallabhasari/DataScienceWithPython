my_str = "Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

#Sort the list dictionary case-insensitive
#words.sort(key = lambda x: x.lower())

#remove the duplicates
#Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
#words = list(dict.fromkeys(words))

# display the sorted words

print("The sorted words are:")
for word in words:
  print(word)