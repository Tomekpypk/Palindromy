def palindrome(word):
    word = word.replace(" ", "").lower()  
    return word == "".join(reversed(word)) 

word1 = "potop"
word2 = "kajak"
word3 = "programowanie"

print(word1, word2, word3)
print(palindrome(word1))
print(palindrome(word2))
print(palindrome(word3))

