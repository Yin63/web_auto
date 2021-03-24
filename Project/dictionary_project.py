
a = [1, 2, '6', 'summer']

print('i' in a)

dicti1 = {'class_id': 45, 'num': 20}

num = dicti1.get('num')

if num > 5:
    print('班级人数为{}'.format(num))
else:
    print('人数不足')



list1 = ['方方土', '七木' , '荷花鱼' ,'kingo' , 'Amiee' , '焕蓝']

newlist = []

for i in range(len(list1)):
    if (i+2)%2 == 0:
        gender = '男'
    else:
        gender = '女'

    userinfo = {}
    userinfo.update({'name': list1[i], 'age': (i+13)*1.5, 'gender': gender, '城市':'北京'})
    newlist.append(userinfo)

print(newlist)