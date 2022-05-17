# Files

#filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
total = 0
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:"):
        text=line.rstrip()
        find=line.find(":")
        part = float(text[find+1:])
        count=count+1
        total=total+part
        
        avg=total/count
print("Average spam confidence:",avg)
#...