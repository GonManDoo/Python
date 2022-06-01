from playfair_cipher import input_key_text
from playfair_cipher import choose_fair
from list_process import five_by_five_table
from playfair_cipher import input_plain_text
from list_process import make_fair
from list_process import two_by_n_table
from playfair_cipher import encode
from list_process import list_choose
# key 로 사용할 문자 입력
key_text = input_key_text()

# fair 를 이룰 문자 선택
listed_key_faired, location_faired = choose_fair(key_text)

# 5*5 테이블 형성
listed_key_table = five_by_five_table(listed_key_faired)

# 암호화할 평문 입력
listed_plain_text = input_plain_text()

# 평문을 2쌍씩 짝 지음
listed_plain_faired = make_fair(listed_plain_text)

# 2쌍씩 짝 지은 결과를 보임
two_by_n_table(listed_plain_faired)

# 암호화 진행
listed_encoded_text = encode(listed_plain_faired, listed_key_table, location_faired)

listed_encoded_text = list_choose(listed_encoded_text)

print("cehckehck:", listed_encoded_text)

# 결과를 표로 보임
two_by_n_table(listed_plain_faired, listed_encoded_text)

