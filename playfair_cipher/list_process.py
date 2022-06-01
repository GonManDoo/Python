# array 형태의 문자를 list 에 복사
def array_copy_to_list(arrayed_text):
    temp_list = []
    i = 0
    while i < len(arrayed_text):
        temp_list.append(arrayed_text[i])
        i += 1
    return temp_list


# array 형태의 문자를 공백제외 하고, 대문자로 바꿔서 list 에 복사
def array_copy_to_list_exclude_enter_capital(arrayed_text):
    temp_list = []
    i = 0
    while i < len(arrayed_text):
        if arrayed_text[i] != " ":       # 공백이 아닐 경우에만
            temp = arrayed_text[i]
            if 96 < ord(arrayed_text[i]) < 123:     # 소문자일 경우
                temp = chr(ord(arrayed_text[i]) - 32)       # 대문자로 변환해서
            temp_list.append(temp)
        i += 1
    return temp_list


# list 안에 중복된 문자를 제거
def delete_overlapped_list(listed_text):
    temp_list = []
    i = 0
    while i < len(listed_text):
        t = i + 1
        while t < len(listed_text) and listed_text[i] != "":     # listed_text[i]가 공백이 아니라면,
            if listed_text[i] == listed_text[t]:        # 앞에 있는 값과 뒤 문자가 서로 같으면
                listed_text[t] = ""        # 뒤 문자를 공백으로 만듬
            t += 1
        i += 1

    # 공백 제거
    i = 0
    while i < len(listed_text):
        if listed_text[i] != "":        # 공백이 아닌 경우에만
            temp_list.append(listed_text[i])        # temp_list 에 추
        i += 1

    return temp_list


def make_after_str(listed_text):
    # a, b, c, d ~ z list 만들기
    temp_list = []
    i = 65
    while i < 91:
        temp = chr(i)       # 문자 형으로 변환
        temp_list.append(temp)      # 추가
        i += 1

    # a 부터 z 까지의 list 에서 매개 변수로 받은 list 와 겹치는 문자를 제거
    i = 0
    while i < len(listed_text):
        temp = temp_list.index(listed_text[i])      # 문자의 위치를 반환해서
        del temp_list[temp]     # 제거
        i += 1

    return temp_list


def five_by_five_table(listed_text):
    # 5*5 테이블 형성
    table = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
             ["", "", "", "", ""]]

    # table 에 값 삽입
    i = 0
    h = 0
    while h < 5:
        w = 0
        while w < 5:
            table[h][w] = listed_text[i]
            i += 1
            w += 1
        h += 1

    # table 출력
    h = 0
    while h < 5:
        print("[", table[h][0], "]      ", "[", table[h][1], "]     ", "[", table[h][2], "]     ",
              "[", table[h][3], "]     ", "[", table[h][4], "]   ")
        h += 1

    return table


# 평문을 2개씩 쌍을 지음
def make_fair(listed_text):
    temp_list = []
    i = 0
    while i < len(listed_text):
        try:
            # 같은 문자일 경우
            if listed_text[i] == listed_text[i + 1]:
                temp = str(listed_text[i]) + "X"  # 첫문자와 X를 묶고
                temp_list.append(temp)  # 삽입
                listed_text.insert(i + 1, 0)  # 문자열에는 빈공간을 추가하여 추후 연산에 영향이 없도록 함
            # 일반적 상황(2개씩 페어)
            else:
                temp = str(listed_text[i]) + str(listed_text[i + 1])
                temp_list.append(temp)
            i += 2
        # 뒷 값이 없을 경우
        except IndexError:  # list out of range 오류 발생 시 실행하도록 함
            temp = str(listed_text[i]) + "X"  # 첫문자와 X를 묶고
            temp_list.append(temp)  # 삽입
            i += 2

    return temp_list


# 2개씩 쌍을 지은 평문을 테이블로 출력(암호화 결과도 포함할 수 있음)
def two_by_n_table(listed_fair_text, listed_encoded_text="None"):
    i = 0
    while i < len(listed_fair_text):
        print("[", listed_fair_text[i], "]  ", end="")     # 줄바꿈 없이 연속 출력
        i += 1
    print("")

    if listed_encoded_text != "None":       # 암호화 결과도 값이 입력되있으면, 출력하도록 함
        i = 0
        while i < len(listed_encoded_text):
            print("[", listed_encoded_text[i], "]  ", end="")  # 줄바꿈 없이 연속 출력
            i += 1


# 2차원 배열에서 문자의 index 를 반환
# listed_key_table : 5*5 테이블 2차원 배열
# char : 검색하길 원하는 문자
# h, w : 최대 좌표, 여기선 5 5로 전달
# faired_location : 사용자에 의해 묶인 table index 좌표
def location_find(listed_key_table, char, h, w, faired_location):
    listed_location = []
    i = 0
    while i < h:
        t = 0
        while t < w:
            # 만약 fair 된 index 를 탐색한다면,
            if i == faired_location[0] and t == faired_location[1]:
                # fair 를 분리
                temp = list(listed_key_table[i][t])     # 3개의 인덱스(문자, /, 문자)를 가짐
                # 만약 fair 묶음에 char 이 있다면,
                if temp[0] == char or temp[2] == char:
                    listed_location.append(i)  # h 추가
                    listed_location.append(t)  # w 추가
                    # break(모든 루프를 끝냄)
                    t = w
                    i = h
            # 일반적 상황
            elif listed_key_table[i][t] == char:
                listed_location.append(i)       # h 추가
                listed_location.append(t)       # w 추가
                # break(모든 루프를 끝냄)
                t = w
                i = h
            t += 1
        i += 1

    return listed_location


def list_choose(listed_text):
    i = 0
    while i < len(listed_text):
        print("listed_text[i]:", listed_text[i])
        if len(listed_text[i]) == 4:        # listed_text[i]의 길이가 3이상이면(중복된 값이면)
            print("진입")
            temp = listed_text[i]       # listed_text[i]를 temp에 넣고
            print("temp:", temp)
            temp = list(temp)
            print("temp_list:", temp)
            temp = temp[0] + temp[1]
            listed_text[i] = temp
        i += 1

    return listed_text
