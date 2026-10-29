public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> number_index = new Dictionary<int, int>();
        int num_length = nums.Length;
        for (int i = 0; i < num_length; ++i) {
            if (number_index.ContainsKey(target - nums[i])) {
                return [number_index[target - nums[i]], i];
            }
            number_index.Add(nums[i], i);
        }

        return [];
    }
}
