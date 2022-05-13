# Strings

text = "X-DSPAM-Confidence:    0.8475"

a=text.find("0")
s=float()
s=text[a:]
print(s)