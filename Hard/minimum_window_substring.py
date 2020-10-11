# Intuitive solution would be to use a sliding window

# Expand window with right pointer until the window has all desired characters
# Contract and save smallest window till now, if window is NOT desireable, repeat previous step and expand window
# Answer is the smallest desireable window

# There may be repeats of certain characters within our window, need some way of
#  keeping track of number of repeats we've seen within our window

# 1. for loop for tail ptr inc every round
# 2. once window reached with all desireable chars - USE counter and hashmap to track
# 3. while loop for head ptr to contract window until window ISN'T valid, break out of while loop

# O(N+M) Time and O(M) Space complexity

def get_shortest_unique_substring(arr, str):
  # use 2 ptrs p1, p2
  # p1 is for first char of substr in arr
  # p2 is last char in substr
  
  # check inside inner loop if arr[p1..p2] contains str
  # track min length of valid substr and corresponding p1,p2
  
  head = 0
  res = ""
  counter = 0 # unique counter

  cMap = {}
  # init map to count repeats of char in arr in desired window
  for c in arr:
    cMap[c] = 0
  
  # Expand sliding window
  for tail in range(0, len(str)):
    # skip char not in array
    if str[tail] not in cMap:
      continue
    # update cMap new window vaid
    if cMap[str[tail]] == 0:
      # first occurence, update unique counter
      counter += 1

    cMap[str[tail]] += 1
    
    # check if window is valid, contract window until it isn't
    while(counter == len(arr)):
      windowL = tail - head + 1
      # found unique min in str
      if (windowL == len(arr)):
        return str[head:tail+1]
      
      # update result of min valid window
      if (res == "" or windowL < len(res)):
        res = str[head:tail+1]
      
      # contract window until not valid, update cMap
      if str[head] in cMap:
        hCount = cMap[str[head]] - 1
        if hCount == 0:
          # window no longer valid
          counter -= 1
        cMap[str[head]] = hCount
      
      head += 1
  
  print(res)
  return res
      
  
print('TESTS...') 
print(get_shortest_unique_substring(['x','y','z'], "xyyzyzyx"))

