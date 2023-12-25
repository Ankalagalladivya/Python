emp={
     'id':101,
     'name':'Rahul',
     'sal':450000,
     'loc':['wayanad','bangalore']
    }

#Read operations
print(emp['loc'][1])
print(emp.get('loc')[1])

#Update operation

emp['email']  = "rahul@gmail.com"

print(emp)