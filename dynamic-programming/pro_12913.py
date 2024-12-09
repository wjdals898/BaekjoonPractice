# 땅따먹기

def solution(land):
    n = len(land)
    for i in range(1, n):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[-1])


data = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(data))
