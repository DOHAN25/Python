# list : []

# 생성자
a = list()
print(a)
a.append(1)
print(a)
a.append('one')
print(a)
a[1] = 'two'
print(a)

#a[2] = 3
#print(a)

# [] 사용
b = [1,2,3,'4',5]
print(b)

print(b[0]+b[4])

b.reverse()
print(b)

b.sort()
print(b)

# 중첩
c = ['a','b','c',['d','e','f']]
print(c)
print(c[3][2])

print(b + c)


# tuple : ()
# 수정 불가능한 list

# 생성자
a = tuple()
print(a)
#a.append(1)
#print(a) append 사용 불가능
b = tuple([1,2,'3'])
print(b)

# () 사용
c = (1,2,3,4,5)
print(c)
#c[1]='two'
#print(c)

d = tuple(range(3,6))
print(d)
print(c+d)

#tuple을 list로
e = list(d)
print(e)
#list를 tuple
f = tuple(e)
print(f)
#f.append(6)
#print(f)

#unpacking 확실하게 알아야 unpacking 가능
g,h,i,j = f
print(g)
print(h)
print(i)
print(j)




