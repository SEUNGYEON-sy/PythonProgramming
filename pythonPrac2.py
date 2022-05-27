Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
my_str1 = 'a' + 'b' + 'c'
print(my_str1)
abc
my_str2 = 'abc' * 4
print(my_str2)
abcabcabcabc
=================
SyntaxError: invalid syntax
#=====================
# 인덱싱
alphabet = 'abcde'
print(alphabet[0])
a
# 뒤에서부터 가져오기
print(alphabet)
abcde
print(alphabet[-1])
e
print(alphabet[-3])
c
# 슬라이싱
my_str = 'Hello Python!'
print(my_str[0:1])
H
print(my_str[0:2])
He
print(my_str[3:7])
lo P

## 숫자 생략하기
print(my_str[:5])
Hello
print(my_str[6:])
Python!

## 문자열 분리하기
fruit_str = 'apple banana lemon'

fruits = fruit_str.split()
print(fruits)
['apple', 'banana', 'lemon']
print(fruits[1])
banana
print(fruits[2])
lemon
print(fruits[0])
apple

## 문자열 포맷팅
print('Life is {}'.format('Short!'))
Life is Short!
print('{} x {} = {}'.format(2,3,2*3))
2 x 3 = 6
### 여러줄 문자열
print('''첫 번째
두 번째
세 번째''')
첫 번째
두 번째
세 번째
print("""1
2
3
4
5""")
1
2
3
4
5

## 출력의 끝 지정하기
print('coding', end='')
coding
print('coding', end='-')
coding-
print('coding', end='\n')
coding
print('coding', end='\t')
coding	
