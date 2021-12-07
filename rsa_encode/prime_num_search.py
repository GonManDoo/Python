# 오일러 체 알고리즘
def euler_of_sieve(from_num, to_num):
    index_end = to_num - 2
    prime_num_list = []

    # 1. 2부터 to_num 까지 숫자를 list 에 입력
    n = 2  # 소수 2부터 시작/prime_num_list[i] = i+2
    while n <= to_num:
        prime_num_list.append(n)
        n += 1

    # 2. 리스트의 i번째 숫자와 자기 자신을 포함한 모든 숫자를 곱하여 새로운 리스트를 만든다.
    i = 0
    new_list = []
    while i <= index_end:  # 인덱스 0부터 인덱스 to_num(끝)까지
        n = i
        while n <= index_end:
            # (불필요 연산 제거). 마지막 인덱스 값보다 큰 경우엔 다음 연산이 의미가 없으므로 중단
            if prime_num_list[i] * prime_num_list[n] > to_num:
                break
            else:
                new_list.append(prime_num_list[i] * prime_num_list[n])
            n += 1
        i += 1
        # 3. 1에서 만든 리스트에서 2에서 만든 리스트와 겹치는 숫자를 제거
        # 3-1. new_list[]에 있는 값이 있는 prime_num_list 위치 찾기
        z = 0  # 초기화
        while z < len(new_list):
            location = prime_num_list.index(new_list[z])
            z += 1
            # 3-2. 해당 인덱스를 삭제
            del prime_num_list[location]  # prime_num_list 길이가 줄어듬 ->  i 루프 n 루프에 동기화 필요
            # 3-3. 인덱스 길이 동기화
            index_end = len(prime_num_list) - 1
        new_list = []  # 초기화(다음 i, n 루프를 위해서)
    # 4. 2부터 to_num 까지 나온 소수를 from_num 부터 to_num 까지로 수정
    i = 0
    while i <= index_end:
        # from_num 보다 작은 소수면,
        if prime_num_list[i] < from_num:
            del prime_num_list[i]  # 인덱스 전체 길이(index_end) 줄어둠
            # 인덱스 길이 동기화
            index_end = len(prime_num_list) - 1
            # 인덱스 포인터 동기화
            i -= 1
        i += 1

    return prime_num_list


# 오일러 체 알고리즘 중간 과정 확인 가능
def euler_of_sieve_print(from_num, to_num):
    index_end = to_num - 2
    prime_num_list = []

    # 1. 2부터 to_num 까지 숫자를 list 에 입력
    print("# 1 2부터 to_num 까지 숫자를 list 에 입력")
    n = 2  # 소수 2부터 시작/prime_num_list[i] = i+2
    while n <= to_num:
        prime_num_list.append(n)
        n += 1

    print(prime_num_list)

    # 2. 리스트의 i번째 숫자와 자기 자신을 포함한 모든 숫자를 곱하여 새로운 리스트를 만든다.
    print("# 2. 리스트의 i번째 숫자와 자기 자신을 포함한 모든 숫자를 곱하여 새로운 리스트를 만든다.")
    i = 0
    new_list = []
    while i <= index_end:  # 인덱스 0부터 인덱스 to_num(끝)까지
        n = i
        while n <= index_end:
            # (불필요 연산 제거). 마지막 인덱스 값보다 큰 경우엔 다음 연산이 의미가 없으므로 중단
            print("[", i, "][", n, "]")
            print("prime_num_list[", i, "] * prime_num_list[", n, "]", prime_num_list[i], "*", prime_num_list[n])
            if prime_num_list[i] * prime_num_list[n] > to_num:
                print("break")
                break
            else:
                print("else")
                new_list.append(prime_num_list[i] * prime_num_list[n])
            print("[", i, "][", n, "]", new_list)
            n += 1
        i += 1
        # 3. 1에서 만든 리스트에서 2에서 만든 리스트와 겹치는 숫자를 제거
        print("# 3. 1에서 만든 리스트에서 2에서 만든 리스트와 겹치는 숫자를 제거")
        # 3-1. new_list[]에 있는 값이 있는 prime_num_list 위치 찾기
        z = 0  # 초기화
        print("len(new_list):", len(new_list))
        while z < len(new_list):
            print("z:", z)
            location = prime_num_list.index(new_list[z])
            z += 1
            # 3-2. 해당 인덱스를 삭제
            del prime_num_list[location]  # prime_num_list 길이가 줄어듬 ->  i 루프 n 루프에 동기화 필요
            # 3-3. 인덱스 길이 동기화
            index_end = len(prime_num_list) - 1
        new_list = []  # 초기화(다음 i, n 루프를 위해서)
        print(prime_num_list)
    # 4. 2부터 to_num 까지 나온 소수를 from_num 부터 to_num 까지로 수정
    print("# 4. 2부터 to_num 까지 나온 소수를 from_num 부터 to_num 까지로 수정")
    i = 0
    while i <= index_end:
        # from_num 보다 작은 소수면,
        if prime_num_list[i] < from_num:
            del prime_num_list[i]  # 인덱스 전체 길이(index_end) 줄어둠
            # 인덱스 길이 동기화
            index_end = len(prime_num_list) - 1
            # 인덱스 포인터 동기화
            i -= 1
        i += 1

    print("from_num 부터, to_num 까지의 소수", prime_num_list)

    return prime_num_list
