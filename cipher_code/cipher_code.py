def encode_print():
    # Keyword 입력 받기
    sign_a = 0  # Keyword 입력에 쓰일 sign_A
    keyword = input("Keyword:")  # Keyword 입력 받기, 아스키코드로 변환할 예정, 문자로 입력 됨
    if keyword == "":
        while sign_a == 0:
            print("no message. input again")
            keyword = input("Keyword:")  # Keyword 입력 받기, 아스키코드로 변환할 예정
            if keyword != "":  # 어떤 값이라도 입력되었다면,
                sign_a += 1  # sign_A 값을 변경하여 while 탈출

    # Keyword sort(List)에 Keyword(Array)를 복사
    keyword_sort = []
    i = 0
    while i < len(keyword):
        keyword_sort.append(keyword[i])
        i += 1

    # Keyword sort(List) 정렬
    front = 0
    while front < len(keyword) - 1:
        print("front:", front)
        back = front + 1
        while back < len(keyword):
            print("back:", back)
            print("Keyword_sort[", front, "front]:", keyword_sort[front])
            print("Keyword_sort[", back, "back]:", keyword_sort[back])
            if keyword_sort[front] > keyword_sort[back]:
                temp = keyword_sort[back]
                keyword_sort[back] = keyword_sort[front]
                keyword_sort[front] = temp
            back += 1
        front += 1
    print(keyword_sort)

    # keycode(List 처리)
    keycode = []
    i = 0
    while i < len(keyword):
        keycode.append(keyword_sort.index(keyword[i]))
        i += 1
    print(keycode)

    # message 입력(array 로 입력, Keyword 입력과 유사)
    sign_a = 0  # message 입력에 쓰일 sign_A
    message = input("message:")  # message 입력 받기, 아스키코드로 변환할 예정, 문자로 입력 됨
    if keyword == "":
        while sign_a == 0:
            print("no message. input again")
            message = input("message:")  # Keyword 입력 받기, 아스키코드로 변환할 예정
            if message != "":  # 어떤 값이라도 입력되었다면,
                sign_a += 1  # sign_A 값을 변경하여 while 탈출

    # Keycode extension (아래 cipher_code 의 예외 전처리)
    line = len(message) / len(keyword)
    keycode_temp = list(keycode)
    keycode_original = list(keycode)
    print("keycode_temp:", keycode_temp)

    n = 1
    print("keycode:", keycode)
    while n < line:
        i = 0
        while i < len(keyword):
            keycode_temp[i] += n * len(keyword)
            i += 1
            print("Keycode_temp:", keycode_temp)
            print("aKeycode:", keycode)
        print("Keycode:", keycode)
        keycode += keycode_temp
        print("Keycode += Keycode_temp:", keycode)
        keycode_temp = keycode_original
        n += 1
    print(keycode)

    # cipher_code 에 message 길이만큼 a 삽입
    cipher_code = []
    i = 0
    while i < len(message):
        cipher_code.append("a")
        i += 1
    print(cipher_code)

    # message 의 각 문자를 순서에 맞게 cipher 로 변환
    i = 0
    while i < len(message):
        cipher_code[keycode[i]] = message[i]
        i += 1
    print(cipher_code)

    return cipher_code


def encode_no_print():
    # keyword 입력 받기
    sign_a = 0  # Keyword 입력에 쓰일 sign_A
    keyword = input("keyword:")  # Keyword 입력 받기, 아스키코드로 변환할 예정, 문자로 입력 됨
    if keyword == "":
        while sign_a == 0:
            print("no message. input again")
            keyword = input("keyword:")  # Keyword 입력 받기, 아스키코드로 변환할 예정
            if keyword != "":  # 어떤 값이라도 입력되었다면,
                sign_a += 1  # sign_A 값을 변경하여 while 탈출

    # keyword sort(list)에 keyword(array)를 복사
    keyword_sort = []
    i = 0
    while i < len(keyword):
        keyword_sort.append(keyword[i])
        i += 1

    # keyword sort(List) 정렬
    front = 0
    while front < len(keyword) - 1:
        back = front + 1
        while back < len(keyword):
            if keyword_sort[front] > keyword_sort[back]:
                temp = keyword_sort[back]
                keyword_sort[back] = keyword_sort[front]
                keyword_sort[front] = temp
            back += 1
        front += 1

    # Keycode(List 처리)
    keycode = []
    i = 0
    while i < len(keyword):
        keycode.append(keyword_sort.index(keyword[i]))
        i += 1

    # message 입력(array 로 입력, Keyword 입력과 유사)
    sign_a = 0  # message 입력에 쓰일 sign_A
    message = input("message:")  # message 입력 받기, 아스키코드로 변환할 예정, 문자로 입력 됨
    if keyword == "":
        while sign_a == 0:
            print("no message. input again")
            message = input("message:")  # keyword 입력 받기, 아스키코드로 변환할 예정
            if message != "":  # 어떤 값이라도 입력되었다면,
                sign_a += 1  # sign_a 값을 변경하여 while 탈출

    # keycode extension(아래 cipher_code 의 예외 전처리)
    line = len(message) / len(keyword)
    keycode_temp = list(keycode)
    keycode_original = list(keycode)

    n = 1
    while n < line:
        i = 0
        while i < len(keyword):
            keycode_temp[i] += n * len(keyword)
            i += 1
        keycode += keycode_temp
        keycode_temp = keycode_original
        n += 1

    # cipher_code 에 message 길이만큼 a 삽입
    cipher_code = []
    i = 0
    while i < len(message):
        cipher_code.append("a")
        i += 1

    # message 의 각 문자를 순서에 맞게 cipher 에 입력
    i = 0
    while i < len(message):
        cipher_code[keycode[i]] = message[i]
        i += 1
    print(cipher_code)

    return cipher_code
