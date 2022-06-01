from list_process import array_copy_to_list_exclude_enter_capital
from list_process import delete_overlapped_list
from list_process import make_after_str
from list_process import location_find


# key 입력 및 처리
def input_key_text(listed_text="None"):
    while listed_text == "None" or listed_text == "":  # 사용자는 선택적으로 text 를 직접 입력하거나, 매개 변수로 전달
        listed_text = input("key 값을 입력:")  # listed_text 에 key 값을 입력
        listed_text = array_copy_to_list_exclude_enter_capital(listed_text)       # list 로 변환

    # 중복문자 제거
    listed_text = delete_overlapped_list(listed_text)
    # 후행문자 입력
    listed_text += make_after_str(listed_text)

    return listed_text


# fair 를 이룰 문자 선택
def choose_fair(listed_text):       # listed_text: 26개 문자가 입력된 list
    print(listed_text)      # listed_text 를 보여줌
    fair_char_1_location = "b"
    fair_char_2_location = "a"
    # 오류 제거용
    fair_char_1 = ""
    fair_char_2 = ""
    while fair_char_1_location > fair_char_2_location:        # 오류 처리
        print("첫번째 문자는 두번째 문자보다 앞에 있어야 합니다.")
        fair_char_1 = input("fair 를 만들 첫번째 문자를 입력하세요:")
        if ord(fair_char_1) > 96:       # 소문자면
            fair_char_1 = chr(ord(fair_char_1) - 32)        # 대문자로 변환해서 입력
        fair_char_2 = input("fair 를 만들 두번째 문자를 입력하세요:")
        if ord(fair_char_2) > 96:       # 소문자면
            fair_char_2 = chr(ord(fair_char_2) - 32)        # 대문자로 변환해서 입력

        # listed_text 에서의 위치를 반환
        fair_char_1_location = listed_text.index(fair_char_1)
        fair_char_2_location = listed_text.index(fair_char_2)

    # 앞 문자에 뒷 문자를 묶음
    temp = listed_text.index(fair_char_1)       # 위치 파악해서
    listed_text[temp] = listed_text[temp] + "/" + fair_char_2

    # 뒷 문자는 제거
    temp = listed_text.index(fair_char_2)       # 위치 파악해서
    del listed_text[temp]       # 제거

    # 좌표 반환 처리(table 상에서)
    location = []
    temp = int(fair_char_1_location / 5)
    location.append(temp)

    temp = int(fair_char_1_location % 5)
    location.append(temp)

    return listed_text, location      # list 를 반환


# 평문 입력
def input_plain_text(listed_text="None"):
    while listed_text == "None" or listed_text == "":  # 사용자는 선택적으로 text 를 직접 입력하거나, 매개 변수로 전달
        listed_text = input("평문을 입력:")  # listed_text 에 평문을 입력
        listed_text = array_copy_to_list_exclude_enter_capital(listed_text)       # list 로 변환
    return listed_text


