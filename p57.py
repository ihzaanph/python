inf=False
try:
      with open('abc.txt','r') as inf:
          wordsList = inf.read().split()
      l= len(max(wordsList, key=len))
      result = [x for x in wordsList if len(x) == l]
      print("The following are the longest words from a text file:")
      print(result)
except IOError as e:
       print(e)
finally:
          if inf:inf.close()