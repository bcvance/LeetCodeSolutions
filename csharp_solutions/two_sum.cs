public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int,int> numTable = new Dictionary<int,int>();
        for (int i=0; i<nums.Length; i++) {
            int neededNum = target - nums[i];
            if (numTable.ContainsKey(neededNum)) {
                return new int[]{i, numTable[neededNum]};
            }
            else {
                numTable[nums[i]] = i;
            }
        }
        return new int[]{-1,-1};
    }
}