import time

call_count = 0

def hanoi_tower(n, fr, tmp, to) :
    global call_count
    call_count += 1

    if (n == 1) :
        print(f"원판 1 : {fr} --> {to}")
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print(f"원판 {n} : {fr} --> {to}")
        hanoi_tower(n - 1, tmp, fr, to)

n = int(input())
start_time = time.time()

hanoi_tower(n, 'A', 'B', 'C')

end_time = time.time()
exe_time = end_time - start_time

print(f"\n총 함수 호출 횟수 : {call_count}")
print(f"\n실행 시간: {exe_time:.6f}초")

