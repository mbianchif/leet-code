package thetwosneakynumbersofdigitville

func getSneakyNumbers(nums []int) []int {
	seen := make(map[int]struct{})
	repeated := make([]int, 0, 2)

	// O(n)
	for _, x := range nums {
		if _, ok := seen[x]; !ok {
			seen[x] = struct{}{}
		} else {
			repeated = append(repeated, x)
			if 2 == len(repeated) {
				return repeated
			}
		}
	}

	return nil
}
