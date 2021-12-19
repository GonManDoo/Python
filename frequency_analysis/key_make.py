from file_process import file_copy_to_list
from file_process import list_copy_to_file_enter
from frequency_analysis import key_make

# file 읽기
# output : listed_text(평문)
plain_text = file_copy_to_list("C:\\Users\\gunma\\Documents\\plain_text.txt")

# Key(빈도 수) 생성하기
# output : listed text
key_list = key_make(plain_text)

# Key(빈도 수) 파일 저장
# output : 각 문자의 빈도수가 개행문자("\n")로 구별되는 파일
list_copy_to_file_enter(key_list, "C:\\Users\\gunma\\Documents\\key(count).txt")
