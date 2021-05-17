# 문자열 (내장함수)

#덧셈

str = "꽃이 피는 날 goodbye~ 이런 결말이 어울려 안녕 꽃잎 같은 안녕"
str2 = "는 국힙원탑입니다."
print(len(str))


print(str2[2:5])
#인덱싱 
#슬라이싱
#문자열의 길이 : len(문자열 변수 : 길이)
#문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수.count ('특정문자')

print (str.count('아')) 
print (str.split('~')) #공백 기준으로 나누겠다
print (str.index('꽃'))