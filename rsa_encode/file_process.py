# 경로 전달 시, '\' 를 '\\'로 표현 해야 정상적으로 전달 됨
def file_copy_to_list(location):       # location: 파일 경로
    f = open(location, 'r')
    line = f.read()     # file 내용을 모두 line 에 입력
    f.close()

    # listed_plain(List)에 line(Array)를 복사
    listed_plain_text = []
    i = 0
    while i < len(line):
        listed_plain_text.append(line[i])
        i += 1
    return listed_plain_text
