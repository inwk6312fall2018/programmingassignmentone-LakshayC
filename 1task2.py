
def change_ip(file_name):
	file=open(file_name)
	lst=[]
	lst2=[]	#contains all ips
	lst3=[]	#contains list in ip add
	lst4=[]	#list of updated ip address 
	for line in file:
		line=line.strip()
		for word in line.split():
			lst.append(word)
	for i in range(len(lst)):
		if lst[i-1]!='no' and lst[i]=='ip' and lst[i+1]=='address':
			lst2.append(lst[i+2])	#add all ip add in lst2
	for i in lst2:
		lst3.append(i.split('.'))	#list of elements in ip
	for i in lst3:		#remove '172' or '192' and update with '10'
		del i[0]	#del first element
		i.insert(0,'10')	#insert '10' at first location
		lst4.append('.'.join(i))	#add upated ip add in list
	return lst4

print(change_ip('running-config.txt'))
