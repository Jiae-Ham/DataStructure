import re
from CircularQueue import CircularQueue

queue = CircularQueue(10)

while True:
    command = input("[메뉴선택] e-enqueue, d-dequeue, q-종료=> ")

    if command == 'e':
        if not queue.isFull():
            value = input(" 입력할 요소 값: ")
            queue.enqueue(value)
            print("[큐 상태]:", queue)
        else:
            print(" 큐가 가득 찼습니다. 더 이상 요소를 추가할 수 없습니다.")
            print("[큐 상태]:", queue)
    elif command == 'd':
        if not queue.isEmpty():
            dequeued_value = queue.dequeue()
            print(f" 삭제된 요소: {dequeued_value}")
        else:
            print(" 큐가 비어 있습니다. 삭제할 요소가 없습니다.")
        print("[큐 상태]:", queue)
    elif command == 'q':
        print(" 프로그램을 종료합니다.")
        exit()
    else:
        print(" 잘못된 명령어입니다. 다시 시도해 주세요.")
