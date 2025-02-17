def grid_paths(m, n):
    # dp[i][j]는 (i, j) 위치까지 도달하는 경로의 수를 의미합니다.
    dp = [[0] * n for _ in range(m)]

    # 첫 번째 행과 첫 번째 열은 이동 방법이 단 한 가지입니다.
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    # 각 칸은 위쪽 칸과 왼쪽 칸에서 올 수 있으므로
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# 예시: 4행 5열 격자
m, n = 4, 5
print(f"{m}x{n} 격자의 경로 수: {grid_paths(m, n)}")