# 암호화
# listed_plain_text: 2개씩 묶인 평문
# listed_key_table: 5*5 테이블 2차원 배열
# location: 사용자에 의해 묶인 두개의 문자의 좌표
def encode(listed_plain_text, listed_key_table, location):
    temp_list = []
    i = 0
    while i < len(listed_plain_text):
        print("[", listed_plain_text[i], "]")
        # 묶여있는 문자열을 분리
        char = list(listed_plain_text[i])
        # 5*5 테이블에서 위치를 파악
        location_1 = location_find(listed_key_table, char[0], 5, 5, location)
        location_2 = location_find(listed_key_table, char[1], 5, 5, location)

        # 서로 다른 행과 열에 존재할 경우
        if location_1[0] != location_2[0] and location_1[1] != location_2[1]:
            print("# 서로 다른 행과 열에 존재할 경우")
            # 두 문자의 행과 열이 만나는 곳(각 좌표의 h 값을 교환)
            # location1_new = [location_2[0], location_1[1]]
            # location2_new = [location_1[0], location_2[1]]
            a = location_2[0]
            b = location_1[1]
            temp1 = listed_key_table[a][b]
            c = location_1[0]
            d = location_2[1]
            temp2 = listed_key_table[c][d]
            temp3 = temp1 + temp2       # 암호 문자 합치기
            temp_list.append(temp3)     # 암호 문자열에 추가
            print("temp_list:", temp_list)
        # 같은 열에 있다면,
        elif location_1[1] == location_2[1]:
            print("# 같은 열에 있다면,")
            # location_1이 location_2 보다 위에 있다면(작다면),
            print("location_1[0]:", location_1[0])
            print("location_2[0]:", location_2[0])
            if location_1[0] < location_2[0]:
                print("# location_1이 location_2 보다 위에 있다면,(작다면)")
                # location_2가 맨 아래 붙어있다면,
                if location_2[0] == 4:
                    print("# location_2가 맨 아래 붙어있다면,")
                    # location_1은 2로 교체
                    a = location_2[0]
                    b = location_2[1]
                    temp1 = listed_key_table[a][b]
                    # 같은 열의 맨 위 문자로 교체
                    d = location_2[1]
                    temp2 = listed_key_table[0][d]
                    # 문자 합치기
                    temp3 = temp1 + temp2
                    # 문자열에 추가
                    temp_list.append(temp3)
                    print("temp_list:", temp_list)
                # location_1이 location_2보다 위에 있긴한데, 맨 아래가 아니라면,
                else:
                    print("# location_1이 location_2보다 위에 있긴한데, 맨 아래가 아니라면,")
                    # location_1은 2로 교체
                    a = location_2[0]
                    b = location_2[1]
                    temp1 = listed_key_table[a][b]
                    # location_2는 바로 아래 있는 문자로 교체
                    c = location_2[0]
                    d = location_2[1]
                    temp2 = listed_key_table[c+1][d]
                    # 문자 합치기
                    temp3 = temp1 + temp2
                    # 문자열에 추가
                    temp_list.append(temp3)
                    print("temp_list:", temp_list)
            # location_2가 location_1보다 위에 있는데,
            # location_1이 맨 아래 있다면,
            elif location_1[0] == 4:
                print("# location_2가 location_1보다 위에 있는데,")
                print("# location_1이 맨 아래 있다면,")
                # location_2는 1로 교체
                a = location_1[0]
                b = location_1[1]
                temp2 = listed_key_table[a][b]
                # location_1은 같은 열의 맨 위 문자로 교체
                d = location_1[1]
                temp1 = listed_key_table[0][d]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
            # location_2가 location_1보다 위에 있는데,
            # location_1이 맨 아래가 아니라면,
            else:
                print("# location_2가 location_1보다 위에 있는데,")
                print("# location_1이 맨 아래가 아니라면,")
                # location_2는 1로 교체
                a = location_1[0]
                b = location_1[1]
                temp2 = listed_key_table[a][b]
                # location_1는 바로 아래 있는 문자로 교체
                c = location_1[0]
                d = location_1[1]
                temp1 = listed_key_table[c + 1][d]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
        # 같은 행에 있에 있는데
        # location_1이 location_2보다 좌측에 있다면,
        elif location_1[1] < location_2[1]:
            print("# 같은 행에 있에 있는데")
            print("# location_1이 location_2보다 좌측에 있다면,")
            # 그리고 location_2가 우측 끝에 위치한다면,
            if location_2[1] == 4:
                print("# 그리고 location_2가 우측 끝에 위치한다면,")
                # location_1은 2로 교체
                a = location_2[0]
                b = location_2[1]
                temp1 = listed_key_table[a][b]
                # location_2는 맨 왼쪽 문자로 교체
                c = location_2[0]
                temp2 = listed_key_table[c][0]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
            # location_1이 location_2보다 좌측에 있긴한데,
            # location_2가 우측 끝에 위치하지 않는다면,
            else:
                print("# location_1이 location_2보다 좌측에 있긴한데,")
                print("# location_2가 우측 끝에 위치하지 않는다면,")
                # location_1은 2로 교체
                a = location_2[0]
                b = location_2[1]
                temp1 = listed_key_table[a][b]
                # location_2는 바로 오른쪽 문자로 교체
                c = location_2[0]
                d = location_2[1]
                temp2 = listed_key_table[c][d+1]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
        # 같은 행에 있는데
        # location_2가 location_1보다 좌측에 있다면,
        else:
            print("# 같은 행에 있는데")
            print("# location_2가 location_1보다 좌측에 있다면,")
            # location_1이 우측 끝에 위치한다면
            if location_1[1] == 4:
                print("# location_1이 우측 끝에 위치한다면")
                # location_2은 1로 교체
                a = location_1[0]
                b = location_1[1]
                temp2 = listed_key_table[a][b]
                # location_1는 맨 왼쪽 문자로 교체
                c = location_1[0]
                temp1 = listed_key_table[c][0]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
            # location_1이 우측 끝에 위치하지 않는다면,
            else:
                print("# location_1이 우측 끝에 위치하지 않는다면,")
                # location_2은 1로 교체
                a = location_1[0]
                b = location_1[1]
                temp2 = listed_key_table[a][b]
                # location_1는 바로 오른쪽 문자로 교체
                c = location_1[0]
                d = location_1[1]
                temp1 = listed_key_table[c][d + 1]
                # 문자 합치기
                temp3 = temp1 + temp2
                # 문자열에 추가
                temp_list.append(temp3)
                print("temp_list:", temp_list)
            print("\n")
        print("\n")
        i += 1

    return temp_list
