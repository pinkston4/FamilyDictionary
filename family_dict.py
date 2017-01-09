my_family = {'sister':{'name': 'Lillian', 'age':11}, 
			'mother':{'name': 'Carrie', 'age':53}, 
			'father':{'name': 'Ray', 'age':53}}

for (family_member, info) in my_family.items():
	print('{0} is my {1}, and is {2} years old'.format(info['name'],family_member,info['age']))



