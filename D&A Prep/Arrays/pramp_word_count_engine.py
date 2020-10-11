def word_count_engine(document):
  mp = {}
  list = document.split()
  # create hash of unique words, occurence count, min discoverable index
  for i in range(len(list)):
    clean = cleanWord(list[i])
    if clean not in mp:
      mp[clean] = [1, i]
    else:
      mp[clean][0] += 1
      mp[clean][1] = min(mp[clean][1], i)

  ls = []
  for k,v in mp.items():
    item = [k, v[0], v[1]]
    ls.append(item)
  
  # No need to import anything when using lambda functions.
  # Practice different sorting methods
  ls = sorted(ls, key=(lambda x: (x[1], -x[2])), reverse=True)
  # Convert to desired output
  out = map(lambda x: [x[0], str(x[1])], ls)
  print(out)
  return out

          
def cleanWord(word):
  clean = ""
  for w in word.lower():
    if w >= 'a' and w <= 'z':
      clean += w
  return clean

          
doc = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(doc) 

# M be the number of unique words
# O(M * logM) time and O(M) space 