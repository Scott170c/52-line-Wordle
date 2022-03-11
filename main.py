import color
import sys

word = "hello"
correct_count = 0

def how_many(l:list, char):
  x = 0
  for i in l:
    if i == char:
      x += 1
  return x

def color_word(guess):
  final = ""
  guess_chars = []
  for i in range(5):
    if word[i] == guess[i]:
      final = final + color.green + guess[i] + color.reset
      global correct_count
      correct_count += 1
    elif how_many(list(word), guess[i]) > 1:
      if how_many(guess_chars, guess[i]) >how_many(list(word), guess[i]):
        final = final + color.grey + guess[i] + color.reset
      else:
        final = final + color.yellow + guess[i] + color.reset
    elif guess[i] in word:
      final = final + color.yellow + guess[i] + color.reset
    else:
      final = final + color.grey + guess[i] + color.reset
  return final
    
for i in range(6):
  x = input()
  sys.stdout.write("\033[F") #back to previous line 
  sys.stdout.write("\033[K") #clear line 
  print(color_word(x))
  if correct_count == 5:
    break
  else:
    correct_count = 0

if correct_count == 5:
  print("yay you did it!")
else:
  print("better luck next time! the word was: {}".format(word))
