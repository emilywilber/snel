import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text
random = generate_random_text(1000)
#print(random)



def mean(counts):
    total = 0

    for i in range:
        total += counts[i]
    total = total / len(count)
    return total



def chi_square(expected, observed):
    x = 0
    for i in range:
        x = (observed[i] - expected[i]) ^2
        x = x / expected[i]
    return x

