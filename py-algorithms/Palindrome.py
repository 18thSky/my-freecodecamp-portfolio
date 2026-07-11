def ispalindrome(word):
    if not isinstance(word, str):
        return 'Input must be text'
    elif len(word) == 0:
        return 'Cannot be empty'
    
    word = word.lower()
    reversed_word = word[[:-1]]

    return word == reversed_word

print("This is palindrome tester program")
user_guess = input("Enter the word to check palindrome")

result = ispalindrome(user_guess)

if result == True:
    print (f"Test Passed: 'user_guess' IS a palindrome")
elif result == False:
    print (f"Test Failed: 'user_guess' IS not a palindrome")
else:
    print(result)