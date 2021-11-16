"""
yesterday.txt 파일을 읽어서
yesterday 단어가 몇번 나

open mode

r : ready w: write

rb :read binary wb : write binary
a : append

"""
def file_read(file_name):
    with open(file_name, "r") as file:
        lyric= file.read()
        return lyric


read = file_read("yesterday.txt")
print(read)

#대문자로 된 단어 찾기
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'number of a word YESTERDAY {n_of_YESTERDAY}')

#
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'number of a word YESTERDAY {n_of_YESTERDAY}')

#
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'number of a word YESTERDAY {n_of_YESTERDAY}')

#
n_of_YESTERDAY = read.upper().count("YESTERDAY")
print(f'number of a word YESTERDAY {n_of_YESTERDAY}')