package lcs

func longestCommonSubsequence(text1 string, text2 string) int {
	n, m := len(text1), len(text2)

	// O(m)
	prev := make([]int, m+1)
	curr := make([]int, m+1)

	// O(n * m)
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if text1[i-1] == text2[j-1] {
				curr[j] = 1 + prev[j-1]
			} else {
				curr[j] = max(prev[j], curr[j-1])
			}
		}

		prev, curr = curr, prev
	}

	return prev[m]
}
