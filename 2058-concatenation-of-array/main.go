func getConcatenation(nums []int) []int {
	n := len(nums)
	ans := make([]int, n*2)
	copy(ans, nums)
	for i := 0; i < n; i++ {
		ans[i+n] = ans[i]
	}
	return ans
}
