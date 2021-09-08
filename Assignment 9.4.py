name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    counts[words[1]] = counts.get(words[1], 0) + 1

largest = None
largest_author = None

for key in counts:
    if largest is None:
        largest = counts[key]
    if largest < counts[key]:
        largest = counts[key]
        largest_author = key

print(largest_author, largest)


if __name__ == '__main__':
    try:
        name = input("Enter file:")
        if len(name) < 1:
            name = "mbox-short.txt"
        handle = open(name)

        m = dict()
        for word in handle:
            if word.startswith('From '):
                word = word.split()
                mail = word[1]
                m[mail] = m.get(mail, 0) + 1
        for key in m:
            if m[key] == max(m.values()):
                print(key, m[key])
    except:
        #print("Can not open file")
        pass