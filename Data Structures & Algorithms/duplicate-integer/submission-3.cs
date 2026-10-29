public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> numbers = new HashSet<int>();

        foreach (int i in nums) {
            if (numbers.Contains(i)) {
                return true;
            }
            numbers.Add(i);
        } 

        return false;
    }
}