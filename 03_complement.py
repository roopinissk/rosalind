'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
'''

# solution

dna = ("AAAACCCGGT")

complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

reverse = "".join(complement[char]for char in dna)[::-1]
print(reverse)