import random


# RSA 공개키, 비밀키 생성
def key_make(prime_list):       # 소수가 있는 list 가 매개변수
    random.shuffle(prime_list)      # sort 된 상태인 prime_list 섞어줌

    d = 0.1
    while d % 1 != 0:       # d가 정수가 나올 때까지
        # 1. 서로 다른 임의의 두 개의 소수 p, q를 곱하여 n을 만든다.
        p = 0
        q = 0
        n = 0
        while p == q or n < 128:        # p, q가 서로 다르고, n이 128보다 클 때까지
            p = random.randrange(0, len(prime_list))  # 소수 p
            q = random.randrange(0, len(prime_list))  # 소수 q
            n = p * q
        p = prime_list[p]
        q = prime_list[q]
        n = p * q

        # 2. 오일러 파이 함수 ϕ(n)[euler_n 으로 표현] 값을 구한다.
        euler_n = (p - 1) * (q - 1)

        # 3. q, p 와 서로소 관계에 있는 양수 e를 구합니다.
        e = p
        while e % p == 0 or e % q == 0:
            e = random.randrange(2, euler_n)

        # 4. e 와 서로소 관계에 있는 양수 d를 구합니다. (d < ϕ(n))
        d = (1 + (euler_n * 2))/e
    d = int(d)

    print("공개 키&비밀 키n:", n)
    print("공개 키e:", e)
    print("비밀 키d:", d)


# RSA 공개키 비밀키 생성 중간 과정 확인 가능
def key_make_print(prime_list):     # 소수가 있는 list 가 매개변수
    print(prime_list)
    random.shuffle(prime_list)      # sort 된 상태인 prime_list 섞어줌
    print(prime_list)

    d = 0.1
    while d % 1 != 0:       # d가 정수가 나올 때까지
        # 1. 서로 다른 임의의 두 개의 소수 p, q를 곱하여 n을 만든다.
        p = 0
        q = 0
        n = 0
        while p == q or n < 128:        # p, q가 서로 다르고, n이 128보다 클 때까지
            p = random.randrange(0, len(prime_list))  # 소수 p
            q = random.randrange(0, len(prime_list))  # 소수 q
            n = p * q
        p = prime_list[p]
        q = prime_list[q]
        print("p:", p)
        print("q:", q)
        n = p * q
        print("n:", n)

        # 2. 오일러 파이 함수 ϕ(n)[euler_n 으로 표현] 값을 구한다.
        euler_n = (p - 1) * (q - 1)
        print("euler_n:", euler_n)

        # 3. q, p 와 서로소 관계에 있는 양수 e를 구합니다.
        e = p
        while e % p == 0 or e % q == 0:
            e = random.randrange(2, euler_n)
        print("e:", e)

        # 4. e 와 서로소 관계에 있는 양수 d를 구합니다. (d < ϕ(n))
        d = (1 + (euler_n * 2))/e
    d = int(d)
    print("d:", d)

    print("공개 키&비밀 키n:", n)
    print("공개 키e:", e)
    print("비밀 키d:", d)


# RSA 암호화
def rsa_encode(plain_text):
    n = int(input("공개키 n을 입력:"))
    e = int(input("비밀키 e를 입력:"))
    ascii_text = []
    i = 0
    while i < len(plain_text):
        ascii_text.append(ord(plain_text[i]))
        i += 1
    # C(암호문) = M^e (mod n) M은 평문 : C % n = M^e
    encoded_text = []
    i = 0
    while i < len(plain_text):
        temp = ascii_text[i]
        encoded_text.append((temp ** e) % n)  # # encoded_text[i] L : 평문, ned[1] : e
        i += 1

    return encoded_text


# RSA 암호화 중간 과정 확인 가능
def rsa_encode_print(plain_text):
    n = int(input("공개키 n을 입력:"))
    e = int(input("비밀키 e를 입력:"))
    ascii_text = []
    i = 0
    while i < len(plain_text):
        ascii_text.append(ord(plain_text[i]))
        i += 1
    print("ascii_text:", ascii_text)

    # C(암호문) = M^e (mod n) M은 평문 : C % n = M^e
    encoded_text = []
    i = 0
    print("n:", n)
    print("e:", e)
    while i < len(plain_text):
        temp = ascii_text[i]
        print("temp ** e:", temp ** e)
        print("(temp ** e) / n:", (temp ** e) % n)
        encoded_text.append((temp ** e) % n)  # # encoded_text[i] L : 평문, ned[1] : e
        i += 1

    print("encoded_text:", encoded_text)

    return encoded_text


def rsa_decode_print(encoded_text):
    n = int(input("공개키 n을 입력:"))
    d = int(input("공개키 d를 입력:"))

    decoded_text = []
    i = 0
    while i < len(encoded_text):
        if encoded_text[i] != "":
            temp = int(encoded_text[i])
            decoded_text.append((temp ** d) % n)
        i += 1
    print("decoded_text:", decoded_text)

    return decoded_text


def rsa_decode(encoded_text):
    n = int(input("공개키 n을 입력:"))
    d = int(input("공개키 d를 입력:"))

    decoded_text = []
    i = 0
    while i < len(encoded_text):
        if encoded_text[i] != "":
            temp = int(encoded_text[i])
            decoded_text.append((temp ** d) % n)
        i += 1

    return decoded_text
