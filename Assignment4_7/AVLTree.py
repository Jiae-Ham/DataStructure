from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")


def delete_avl(root, key):
    if root is None:
        return root  # 공백 트리일 경우 반환

    # 이진 탐색 트리의 삭제 과정
    if key < root.key:  # 왼쪽 서브트리에서 삭제
        root.left = delete_avl(root.left, key)
    elif key > root.key:  # 오른쪽 서브트리에서 삭제
        root.right = delete_avl(root.right, key)
    else:  # 삭제할 노드를 찾음
        if root.left is None:  # 자식이 하나(오른쪽 자식 또는 없음)
            return root.right
        elif root.right is None:  # 자식이 하나(왼쪽 자식)
            return root.left
        else:  # 자식이 둘인 경우
            # 오른쪽 서브트리에서 최소 노드를 찾아 대체
            min_node = search_min_bst(root.right)
            root.key = min_node.key
            root.value = min_node.value
            root.right = delete_avl(root.right, min_node.key)

    # 삭제 후 AVL 균형 조정
    return reBalance(root)


from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None

    print("=== AVL 트리 삽입 테스트 ===")
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)

        print(f"삽입({i}): ", end="")
        levelorder(root)
        print()

    print("\n=== AVL 트리 삭제 테스트 ===")
    delete_nodes = [3, 5, 7]
    for key in delete_nodes:
        print(f"삭제({key}): ", end="")
        root = delete_avl(root, key)
        levelorder(root)
        print()

    print("\n=== AVL 트리 최종 상태 ===")
    print("노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))


