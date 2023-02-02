// How this works:
// for statement gets the index and value of each num, ex: [2,7,15,11] -> i=0 v=2, i=1 v=7
// remaining is calculated by subtracting the value of the current # from target
// the remaining number is searched in the hashmap, checking if previous iterations added it
// if the remaining number is there, return the index of it in the hashmap through hashmap[remaining] along with the index of the current #
// if the remaining number is not there, add current number and its index into the hashmap
// next iteration will check for the next remaining in hashmap and check if it's there.

package main

func twoSum(nums []int, target int) []int {
	hm := make(map[int]int)
	for i, v := range nums {
		remaining := target - v
		if _, ok := hm[remaining]; ok {
			return []int{hm[remaining], i}
		} else {
			hm[v] = i
		}
	}
	return []int{}

}