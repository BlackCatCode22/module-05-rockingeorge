fname = input('Enter File:')
if len(fname) < 1 : fname = 'words.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
            # idiom: retrieve/create/update counter
            di[w] = di.get(w,0) + 1

# priint(di)
            
#now we want to find the most common word
largest = -1
theword = None
for k,v in di.items() :
      if v > largest :
            largest = v
            theword = k #cature/remember the key that was largest

print(theword,largest)


#counting word frequency usinga  dictionary