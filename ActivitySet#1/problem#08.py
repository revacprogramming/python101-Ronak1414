# Files

#filename = "dataset/mbox-short.txt"
fname = input("Enter file name: ")
fh = open(fname)
count=0
for line in fh:
    if  line.startswith("X-DSPAM-Confidence:    0.8475"):
        count=count+1
        
        continue
    
  
avg=float(float(count)/float(line))
print("Average spam confidence:",avg)

