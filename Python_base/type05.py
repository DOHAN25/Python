# set (����)

# ������
a = set(['1','2','3','4','4'])
print(a)

#�����ڿ� iteratble�� ��ü��  ������ set�� ������ ��ȯ
b = set('hello')
print(b)

#{} ���
c = {'a','b','c', 'hello', '1','2','3'}
print(c)

c.add('world')
print(c)

# ������, ������
print(a.union(b))
print(a | b)

print(a.intersection(c))
print(a&c)
