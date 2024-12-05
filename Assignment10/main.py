from queue import Queue

# 비교 및 이동 횟수 초기화
num_comp = 0
num_mov = 0

def printStep(A, val):
    print("  Step %2d = " % val, end='')
    print(A)

def selection_sort(A):
    global num_comp, num_mov
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            num_comp += 1  # 비교 증가
            if A[j] < A[least]:
                least = j
        A[i], A[least] = A[least], A[i]
        num_mov += 2  # 스왑은 3번의 이동
        printStep(A, i+1)

def insertion_sort(A):
    global num_comp, num_mov
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0:
            num_comp += 1  # 비교 증가
            if A[j] > key:
                A[j + 1] = A[j]
                num_mov += 1  # 데이터 이동 증가
                j -= 1
            else:
                break
        A[j + 1] = key
        num_mov += 1  # 데이터 삽입 이동
        printStep(A, i)

def bubble_sort(A):
    global num_comp, num_mov
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            num_comp += 1  # 비교 증가
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                num_mov += 2  # 스왑은 3번의 이동
                bChanged = True
        if not bChanged:
            break
        printStep(A, n - i)

def sortGapInsertion(A, first, last, gap):
    global num_comp, num_mov
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i - gap
        while j >= first:
            num_comp += 1  # 비교 증가
            if key < A[j]:
                A[j + gap] = A[j]
                num_mov += 1  # 데이터 이동 증가
                j -= gap
            else:
                break
        A[j + gap] = key
        num_mov += 1  # 데이터 삽입 이동

def shell_sort(A):
    n = len(A)
    gap = n // 2
    while gap > 0:
        if gap % 2 == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n - 1, gap)
        print('     Gap=', gap, A)
        gap = gap // 2

def heapify(A, n, i):
    global num_comp, num_mov
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        num_comp += 1  # 비교 증가
        if A[i] < A[l]:
            largest = l
    if r < n:
        num_comp += 1  # 비교 증가
        if A[largest] < A[r]:
            largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        num_mov += 2  # 스왑은 3번의 이동
        heapify(A, n, largest)

def heapSort(A):
    global num_comp, num_mov
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        num_mov += 2  # 스왑은 3번의 이동
        heapify(A, i, 0)

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    global sorted, num_comp, num_mov
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        num_comp += 1  # 비교 증가
        if A[i] <= A[j]:
            sorted[k] = A[i]
            num_mov += 1  # 데이터 이동 증가
            i += 1
        else:
            sorted[k] = A[j]
            num_mov += 1  # 데이터 이동 증가
            j += 1
        k += 1
    while i <= mid:
        sorted[k] = A[i]
        num_mov += 1  # 데이터 이동 증가
        i += 1
        k += 1
    while j <= right:
        sorted[k] = A[j]
        num_mov += 1  # 데이터 이동 증가
        j += 1
        k += 1
    A[left:right + 1] = sorted[left:right + 1]
    num_mov += right - left + 1  # 병합 이동 횟수

def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q - 1)
        quick_sort(A, q + 1, right)

def partition(A, left, right):
    global num_comp, num_mov
    low = left + 1
    high = right
    pivot = A[left]
    while low <= high:
        while low <= right and A[low] < pivot:
            num_comp += 1  # 비교 증가
            low += 1
        while high >= left and A[high] > pivot:
            num_comp += 1  # 비교 증가
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
            num_mov += 2  # 스왑은 3번의 이동
    A[left], A[high] = A[high], A[left]
    num_mov += 2  # 피벗 스왑 이동
    return high

BUCKETS = 10
DIGITS = 4

def radix_sort(A):
    global num_mov
    queues = [Queue() for _ in range(BUCKETS)]
    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i] // factor) % BUCKETS].put(A[i])
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                num_mov += 1  # 이동 증가
                i += 1
        factor *= 10
        printStep(A, d + 1)

def main():
    global num_comp, num_mov, sorted

    print("* Please input a data list (e.g., 5, 8, 1, 3, 4): ", end="")
    data = list(map(int, input().split(", ")))

    print("* Target Sorting Algorithm List")
    print("  Selection(SEL), Insertion(INS), Bubble(BUB), Shell(SHE),")
    print("  Heap(HEA), Merge(MER), Quick(QUI), Radix(RAD)")

    print("* Select sorting algorithm: ", end="")
    algo = input().strip().upper()

    num_comp = 0  # 비교 횟수 초기화
    num_mov = 0  # 데이터 이동 횟수 초기화
    sorted = [0] * len(data)  # 병합 정렬용 임시 리스트 초기화

    if algo == "SEL":
        selection_sort(data)
    elif algo == "INS":
        insertion_sort(data)
    elif algo == "BUB":
        bubble_sort(data)
    elif algo == "SHE":
        shell_sort(data)
    elif algo == "HEA":
        heapSort(data)
    elif algo == "MER":
        merge_sort(data, 0, len(data) - 1)
    elif algo == "QUI":
        quick_sort(data, 0, len(data) - 1)
    elif algo == "RAD":
        radix_sort(data)
    else:
        print("Invalid algorithm selection!")
        return

    print(">> Sorted:", data)
    print(">> Number of Comparisons:", num_comp)
    print(">> Number of Data Movements:", num_mov)


if __name__ == "__main__":
    main()
