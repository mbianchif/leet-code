package calculateMoneyInLeetcodeBank

func totalMoney(n int) int {
	k := 28

	weekSize := 7
	wholeWeeks := n / weekSize
	wholeWeeksTotal := (wholeWeeks-1)*wholeWeeks/2*weekSize + wholeWeeks*k

	partialWeekSize := n % weekSize
	partialWeekTotal := wholeWeeks*partialWeekSize + partialWeekSize*(partialWeekSize+1)/2

	return wholeWeeksTotal + partialWeekTotal
}
