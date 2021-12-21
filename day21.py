from functools import cache, reduce
val1 = 4
val2 = 2

sum1 = 0
sum2 = 0

v1 = True
rounds = 0
i = 1
while sum1 < 1000 and sum2 < 1000:
  if v1:
    val1 = ((val1 + i + i+1 + i+2-1) % 10)+1
    sum1 += val1
  else:
    val2 = ((val2 + i + i+1 + i+2-1) % 10)+1
    sum2 += val2
  v1 = not v1
  i = ((i+2)%100)+1
  rounds += 3

print(rounds*min(sum2, sum1))

'''minOrder = [1,1,1,1,3,3] # starting 1   - 6 Rounds = +29
maxOrder = [3,3,1,1,1,1] # starting 10  - 6 Rounds = +43

val1FirstMin = 0 # already valid
val1FirstMinIdx = 3
val1FirstMax = 2
val1FirstMaxIdx = 2

val2FirstMin = 0 # already valid
val2FirstMinIdx = 1
val2FirstMax = 1
val2FirstMaxIdx = 1'''

def fastModulo(pos):
  if pos > 10:
    pos -= 10
  return pos

@cache
def rollOnce(v1, v2, s1, s2, switch):
  if switch == 3: # 3 tosses done
    s1 = s1+v1 # add v1 to sum
    if s1 >= 21: # won?
      return (1, 0)
    # switch player
    s1r1, s2r1 = rollOnce(v2, v1, s2, s1, 0)
    s2sum = s2r1
    s1sum = s1r1
    return (s2sum, s1sum)
  else: # only a normal toss
    v1r1 = fastModulo(v1+1)
    v1r2 = fastModulo(v1+2)
    v1r3 = fastModulo(v1+3)
    s1r1, s2r1 = rollOnce(v1r1, v2, s1, s2, switch+1)
    s1r2, s2r2 = rollOnce(v1r2, v2, s1, s2, switch+1)
    s1r3, s2r3 = rollOnce(v1r3, v2, s1, s2, switch+1)
    s1sum = s1r1+s1r2+s1r3
    s2sum = s2r1+s2r2+s2r3
    return (s1sum, s2sum)
r1 = rollOnce(4, 2, 0, 0, 0)
print(r1)