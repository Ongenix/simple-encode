__author__ = "Ongenix"

import sys

def main(option, text, pipe):
  characters = r"abcdefghijklmnopqrstuvwxyz.!@#$%^&*(),:;1234567890 "
  encodedtext = ""
  decodedtext = ""
  if option.lower() == "encode":
    for i in range(len(text)):
      if (characters.index(text[i]))+2 > len(characters):
        encodedtext += characters[0]
      else:
        encodedtext += characters[(characters.index(text[i]))+1]
    if pipe == "--console":
      print(encodedtext)
    else:
      with open(pipe,"a") as f:
        f.write("\n"+str(encodedtext))
  elif option.lower() == "decode":
    for i in range(len(text)):
      if (characters.index(text[i]))-1 < 0:
        decodedtext += characters[len(characters)-1]
      else:
        decodedtext += characters[(characters.index(text[i]))-1]
    if pipe == "--console":
      print(decodedtext)
    else:
      with open(pipe,"a") as f:
        f.write("\n"+str(decodedtext))
  
try:
  main(sys.argv[1],sys.argv[2],sys.argv[3])
except Exception:
  option = input("Encode or Decode?\n").lower()
  text = input("Text?\n")
  main(option,text,"--console")
