
with open("/Users/han3/Downloads/rosalind_lcsq-.txt", "r") as file:
    sequences = [
        line.strip()
        for line in file.read().strip().splitlines()
        if not line.startswith(">")
    ]

# Ensure we have exactly two sequences
if len(sequences) < 2:
    raise ValueError("The file must contain at least two sequences.")
s, t = sequences[0], sequences[1]

m, n = len(s), len(t)
dp = [[""] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = (
            dp[i - 1][j - 1] + s[i - 1] if s[i - 1] == t[j - 1] 
            else max(dp[i - 1][j], dp[i][j - 1], key=len)
        )

print(dp[m][n])
