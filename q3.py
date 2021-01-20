'''As a good computer scientist, you always like your shopping list to be printed in exactly the same format with a line of dashes underneath of matching length.

Input the names of 4 food items on separate lines of input.

Output a formatted shopping list which is comma and space separated and exactly underlined in the format:

food1, food2, food3, food4
--------------------------
Input Format
4 words in lower case on separate lines

Output Format
2 lines of text in the form shown above


Example Input

peas
carrots
squash
bread
Example Output

peas, carrots, squash, bread
--------------------------
'''

food = []
for i in range(4):
  food.append(input())
ans = ', '.join(food)
print(ans)
print('-' * len(ans))