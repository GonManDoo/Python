# list 를 file 로 변환(각 인덱스를 개행문자로 구분)-frequency_analysis 에서 가져옴
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