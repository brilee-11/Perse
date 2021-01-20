'''Mark wants to find and print out all of the vowels (aeiou) as they occur in order and including repeats within a 5-letter lower-case word entered by the user.

Input Format
A five-letter lower-case word

Output Format
The vowels as they occur in the input word, one each line.

Example Input

moose
Example Output

o
o
e
'''

input = str(input())

# len(input) == 5

vowels = ["a", "e", "i", "o", "u"]
for i in input:
  if i in vowels:
    print(i)

#correct