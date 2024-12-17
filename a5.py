'''
Write a Python program to compute the following operations on String:
a) To display the word with the longest length
b) To determine the frequency of occurrence of a particular character in the string
c) To check whether the given string is a palindrome or not
d) To display the index of the first appearance of the substring
e) To count the occurrences of each word in a given string
'''

def longest_word(s):
    word = ''
    longest = ''
    max_length = 0
    for ch in s:
        if ch != ' ':
            word+= ch
        else:
            if len(word) > max_length:
                longest = word
                max_length = len(longest)
            word = '' 

    if len(word) > max_length:
                longest = word
                max_length = len(longest)

    print(f"The longest word in the string is \"{longest}\" with a length of {len(longest)}")

def find_freq(s):
    print("Find the character whose frequency you need to find")
    ch = input()
    count = 0
    for char in s:
        if char == ch:
            count +=1
    
    print(f"The frequency of the character \'{ch}\' is {count}")

def check_palindrome(s):
    new_str = s[::-1]
    if(new_str == s):
        print("The given string is palindrome")
    else :
        print("The string is not palindrome")

def substring_index(s):
    index = -1
    print("Enter the substring to find : ")
    substring = input()
    for i in range(0, len(s) - len(substring) + 1):
        if s[i:i+len(substring)] == substring:
            index = i
    
    if(index==-1) : 
        print("The substring was not found")
    else : 
        print("The substring was found at index :" +str(index))

def word_occurences(s):
    word_check = {}
    word = ''
    for ch in s:
        if ch != ' ':
            word+= ch
        else:
            if word in word_check:
                word_check[word] +=1
            else:
                word_check[word] = 1
            word = ''
            
    # to check for the last word, because if string doesnt end in space, that last word gets stored in the word variable
    if word in word_check:
        word_check[word] +=1
    else:
         word_check[word] = 1
        
    for w,o in word_check.items():
        print(f"The occurence of {w} in the string is {o}")



def main():
    while True:
        print("\n------------------- MENU -------------------")
        print("1. Display the word with the longest length")
        print("2. Determine the frequency of a particular character")
        print("3. Check whether the given string is a palindrome")
        print("4. Display the index of the first appearance of a substring")
        print("5. Count the occurrences of each word in the string")
        print("6. Exit")
        print("Enter your choice (1-6): ")
        choice = input()
        print("\n")

        if choice == '6':
            print("Exiting the program.")
            break

        str = input("Enter a string: ")

        if choice == '1':
            longest_word(str)
        elif choice == '2':
            find_freq(str)
        elif choice == '3':
            check_palindrome(str)
        elif choice == '4':
            substring_index(str)
        elif choice == '5':
            word_occurences(str)
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
