# -*- coding: utf-8 -*-
"""Q4_StringBruteForceAlgo_Iqubal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tojK2yFDUWGnxYfOMw2ybNs_dfwanzGt
"""

class palindrome :
    def  getPalindromeCount(s) : # function for getting the palindrime count
        count = 0 # count is for countig the word
        i = 0
        while (i < len(s)) :
            hash = [0] * (26) # 26 letter in the aplhabet
            count += 1
            # since 1 character is palindrome anyway
            j = i + 1
            while (j < len(s)) :
                hash[ord(s[j]) - ord('a')] += 1
                if (palindrome.palindromePossible(hash)) :
                    count += 1
                j += 1
            i += 1
        return count
        
    def  palindromePossible(hash) : # possible palindrome
        odd_count = 0
        i = 0
        while (i < len(hash)):
            if (hash[i] % 2 != 0):
                odd_count += 1
            i += 1
        return odd_count < 2

    def main(args) :
        print(palindrome.getPalindromeCount(input()))
    
# Driver code:
pl = palindrome()
pl.main()

