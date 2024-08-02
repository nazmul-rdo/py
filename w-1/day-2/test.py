def myfunc(n):
  return abs(n - 40)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

# Explanation of the sorted order:
# 50 is 10 units away from 40.
# 23 is 17 units away from 40.
# 65 is 25 units away from 40.
# 82 is 42 units away from 40.
# 100 is 60 units away from 40.