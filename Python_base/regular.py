import re

'''
Regualr Expression
. : ���� 1��
^ : ���ڿ��� ����
$ : ���ڿ��� ������
[]: ���� ����
| : or
(): ��ȣ ���� ���Խ� �׷�

* : 0 or more
+ : 1 or more
? : 0 or 1
{n} : n �� �ݺ�
{n, m}: n�� ���� m��
{n, } : n�� ���� ���Ѵ�
'''


"""
r ���ڿ� ǥ���(re ��� Ȯ�� ����)
\w : [a-zA-z0-9_] -> a~Z, 0~9 _�����ϴ� ��� ����
\W : [^a-zA-Z0-9_\ -> ���� ���� ������ ������ ����
\d : [0-9] -> 0~9��� ��� ����
\D : [^0-9] -> ���ڸ� ������ ������ ����
\s : [\t\n\r\f\v] -> ���鹮��
\S : [^\t\n\r\f\v] -> ������ ������ ��� ����
\b : �ܾ��� ���۰� ���� �� ����
\B : �ܾ��� ���۰� ���� �ƴ� �� ����
\\ : \
\[����] : ������ ���ڸ�ŭ ��ġ�ϴ� ���ڿ�
\A : ���ڿ��� ����
\Z : ���ڿ���
"""

str01 = '���� �̸�����  kh.123@kh.com123�Դϴ�'
match = re.search(r'[\w]*@[a-zA-Z.]*', str01)
print(match.group())