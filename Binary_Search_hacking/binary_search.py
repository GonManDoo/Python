# 선형 리스트 만들기
def liner_list(start, end):     # 몇부터 몇까지 선형 정렬된 리스트를 만들 것인가
    temp_list = []
    while start < end + 1:
        temp_list.append(start)
        start += 1
    return temp_list


# 이진 탐색 키 만들기
def binary_search_key(sorted_list):
    # 홀수라면
    if len(sorted_list) % 2 == 1:
        key = (len(sorted_list) + 1) / 2        # 중간 값을 key 로 만듬
    else:
        key = len(sorted_list) / 2
