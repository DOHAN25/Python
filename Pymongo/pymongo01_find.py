# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.test
score = db.score

cursor = score.find()
#print(cursor)

for doc in cursor:
    pprint.pprint(doc)
    
    
print('-------')

lee = score.find({'name':'lee'})
for doc in lee:
    print(doc)
leess = score.find_one({'name': '이순신'})
print(leess)



print('-----')

print('document의 총 갯수 : ', score.count_documents({}))

print('----')
# 국어 점수가 70점보더 더 큰 토큐먼트들을 출력하자.
kors = score.find({'kor': {'$gt':70}})
for doc in kors:
    print(doc)
    

