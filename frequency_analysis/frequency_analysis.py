# 문자 별 빈도수를 카운트
def key_make(listed_file):      # 평문 file 이 list 로 바뀐 것
    ascii_list = []     # 입력된 문자열을 아스키 코드로 변환하여 복사할 list
    count_list = []     # 문자 개수를 카운트할 list

    # count_list 의 빈 공간 확보
    i = 0
    while i < 26:
        count_list.append(0)
        i += 1

    # 입력된 문자열을 아스키 코드로 변환하여 복사
    i = 0
    while i < len(listed_file):
        temp = ord(listed_file[i])
        ascii_list.append(temp)
        i += 1

    # 문자 빈도수 카운트
    i = 0
    while i < len(listed_file):
        # 소문자(97~122)
        if 96 < ascii_list[i] < 123:
            temp = ascii_list[i] - 97
            count_list[temp] += 1
        # 대문자(65~90)
        elif 64 < ascii_list[i] < 91:
            temp = ascii_list[i] - 65
            count_list[temp] += 1
        # 나머지 문자 형태는 전부 무시
        i += 1

    return count_list       # 빈도수 카운트 결과를 반환


# 내림차순 정렬
def descending_order_sort(listed_file):     # 암호화 키를 list 형태로 변환한 것을 매개변수
    listed_file_sort = []
    listed_file_char = []

    # listed_file 을 listed_file_sort 로 복사
    i = 0
    while i < len(listed_file):
        temp = listed_file[i]
        listed_file_sort.append(temp)
        i += 1

    # listed_file_char 에 영 소문자 26개를 입력
    i = 0
    char = 97
    while i < 26:
        temp = chr(char)
        listed_file_char.append(temp)
        i += 1
        char += 1       # 하나씩 올리면서 a b c d e f g ~ z 를 입력

    # 정렬
    i = 0
    while i < len(listed_file_sort) - 1:
        t = i + 1
        while t < len(listed_file_sort):
            if listed_file_sort[i] < listed_file_sort[t]:
                # 교체
                temp = listed_file_sort[t]
                w = t
                temp1 = listed_file_char[w]

                listed_file_sort[t] = listed_file_sort[i]
                listed_file_char[t] = listed_file_char[i]

                listed_file_sort[i] = temp
                listed_file_char[i] = temp1
            t += 1
        i += 1

    return listed_file_char


# 암호화
def frequency_analysis_encode(listed_file, listed_char):    # listed_file: 평문, listed_char: 빈도수에 따라 정렬된 문자열
    ascii_list = []     # 입력된 문자열을 아스키 코드로 변환하여 복사할 list
    temp_list = []      # 임시 리스트

    # listed_file 에 있는 문자를 모두 아스키코드로 변환
    i = 0
    while i < len(listed_file):
        temp = ord(listed_file[i])
        ascii_list.append(temp)
        i += 1

    # temp_list 에 빈공간 확보
    i = 0
    while i < len(listed_file):
        temp_list.append("")
        i += 1

    # 암호화 진행
    i = 0
    upper = 65      # 대문자
    lower = 97      # 소문자
    while upper < 91:       # A부터 Z까지
        while i < len(ascii_list):      # 전체 문자열에 대한 검사를 실행
            # 소문자 이거나 혹은 대문자라면,
            if 96 < ascii_list[i] < 123 or 64 < ascii_list[i] < 91:
                if ascii_list[i] == upper or ascii_list[i] == lower:        # 각 문자가 a(예시)일 경우에
                    temp_list[i] = listed_char[upper-65]     # 빈도수에 따라 정렬된 리스트의 (예시)첫번째 문자(e)를 temp_list 에 추가한다.
            else:
                temp_list[i] = chr(ascii_list[i])
            i += 1
        i = 0
        upper += 1
        lower += 1
    return temp_list


# 복호화
def frequency_analysis_decode(listed_file, listed_char):        # listed_file: 암호문, listed_char: 빈도수에 따라 정렬된 문자열
    temp_list = []  # 임시 리스트

    # 복호화 진행
    i = 0
    while i < len(listed_file):
        # 소문자 이거나 혹은 대문자라면,
        if 96 < ord(listed_file[i]) < 123 or 64 < ord(listed_file[i]) < 91:
            temp = listed_file[i]       # listed_file 의 문자를
            index_location = listed_char.index(temp)        # 빈도수에 따라 정렬된 문자열 리스트에서 찾고, 인덱스 위치를 반환
            temp = index_location + 97      # 반환된 인덱스에, 아스키 소문자 시작 값 97을 더해서

            temp = chr(temp)        # 그걸 문자로 변환해서
            temp_list.append(temp)      # 반환
        # 영문자가 아니면
        else:
            temp = listed_file[i]       # 그냥 그대로
            temp_list.append(temp)      # 넣는다
        i += 1

    return temp_list
