

def access_lst(file_name):
	file=open(file_name)
	lst=[]
	for line in file:
		line=line.strip()
		for i in line.split()  # add line to lst
			if i=='global_access' or i=='fw-management_access_in':
				lst.append(line)
	return lst
print(access_lst('running-config.cfg')		
