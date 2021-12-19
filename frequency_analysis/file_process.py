# file 을 list 로 변환
def file_copy_to_list(location="None"):
    while location == "None" or location == "":       # 사용자는 선택적으로 location 경로를 직접 입력하거나, 매개 변수로 전달
        print("[주의 사항]")
        print("상위권한 접근을 위해 pycharm 을 관리자 권한으로 실행하세요")
        print("경로 전달 시, '\\' 를 '\\\\'로 표현 해야 정상적으로 전달됩니다.\n")        # 경로 입력 안내 사항

        print("[예시] C:\\\\test.txt\n")

        location = input("file location:")      # location 에 file 경로를 입력

    f = open(location, 'r', encoding='UTF-8')       # 경로 location 에 있는 파일을 읽기모드로 열음
    line = f.read()     # f.read : 파일 전체의 내용을 하나의 문자열로 읽어옴(array 형태)
    f.close()

    # listed_text(List)에 line(Array)를 복사
    listed_text = []      # 파일의 문자를 하나씩 저장할 list 를 선언
    i = 0
    while i < len(line):        # 파일 문자 개수 만큼 반복
        listed_text.append(line[i])       # array 에 있는 문자를 하나씩 list 에 복사
        i += 1
    return listed_text        # list 형태의 문자 열을 반환, 공백 포함, 개행 문자 포함


# file 을 list 로 변환(개행문자를 제외하고 읽음)
def file_copy_to_list_exclude_enter(location="None"):
    listed_none_enter_text = []
    while location == "None" or location == "":       # 사용자는 선택적으로 location 경로를 직접 입력하거나, 매개 변수로 전달
        print("[주의 사항]")
        print("상위권한 접근을 위해 pycharm 을 관리자 권한으로 실행하세요")
        print("경로 전달 시, '\\' 를 '\\\\'로 표현 해야 정상적으로 전달됩니다.\n")        # 경로 입력 안내 사항

        print("[예시] C:\\\\test.txt\n")

        location = input("file location:")      # location 에 file 경로를 입력

    f = open(location, 'r', encoding='UTF-8')       # 경로 location 에 있는 파일을 읽기모드로 열음
    while True:     # 무한 루프
        line = f.readline()  # file 내용을 줄 마다 읽어서 line 에 담음
        if not line:        # if line == None   읽어온 값이 없으면(End of File)
            break       # 멈춘다
        # 개행 문자 제거
        line = line.rstrip("\n")        # 인자로 전달된 문자열의 오른쪽에서 개행문자를 제거
        # 삽입
        listed_none_enter_text.append(int(line))     # 숫자 형태의 문자를 숫자로 변환하여 리스트에 추가
    f.close()

    return listed_none_enter_text


# list 를 file 로 변환(각 인덱스를 개행문자로 구분)
def list_copy_to_file_enter(listed_text, location="None"):
    while location == "None" or location == "":       # 사용자는 선택적으로 location 경로를 직접 입력하거나, 매개 변수로 전달
        print("[주의 사항]")
        print("상위권한 접근을 위해 pycharm 을 관리자 권한으로 실행하세요")
        print("경로 전달 시, '\\' 를 '\\\\'로 표현 해야 정상적으로 전달됩니다.\n")        # 경로 입력 안내 사항

        print("[예시] C:\\\\test.txt\n")

        location = input("file location:")      # location 에 file 경로를 입력
    f = open(location, "w", encoding='UTF-8')       # 경로 location 에 있는 파일을 쓰기모드로 열음

    # location 에 있는 file 에 listed_text 에 있는 문자를 문자열 형태로 입력
    i = 0
    while i < len(listed_text):
        temp = str(listed_text[i])      # 숫자를 str 형태로 변환(write 하기 위해서)
        f.write(temp)
        f.write("\n")       # 각 배열의 구분을 위한 개행문자 입력
        i += 1
    f.close()


# list 를 file 로 변환(개행문자 구분 없이)
def list_copy_to_file_exclude_enter(listed_text, location="None"):
    while location == "None" or location == "":       # 사용자는 선택적으로 location 경로를 직접 입력하거나, 매개 변수로 전달
        print("[주의 사항]")
        print("상위권한 접근을 위해 pycharm 을 관리자 권한으로 실행하세요")
        print("경로 전달 시, '\\' 를 '\\\\'로 표현 해야 정상적으로 전달됩니다.\n")        # 경로 입력 안내 사항

        print("[예시] C:\\\\test.txt\n")

        location = input("file location:")      # location 에 file 경로를 입력
    f = open(location, "w", encoding='UTF-8')       # 경로 location 에 있는 파일을 쓰기모드로 열음

    # location 에 있는 file 에 listed_text 에 있는 문자를 문자열 형태로 입력
    i = 0
    while i < len(listed_text):
        temp = str(listed_text[i])      # 숫자를 str 형태로 변환(write 하기 위해서)
        f.write(temp)
        i += 1
    f.close()
