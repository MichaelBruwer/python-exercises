
def wordcrimes(words):
  bleh = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      bleh += 1
  return bleh

print(wordcrimes(['alabama', 'toiletpaper', 'spartans', '404']))
