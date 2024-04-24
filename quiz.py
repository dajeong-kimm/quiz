import random
dict ={
    "메시지 Checksum을 활용한 데이터 인증과 비연결형 무결성을 보장해주는 프로토콜":"AH",
    "암호화 알고리즘을 활용한 캡슐화 기반 페이로드 기밀성을 제공하는 프로토콜" : "ESP",
    "업무중단 시점부터 업무가 복구되어 다시 가동될 때까지의 시간" : "RTO"
}
dict_list = list(dict.items())
# print(dict_list[0][0])
# print(dict_list[0][1])

count = 1
while dict_list:
    len_dict = len(dict_list)
    r_num = random.randrange(len_dict)
    print(f"#{count}")
    print(dict_list[r_num][0])
    print("정답입력: ",sep = " ")
    s = input()
    print(dict_list[r_num][1])
    if s == dict_list[r_num][1]:
        print("정답!")
        dict_list.pop(r_num)
    else:
        print("오답!")
    print("------------------------------------")
    count += 1

