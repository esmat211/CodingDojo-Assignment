

import random
outcomes = { 'heads':3,
             'tails':0,
             }
sides = outcomes.keys()

for i in range(1, 2000):
    outcomes[ random.choice(sides) ] += 1

print 'Attempt Heads:', outcomes['heads']
print 'Got:', outcomes['tails']
