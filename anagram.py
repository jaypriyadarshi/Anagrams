import sys

def swap(_string,loc1,loc2):
	temp=_string[loc1]
	_string[loc1]=_string[loc2]
	_string[loc2]=temp
	return _string

def permute(_string,start,end,results):
	#print _string
	if start==end:
		result=""
		for letter in _string:
			result=result+letter
		results.append(result)
		
	else:
		for i in range(start,end+1):
			_string = swap(_string,start,i)
			permute(_string,start+1,end,results)
			_string = swap(_string,start,i)



f=open('anagram_out.txt','w')
_string=sys.argv[1]
results=[]
permute(list(_string),0,len(_string)-1,results)
results.sort()
for i in results:
	f.write(i+"\n")
f.close()
