from file_process import file_copy_to_list
from file_process import file_copy_to_list_exclude_enter
from file_process import list_copy_to_file_enter
from file_process import list_copy_to_file_exclude_enter
from frequency_analysis import key_make
from frequency_analysis import descending_order_sort
from frequency_analysis import frequency_analysis_encode
from frequency_analysis import frequency_analysis_decode


test = file_copy_to_list("C:\\Users\\gunma\\Documents\\test.txt")

test1 = key_make(test)

list_copy_to_file_enter(test1, "C:\\Users\\gunma\\Documents\\test(l2f).txt")

test12 = file_copy_to_list_exclude_enter("C:\\Users\\gunma\\Documents\\test(l2f).txt")

test2 = descending_order_sort(test12)

test3 = frequency_analysis_encode(test, test2)      # 암호문이 list 형태로(공백, 개행문자 포함)

list_copy_to_file_exclude_enter(test3, "C:\\Users\\gunma\\Documents\\harriot_encoded(l2f).txt")

test4 = file_copy_to_list("C:\\Users\\gunma\\Documents\\harriot_encoded(l2f).txt")      # 암호문을 다시 test 4에 읽음

test5 = frequency_analysis_decode(test4, test2)

list_copy_to_file_exclude_enter(test5, "C:\\Users\\gunma\\Documents\\harriot_decoded(l2f).txt")
