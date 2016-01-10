users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "\n" * 2

for x in users:
  # prints out 'Students' and 'Instructors'
	print x

	for y in users[x]:
		print y['first_name'], y['last_name'],'-', len(y['first_name']) + len(y['last_name'])

print "\n" * 2


for x in users:
  # prints out 'Students' and 'Instructors'
  print x

  # prints out 'first_name' and 'last_name'
  for key, value in enumerate(users[x]):
    # variable spot is to ensure the index starts at 1 and not 0
    spot = key + 1
    print str(spot) + " person name is " + value['first_name'] + " and last name is " + value['last_name'], len(value['first_name']) + len(value['last_name'])

