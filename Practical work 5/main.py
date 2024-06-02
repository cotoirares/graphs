def Hamiltonian_path(adj, N):
    dp = [[False for i in range(1 << N)]
          for j in range(N)]

    for i in range(N):
        dp[i][1 << i] = True

    for i in range(1 << N):
        for j in range(N):
            if ((i & (1 << j)) != 0):
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                            adj[k][j] == 1 and
                            j != k and
                            dp[k][i ^ (1 << j)]):
                        dp[j][i] = True
                        break

    for i in range(N):
        if (dp[i][(1 << N) - 1]):
            return True
    return False


def main():
    file_input = open("input.txt", "r")
    N = int(file_input.readline())
    adj = []
    for i in range(N):
        adj.append(list(map(int, file_input.readline().split())))
    if (Hamiltonian_path(adj, N)):
        print("YES")
    else:
        print("NO")

main()