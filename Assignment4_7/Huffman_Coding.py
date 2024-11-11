from MinHeap import heappush, heappop

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __ge__(self, other):
        return self.freq >= other.freq

def make_tree(char_freq):
    # 단계 1: 노드들의 우선순위 큐 (최소 힙) 생성
    heap = [0]  # 힙의 첫 번째 요소는 사용하지 않음
    for char, freq in char_freq.items():
        heappush(heap, Node(char, freq))

    # 단계 2: 허프만 트리 생성
    while len(heap) > 2:  # 힙의 첫 번째 요소(0)을 제외하고 남아있는 노드가 2개 이상일 때
        # 빈도수가 가장 작은 두 노드를 추출
        left = heappop(heap)
        right = heappop(heap)

        # 이 두 노드를 자식으로 가지는 새로운 내부 노드 생성
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # 병합된 노드를 다시 힙에 추가
        heappush(heap, merged)

    # 남은 노드는 허프만 트리의 루트가 됨
    return heappop(heap)

def make_table(root, code_table={}, code=''):
    # 이 노드가 리프 노드일 경우 코드 테이블에 추가
    if root is not None:
        if root.char is not None:
            code_table[root.char] = code
        make_table(root.left, code_table, code + '0')
        make_table(root.right, code_table, code + '1')
    return code_table

def huffman_encoding(data, code_table):
    # 주어진 문자열을 허프만 코드 테이블을 사용하여 인코딩
    return ''.join(code_table[char] for char in data)

def calculate_compression_ratio(original_data, encoded_data):
    # 원본 데이터의 비트 수 계산 (ASCII 가정: 8비트/문자)
    original_bits = len(original_data) * 8
    compressed_bits = len(encoded_data)
    return compressed_bits / original_bits

if __name__ == "__main__":
    # 주어진 문자들과 그 빈도수
    char_freq = {
        'k': 10,
        'o': 5,
        'r': 2,
        'e': 15,
        'a': 18,
        't': 4,
        'c': 7,
        'h': 11
    }

    while True:
        # 문자 입력 guide 메시지
        data = input("Please a word: ")
        if not all(char in char_freq for char in data):
            print("illegal character")
            continue
        break

    # 단계 1: 허프만 트리 생성
    root = make_tree(char_freq)

    # 단계 2: 허프만 코드 테이블 생성
    code_table = make_table(root)
    #확인용
    #print("Huffman Code 테이블:")
    #for char, code in code_table.items():
    #    print(f"{char}: {code}")

    # 단계 3: 주어진 문자열 인코딩
    encoded_data = huffman_encoding(data, code_table)

    # 단계 4: 압축 비율 계산
    compression_ratio = calculate_compression_ratio(data, encoded_data)
    print(f"\n결과 비트 열: '{data}': {encoded_data}")
    print(f"압축률: {compression_ratio:.2f}")
