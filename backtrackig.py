# A O(n^2) time and O(1) space program to find the 
#longest palindromic substring
 
# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome
def longestPalSubstr(string):
    maxLength = 1
 
    start = 0
    length = len(string)
 
    low = 0
    high = 0
 
    # One by one consider every character as center point of 
    # even and length palindromes
    for i in range(1, length):
        # Find the longest even length palindrome with center
    # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
 
        # Find the longest odd length palindrome with center 
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1
 
    print("Longest palindrome substring is:") 
    print (string[start:start + maxLength])
 
    return maxLength

#Esta funcion valida si un elemento es palindromo
def esPalindromo(cadena):
    tam=len(cadena)//2
    comp=cadena[-tam:]
    tmp=comp[::-1]
    if(cadena[:tam]==tmp or len(cadena)==1):
        return True
    else:
        return False


def encontrarPalindromo(cadena):
    vector=""
    return encontrarPalindromo(vector,cadena)

def encontrarPalindromo(vector,cadena):
    if(cadena.length==1):
        vector+=cadena
    elif((cadena.length)/2==0):
        tam=cadena/2
        comparar=cadena[-tam:]
        tmp=comparar[::-1]
        if(cadena[:tam]==tmp):
            vector+=cadena
    else:
        tam=cadena//2
        comparar=cadena[-tam:]
        tmp=comparar[::-1]
        if(cadena[:tam]==tmp):
            vector+=cadena
    return vector

# Driver program to test above functions
string = "forgeeksskeegfor"
print ("Length is: " + str(longestPalSubstr(string)))
print(esPalindromo("tidyit"))

# This code is contributed by BHAVYA JAIN