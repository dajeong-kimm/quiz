import random
dict ={
    "메시지 Checksum을 활용한 데이터 인증과 비연결형 무결성을 보장해주는 프로토콜":"AH",
    "암호화 알고리즘을 활용한 캡슐화 기반 페이로드 기밀성을 제공하는 프로토콜" : "ESP",
    "업무중단 시점부터 업무가 복구되어 다시 가동될 때까지의 시간" : "RTO",
    "DRS의 유형으로 데이터만 원격지에 보관하고, \
재해 시 데이터를 근간으로 필요 자원을 조달하여 복구할 수 있는 재해복구센터로 \
재해 발생 시 복구까지의 소요 시간은 수주에서 수개월이 걸린다.":"Cold Site",
    "가장 간단한 구조를 가지며, \
평문을 일정한 블록 단위로 나누어 순차적으로 암호화하는 구조 \
모든 블록이 같은 암호화 키를 사용하기 때문에 \
보안에 취약하고 특히 반복공격에 취약":"ECB",
    "웹상에 존재하는 데이터를 개별 URI로 식별하고, \
각 URI에 링크 정보를 부여함으로써 상호 연결된 웹을 지향하는 아키텍처":"LOD",
    "작성해야 하는 프로그램에 대한 테스트를 먼저 수행하고 \
이 테스트를 통과할 수 있도록 실제 프로그램의 코드를 작성한다는 원리":"TDD",
    "정보시스템 개발에 필요한 관리 절차와 작업 기반을 체계화한 방법론으로\
 대형 프로젝트를 수행하는 체계적인 방법론":"Information Engineering Development",
    "특정 제품에 적용하고 싶은 공통된 기능을 정의하여 개발하는 방법론으로 \
임베디드 소프트웨어를 작성하는 데 유용한 방법론":"Product Line Development",
}
dict_list = list(dict.items())
# print(dict_list[3][0])
# print(dict_list[3][1])

count = 1
while dict_list:
    len_dict = len(dict_list)
    r_num = random.randrange(len_dict)
    print(f"#{count}")
    print(dict_list[r_num][0])
    print("정답입력: ",sep = " ")
    s = input()
    print(dict_list[r_num][1])
    if s.lower() == dict_list[r_num][1].lower():
        print("정답!")
        dict_list.pop(r_num)
    else:
        print("오답!")
    print("------------------------------------")
    count += 1

