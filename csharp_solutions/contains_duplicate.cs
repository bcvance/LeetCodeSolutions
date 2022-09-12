public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        Dictionary<int,int> numDict = new Dictionary<int,int>();
        for (int i=0; i<nums.Length; i++) {
            if (!numDict.ContainsKey(nums[i])) {
                numDict[nums[i]] = 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
}