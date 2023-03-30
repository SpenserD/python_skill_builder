List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0
for i in List:
  if i % 2 ==0:
    result += i

print(result)


def no_vowel(string):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  result = [letter for letter in string if letter.lower() not in vowels]
  result = " ".join(result)
  print(result)

string = "You are a very annoying human being"
no_vowel(string)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [9, 8, 7, 6, 5, 4]

matches = list(set(list1).intersection(list2))

print(matches)
