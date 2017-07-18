# 1. 가득 주유하고 누적 주행 거리(km)를 기록
# 2. 연료를 절반 이상 쓸 때까지 주행하고 그때 주행거리를 기록
# 3. 다시 가득 주유하며 들어간 기름의 양(L) 확인
# => 두 누적 주행거리 차이를 주유량으로 나누면 연비

def gas_mileage(gas_amount, odometer1, odometer2):
    elapsed_trip = abs(odometer1 - odometer2)
    return elapsed_trip / gas_amount

print(gas_mileage(11.3, 625, 926))
