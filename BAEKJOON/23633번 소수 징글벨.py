# 게임의 규칙

# 1.두 사람은 번갈아가면서 턴 /  한 턴에 징글벨을 최대 A번까지
# 2.두 사람이 게임에서 징글벨을 친 횟수를 합쳐 B -> 게임종료
# 3.소수(prime number)번째로 징글벨을 쳤다면 점수를 1점 얻는다.
# 4.게임이 끝났을 때 점수가 높은 사람이 이긴다.

#첫째 줄 테스트 개수
#둘째 줄 A B
#쿠로부터 시작

from sys import stdin

t= int(stdin.readline())
A,B= map(int, stdin.readline().split())