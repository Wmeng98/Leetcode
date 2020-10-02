# Prison Break
#  
# Find the largest area created in the cell after removing horz and vert rods

# Solution: Find the longest seq of rods removed from horz * longest seq of rods removed from vert
# Time O(n+m) Space O(1)

def find_max_gap(size, rods):
    # track curr gap, max gap, and prev rod removed
    prev = -1
    curr = 1 # by default
    max_gap = curr

    for i in rods:
        # inc to curr gap if prev rod was also removed
        if i - 1 == prev:
            curr += 1
            max_gap = max(max_gap, curr)
        else:
            # reset to track start of new gap
            curr = 2
            max_gap = max(max_gap, curr)
        prev = i
    return max_gap

def max_area(n, m, rows, cols):
    # print('max gap rows', find_max_gap(n, rows),'max gap cols', find_max_gap(m, cols))
    return find_max_gap(n, rows) * find_max_gap(m, cols)


print(max_area(5,5,[],[])) # 1
print(max_area(5,5,[1],[1])) # 4
print(max_area(5,5,[0,1],[1])) # 6
print(max_area(5,5,[0,1],[])) # 3
print(max_area(5,5,[0,1],[3,4])) # 9


