# list : []

# ������
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

# [] ���
b = [1,2,3,'4',5]
print(b)

print(b[0]+b[4])

b.reverse()
print(b)

b.sort()
print(b)

# ��ø
c = ['a','b','c',['d','e','f']]
print(c)
print(c[3][2])

print(b + c)


# tuple : ()
# ���� �Ұ����� list

# ������
a = tuple()
print(a)
#a.append(1)
#print(a) append ��� �Ұ���
b = tuple([1,2,'3'])
print(b)

# () ���
c = (1,2,3,4,5)
print(c)
#c[1]='two'
#print(c)

d = tuple(range(3,6))
print(d)
print(c+d)

#tuple�� list��
e = list(d)
print(e)
#list�� tuple
f = tuple(e)
print(f)
#f.append(6)
#print(f)

#unpacking Ȯ���ϰ� �˾ƾ� unpacking ����
g,h,i,j = f
print(g)
print(h)
print(i)
print(j)




