#switching from 5 - 7 - 5 syllables (proper english is not guaranteed!!)

import random #imports random integers

syl_2 = ['hello','tonight','apple','sunset','river','pencil','escape','pillow','water','gentle','sunshine','angry','silly','hiccup'] 
syl_3 =['beautiful','elastic','fantastic','enchanted','circular','adopted','family','mystery','celebrate','family','pollution','magnetic','elevate','lollipop']
add_1 = ['and','or','but','yet','so','for','nor','if','as','on','with','at']

def haiku():
    line1 = random.choice(syl_2) + " " + random.choice(add_1) + " " + random.choice(syl_2) 
    line2 = random.choice(syl_3) + " " + random.choice(add_1) + " " + random.choice(syl_3)
    line3 = random.choice(syl_2) + " " + random.choice(add_1) + " " + random.choice(syl_2) 


    return f"{line1}\n{line2}\n{line3}"

result = haiku()

print('Generated Haiku: ')
print()
print(result)
