fname = input("Enter file name: ")
fh = open(fname)
all = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                all = all + float(line[20:])
                count = count + 1
average=all/count
print("Average spam confidence:", average)
