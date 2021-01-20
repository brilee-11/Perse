'''Most starfish have five eyes. Most spiders have eight eyes. Most scorpions have twelve eyes! Input the number of each in the room and output the number of eyes on you.

Input Format
Three non-negative whole numbers on separate lines to represent the number of starfish, spiders and scorpions respectively that are present.

Output Format
A single number representing the number of eyes.

Constraints

Each input n will be a whole number, 0 <= n <= 1000
Example Input

3
1
2
Example Output

47
'''


a=5
b=8
c=12

st = int(input())
sp = int(input())
sc = int(input())

output = ((st*a) + (sp*b) + (sc*c))

print(output)