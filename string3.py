# 문자열 "aaaAAbbBBcCCdE" 가 있다.
# 1부터 위의 문자열의 길이까지의 수를 모두 더한 결과를 출력하여라.

# 힌트.문자열의 길이가 3이라고 하면, 1 + 2 + 3의 결과를 출력하시면 됩니다

a = 'aaaAAbbBBcCCdE'
b = len(a)

sum = 0

for i in range(1, b+1):
    sum = sum + i
print(sum)

# a = "aaaAAbbBBcCCdE"
# b = len(a)
#
# sum = 0
#
# for i in range(1, b + 1):
#     sum = sum + i
#
# print(sum)