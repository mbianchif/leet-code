package has_increasing_subarrays

func allIncreasing(nums []int) bool {
	n := len(nums)

	// O(n)
	for i := 1; i < n; i++ {
		if nums[i-1] >= nums[i] {
			return false
		}
	}

	return true
}

func hasIncreasingSubarrays(nums []int, k int) bool {
	n := len(nums)

	// O(n * k)
	for a := range n - 2*k + 1 {
		if allIncreasing(nums[a : a+k]) {
			b := a + k

			if allIncreasing(nums[b : b+k]) {
				return true
			}
		}
	}

	return false
}
