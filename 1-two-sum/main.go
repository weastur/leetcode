func twoSum(nums []int, target int) []int {
    m := make(map[int]int);
	for i, num := range nums {
		m[num] = i;
	}
	for i, num := range nums {
		if j, ok := m[target - num]; ok && j != i {
			return []int{i, j};
		}
	}
	return []int{}
}
