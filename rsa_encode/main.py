from prime_num_search import euler_of_sieve
from file_process import file_copy_to_list_encode
from file_process import list_copy_to_file_decode
from file_process import list_copy_to_file_encode
from file_process import file_copy_to_list_decode
from rsa import rsa_encode
from rsa import key_make
from rsa import rsa_decode


# plain_text(평문)의 아스키 값을 encoded_text 로 전달
plain_text = file_copy_to_list_encode("C:\\test.txt")
prime_num_list = euler_of_sieve(10, 80)
key_make(prime_num_list)

encoded_text = rsa_encode(plain_text)
list_copy_to_file_encode("C:\\encoded.txt", encoded_text)

print("encoded_text:", encoded_text)
test123 = file_copy_to_list_decode("C:\\encoded.txt")

decoded_text = rsa_decode(encoded_text)
list_copy_to_file_decode("C:\\decoded.txt", decoded_text)
