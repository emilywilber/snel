import random

# function to generate a random string of characters with length num_chars
def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text


def mean(inputlist):
    total = 0
    for i in inputlist:
        total += i
    total = total / len(inputlist)
    return total

def chi_square(inputlist):
    expected = mean(inputlist)
    
    X = 0

    for n in inputlist:
        X += ((n - expected)*(n - expected))/expected

    return X


# test code
bunch_of_text = "asdfhjkjaewhfkljsadhflkjhasedfi9835u2xifu-q3ymtocfjd;sk^%$#^YJH&I*^%$*%TNIOUYTYU^RYI^RGLKHNJJKYTB"




# Create counts, which is the list of numbers  (this is just test code)
counts = [0] * 127
for c in bunch_of_text:
    n = ord(c)
    counts[n] += 1


# Generate 15000 random characters
content = generate_random_text(15000)

# code here to write content to a file
with open('words_party.txt', 'w') as f:
    f.write(content)
    f.close()

# read a text file and creates a list with the character counts where counts[32] holds the number of spaces, counts[97] holds the number of lowercase a's and so on.
with open('words_party.txt', 'r') as f:
    readcontent = f.read()
    f.close()

print("contents of file" + readcontent)

# compute the counts list which contains the number of times each character appears 
counts = [0] * 127
for c in readcontent:
    n = ord(c)
    counts[n] += 1

# lop off the first 31 elements of the list
counts = counts[32:127]

print(counts)
print("file contents mean =")
print(mean(counts))
print("chi-square =")
print(chi_square(counts))

