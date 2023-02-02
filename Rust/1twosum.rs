// How this works:
// for statement gets the index and value of each num, ex: [2,7,15,11] -> i=0 v=2, i=1 v=7
// remaining is calculated by subtracting the value of the current # from target
// the remaining number is searched in the hashmap, checking if previous iterations added it
// if the remaining number is there, return the index of it in the hashmap through hashmap[remaining] along with the index of the current #
// if the remaining number is not there, add current number and its index into the hashmap
// next iteration will check for the next remaining in hashmap and check if it's there.

// This was significantly harder than twosum in the other languages, really interesting learning about Rust
// Rust's performance is incredible!

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm = HashMap::<i32, i32>::new();
        for (i, v) in nums.iter().enumerate() {
            let remaining = target - v;
            if hm.contains_key(&remaining) {
                return vec![hm[&remaining], i as i32];
            } else {
                hm.insert(*v, i as i32);
            }
        }
        return [].to_vec()

    }
}