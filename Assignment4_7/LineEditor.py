import re
from CircularQueue import CircularQueue

queue = CircularQueue(10)

while True:
    command = input("[메뉴선택] e-enqueue, d-dequeue, q-종료=> ")

    if command == 'e':
        value = input(" 입력할 요소 값: ")
        queue.enqueue(value)
        print("[큐 상태]:", queue)

    elif command == 'd':
        dequeued_value = queue.dequeue()
        if dequeued_value is not None:
            print(f" 삭제된 요소: {dequeued_value}")
        else:
            print(" 큐가 비어 있습니다.")
        print("[큐 상태]:", queue)

    elif command == 'q':
        exit()

    else:
        print(" 잘못된 명령어입니다. 다시 시도해 주세요.")
