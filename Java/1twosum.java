import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int remaining = target - nums[i];
            if (seen.containsKey(remaining)){
                return new int[] {seen.get(remaining), i};
            } else {
                seen.put(nums[i], i);
            }
        }
        return new int[] {-1, -1};
    }
}
