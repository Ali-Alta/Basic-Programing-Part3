def palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    print(palindrome("civic"))       # True
    print(palindrome("katak"))       # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu"))   # False
    print(palindrome("lion"))        # False