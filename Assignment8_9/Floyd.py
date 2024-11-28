INF = 9999


# 결과 행렬을 출력하는 함수
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if (A[i][j] == INF):
                print(" INF ", end='')
            else:
                print("%4d " % A[i][j], end='')
        print("")


# Floyd 알고리즘을 이용한 최단 경로 탐색 함수
def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수
    A = list(adj)  # 2차원 배열(리스트의 리스트)의 복사
    P = [[-1] * vsize for _ in range(vsize)]  # 경로 복원 행렬 초기화

    # 초기 행렬 복사
    for i in range(vsize):
        A[i] = list(adj[i])

    # Floyd 알고리즘 수행
    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if (A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = k  # 경로 복원 정보 저장

    return A, P


# 경로를 복원하는 함수
def reconstruct_path(P, start, end):
    path = []
    if P[start][end] != -1:
        path.extend(reconstruct_path(P, start, P[start][end]))
        path.append(P[start][end])
        path.extend(reconstruct_path(P, P[start][end], end))
    return path


# 주어진 정점 간의 최단 경로 출력
def print_shortest_path(vertex, P, start, end):
    start_idx = vertex.index(start)
    end_idx = vertex.index(end)
    path = [start_idx] + reconstruct_path(P, start_idx, end_idx) + [end_idx]
    path_str = " -> ".join(vertex[idx] for idx in path)
    return path_str


# 메인 실행 코드
if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [[0, 7, INF, INF, 3, 10, INF],
              [7, 0, 4, 10, 2, 6, INF],
              [INF, 4, 0, 2, INF, INF, INF],
              [INF, 10, 2, 0, 11, 9, 4],
              [3, 2, INF, 11, 0, 13, 5],
              [10, 6, INF, 9, 13, 0, INF],
              [INF, INF, INF, 4, 5, INF, 0]]

    # Floyd 알고리즘 실행
    A, P = shortest_path_floyd(vertex, weight)

    # 사용자로부터 시작 정점과 종료 정점 입력받기
    start_vertex = input("Start Vertex: ")
    end_vertex = input("End Vertex: ")

    # 최단 경로와 거리 출력
    if start_vertex in vertex and end_vertex in vertex:
        start_idx = vertex.index(start_vertex)
        end_idx = vertex.index(end_vertex)

        print(f"\n* Shortest Path : {print_shortest_path(vertex, P, start_vertex, end_vertex)}")
        print(f"* Distance of the Shortest Path : {A[start_idx][end_idx]}")
    else:
        print("입력된 정점이 유효하지 않습니다. 다시 확인해주세요.")
