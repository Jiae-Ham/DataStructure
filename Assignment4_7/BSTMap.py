from BinSrchTree import *


def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')  # node의 key만 중위순회로 출력
        inorder(n.right)

def preorder(n):
    if n is not None:
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key, end=' ')

# 이진탐색트리를 이용한 맵 클래스
class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def search(self, key):
        return search_bst(self.root, key)
        # return search_bst_iter(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)


    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg='BTSMap :', order=1):
        print(msg, end='')
        if order == 1: #전위
            preorder(self.root)
        elif order == 2: #중위
            inorder(self.root)
        elif order == 3: # 후위
            postorder(self.root)
        else:
            print("잘못된 order 값 입니다. 1 : 전위순회, 2: 중위순회, 3: 후위순회")
        print()


# =========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
# =========================================================
# 이진탐색트리를 이용한 맵 테스트 프로그램
if __name__ == "__main__":
    print("\n======= 이진 탐색 트리 테스트 =======")
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value = ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map = BSTMap()

    # 데이터 삽입
    print("\n=== 데이터 삽입 ===")
    for i in range(len(data)):
        map.insert(data[i], value[i])

    # 순회 결과 출력
    print("\n=== 트리 순회 결과 ===")
    map.display("전위 순회: ", order=1)  # 전위순회
    map.display("중위 순회: ", order=2)  # 중위순회
    map.display("후위 순회: ", order=3)  # 후위순회

    # 삭제 후 결과 출력
    delete_keys = [3, 68, 18, 35]
    for key in delete_keys:
        print(f"\n=== 키 {key} 삭제 ===")
        map.delete(key)
        map.display("전위 순회: ", order=1)  # 전위순회
        map.display("중위 순회: ", order=2)  # 중위순회
        map.display("후위 순회: ", order=3) #후위순회
