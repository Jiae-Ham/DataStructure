import re
from ArrayList import ArrayList

list = ArrayList(1000)
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, "
                    "p-출력, l-파일읽기, s-저장, q-종료=> ")

    if command == 'i' :
        pos = int(input(" 입력행 번호: "))
        str = input(" 입력행 내용: ")
        list.insert(pos, str)

    elif command == 'd' :
        pos = int(input(" 삭제행 번호"))
        list.delete(pos)

    elif command == 'r' :
        pos = int(input(" 변경행 번호: "))
        str = input(" 변경행 내용: ")
        list.replace(pos, str)

    elif command == 'p' :
        print('Line Editor')
        for line in range(list.size) :
            print(f"[{line:2d}] {list.getEntry(line)}")
        print()

    elif command == 'q': exit()

    elif command == 'l' :
        filename = input(" 읽어들일 파일 이름 : ")
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines :
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's' :
        filename = input(" 저장할 파일 이름 : ")
        outfile = open(filename, "w")
        len = list.size
        for i in range(len) :
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()

    elif command == 'm' :
        word_dict = {}

        for i in range(list.size) :
            line = list.getEntry(i)
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                word_dict[word] = word_dict.get(word, 0) + 1 #단언의 출현 빈도 해당 단어가 없으면 0 반환 후 1 추가, 있으면 1 추가

        print("단어 출현 빈도수: ")
        for word, count in word_dict.items():
            print(f"{word} : {count}")

        with open("dic.txt", "w") as dic_file:
            for word, count in word_dict.items():
                dic_file.write(f"{word} : {count}\n")
