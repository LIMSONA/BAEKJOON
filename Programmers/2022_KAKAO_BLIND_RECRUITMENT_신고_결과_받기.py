# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

#서로다른 유저 신고 가능, 여러번해도 1회 처리
#k번이상 신고유저 메일로 발송, 신고내용 취합해서 메일발송
#출력: 신고처리 완료 메일 받은 횟수 출력

# def solution(id_list, report, k):
#     answer = []
#     return answer

def solution(id_list, report, k):
    set_report = set(report)
    cnt_list = []  # 신고 당한 사람

    for i in set_report:
        a, b = i.split()
        cnt_list.append(b)

    val_zero = [0] * len(id_list)
    aa = dict(zip(id_list, val_zero))

    for i in cnt_list:
        if aa[i] == 0: aa[i] = 1
        else: aa[i] += 1

    singo = []
    for i in list(aa.keys()):
        if aa[i] >= k: singo.append(i)

    bb = dict(zip(id_list, val_zero))
    for i in set_report:
        a, b = i.split()
        if b in singo: bb[a] += 1

    answer = list(bb.values())
    return answer