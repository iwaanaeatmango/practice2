my_list1 = [] #리스트 만드는 방법 1
my_list2 = list() #리스트 만드는 방법 2

my_list1.append(10)

#extend
my_list1.extend([50,60])
print(my_list1)

#insert
my_list1.insert(0,10)
print(my_list1)

#set (리스트와 다르게 중복을 허용하지 않음, 순서가 유지)
my_set = set(my_list1)
print(my_set)

#tuple 한번 값을 셋팅하면 바꿀 수 없다.
my_tuple1 = (10, 20, 30)
my_tuple2 = tuple()
print(my_tuple1)

num1 = (3)
num2 = (3,)
print(type(num1), type(num2))

#함수의 리턴 타입으로 튜플이 반환된다.
def swap(a, b):
    return (b, a)

#리스트의 슬라이싱
my_list = [10, 20, 100, 40, 10 ,50, 60]
print(my_list)


#문자열 타입 list 선언
cat_list = list('cat')
print(cat_list)

birthday = "2021/11/16"
birth_list = birthday.split("/")
print(birth_list)

if '2021' in birth_list:
    print('oh, yes')

from datetime import datetime as dt

current_year = dt.today().year
birth_year = int(input("몇년생 "))
age = current_year-birth_year+1

print("your age is ", age)
if 17<= age < 20:
    print("고딩 입니다.")
elif 20< age < 27:
    print("대딩입니다.")
else:
    print("학생이 아닙니다.")

