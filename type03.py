# ����
# single quotation �� double quotation�� ���� ����

# single * 1
a = 'python\'s hello, world!'
print(a)

# single * 3
b = '''python's
hello, world!
                hello, python!!
'''
print(b)

# double * 1
c = "Hello, \"World!\""
print(c)

# double * 3
d = """
abc
def
"ghi"
"""
print(d)

# ȥ��
e = 'abc"def"ghi\npython\'s string'
print(e)
f = "abc'def'ghi\ttest"
print(f)
# r : raw string (\�� ���ڷ� �ν�)
g = r":\Workspaces\Workspace_Python\Python00"
print(g)

# ���ڿ�, ���ϱ�, ���ϱ�
str01 = 'hello,'
str02 - 'python!'
print(str01 + str02)
print(str01 * 3 + str02)
