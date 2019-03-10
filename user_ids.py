lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
all_nums=[]
all_users = []

for d in digits:
    for d2 in digits:
        all_nums.append(d+d2)



for num in all_nums:
    for char in lowercase:
        for char2 in lowercase:
            all_users.append(num+char+char2)

all_users_1=[d+d1+c+c1 for d in digits for d1 in digits for c in lowercase for c1 in lowercase]

print(len(all_users))
print(all_users[0:6])
print(all_users_1[0:6])
print(all_users == all_users_1)

