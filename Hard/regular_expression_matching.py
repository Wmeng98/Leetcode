# Also seen on pramp as - Basic Regex Parser

'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

'''

# Ignoring the Kleene star, our algorithm can be implemented recursivey like so...
def isMatch(text, pattern):
    # base case where pattern is empty str
    if pattern == "":
        if text == "":
            # text matches pattern
            return True
        else:
            return False
    
    # compare first char of text/pattern match and recurse on the rest
    firstMatch = False if text == "" else pattern[0] in {'.', text[0]} # first char of pattern either wildcard or matches text
    # recurse on substrs
    
    # RECALL: slicing outside the bounds of a sequence (at least for built-ins) doesn't cause an error
    return firstMatch and isMatch(text[1:], pattern[1:])

print('Wildcard only func test:', isMatch('abc', 'a.c'))
print('Wildcard only func test:', isMatch('abc', 'a..c'))


'''
p = .*b
      |    
t = ab
     |


True and    
'''

# Now include Kleene Star into recursive solution for Regex Parsing

# Ignoring the Kleene star, our algorithm can be implemented recursivey like so...
def isMatch2(text, pattern):
    # base case where pattern is empty str
    # print(text,pattern)
    if pattern == "":
        if text == "":
            # text matches pattern
            return True
        else:
            # print('not match', text, pattern)
            return False
    
    # compare first char of text/pattern match and recurse on the rest
    firstMatch = bool(text) and pattern[0] in {'.', text[0]} # first char of pattern either wildcard or matches text
    
    # Recurse on substrs

    # NEW - Need to consider if the next char is a Kleene Star
    if len(pattern) > 1 and pattern[1] == '*':
        # can branch into 2 recursive checks

        # either take first match and constrain text
        # or ignore pattern[0]
        return (firstMatch and isMatch2(text[1:], pattern)) or isMatch2(text, pattern[2:])
    else:        
        # RECALL: slicing outside the bounds of a sequence (at least for built-ins) doesn't cause an error
        return firstMatch and isMatch2(text[1:], pattern[1:])

print('Regex only func test:', isMatch2('abc', 'a*c'))
print('Regex only func test:', isMatch2('abc', 'a.*c'))
print('Regex only func test:', isMatch2('abdfsfsdfc', 'a.*c'))
print('Regex only func test:', isMatch2('abdfsfsdfc', 'a.*e'))

'''

a.*c
    |
abc
   |

'''

'''

[DYNAMIC PROGRAMMING APPROACH]

Finally, we can observe that the problem has an optimal substructure
Optimal substructure being that optimal sol'n to problem can be obtained by using optimal sol'n to its subproblems

Natural to cache intermediate results - easiest to memoize rather than tabulate

dp(i,j) - asks the question whether text[i:] and pattern[j:] match?

We can describe our answer in terms of answers to questions involving smaller things

Recursive + Memoize: Top-down DP!!!

Time: O(TP)
      Work for every call dp(i,j) is done once and is O(1) work
Space: O(TP) boolean entries in our stack + recrusive stack frames

'''
def isMatch3(text, pattern):
    memo = {} # store tuple (i,j) as the key
    def dp(i,j):
        # check if already computed
        if (i,j) not in memo:
            # if reach end of pattern
            # print('i,j: ',i, j)
            if j >= len(pattern):
                ans = i == len(text)
            else:
                firstMatch = i < len(text) and pattern[j] in {text[i], '.'}
                if j < len(pattern) - 1 and pattern[j+1] == '*':
                    ans = dp(i,j+2) or (firstMatch and dp(i+1,j))
                else:
                    ans = firstMatch and dp(i+1,j+1)
            memo[i,j] = ans

        return memo[i,j]
    
    return dp(0,0)

print('DP func test:', isMatch3('abc', 'a*c'))
print('DP func test:', isMatch3('abdfsfsdfc', 'a.*c'))
print('DP func test:', isMatch3('abdfsfsdfc', 'a.*e'))
print('DP func test:', isMatch3('abdfsfsdfc', 'a.*'))