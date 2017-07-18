# 1. 가득 주유하고 누적 주행 거리(km)를 기록
# 2. 연료를 절반 이상 쓸 때까지 주행하고 그때 주행거리를 기록
# 3. 다시 가득 주유하며 들어간 기름의 양(L) 확인
# => 두 누적 주행거리 차이를 주유량으로 나누면 연비

def 연비(주유량, 누적주행1, 누적주행2):
    주행거리 = abs(누적주행1 - 누적주행2)
    return 주행거리 / 주유량

print(연비(11.3, 625, 926))
