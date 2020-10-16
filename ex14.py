def gargle(meh):
  bleh = 0

  for meh in meh:
    if len(meh) > 1 and meh[0] == meh[-1]:
      bleh += 1
  return bleh

print(gargle(['alabama', 'toiletpaper', 'spartans', '404']))
