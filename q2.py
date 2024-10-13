def min_deletion_insertion(str1, str2):
    m, n = len(str1), len(str2)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
    
    deletion_count = sum(1 for i in range(len(str1)) if str1[i] not in str2)
    insertion_count = dp[m][n] - deletion_count
    
    return deletion_count, insertion_count


str1 = "heap"
str2 = "pea"
deletion_count, insertion_count = min_deletion_insertion(str1, str2)

print("Minimum Deletion =", deletion_count)
print("Minimum Insertion =", insertion_count)