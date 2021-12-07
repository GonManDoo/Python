# 경로 전달 시, '\' 를 '\\'로 표현 해야 정상적으로 전달 됨
def file_copy_to_list_encode(location):       # location: 파일 경로
    f = open(location, 'r', encoding='UTF-8')
    line = f.read()     # file 내용을 모두 line 에 입력
    f.close()

    # listed_plain(List)에 line(Array)를 복사
    listed_plain_text = []
    i = 0
    while i < len(line):
        listed_plain_text.append(line[i])
        i += 1
    return listed_plain_text


# decode 용: file 읽어오기(암호문 읽기)
def file_copy_to_list_decode(location):
    i = 0
    listed_encoded_text = []
    f = open(location, 'r', encoding='UTF-8')
    while True:
        line = f.readline()  # file 내용을 줄 마다 입력
        line = line.rstrip("\n")
        listed_encoded_text.append(line)
        i += 1
        if not line:
            break
    f.close()

    return listed_encoded_text


# decode 용: list 를 file 로 만듬
def list_copy_to_file_decode(location, listed_text):
    # 아스키 값을 문자로 변환
    i = 0
    f = open(location, "w", encoding='UTF-8')
    while i < len(listed_text):
        data = chr(int(listed_text[i]))
        f.write(data)
        i += 1
    f.close()


# encode 용: list 를 file 로 만듬
def list_copy_to_file_encode(location, listed_text):
    i = 0
    f = open(location, "w", encoding='UTF-8')
    while i < len(listed_text):
        data = str(listed_text[i])
        f.write(data)
        # 글자 구분용 엔터
        data = "\n"
        f.write(data)
        i += 1
    f.close()
