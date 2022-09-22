public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {

        int numsLength = nums.Length;
        Dictionary<int,int> numsCount = new Dictionary<int,int>();
        List<int>[] bucketArray = new List<int>[numsLength+1];
        int[] output = new int[k];
        
        for (int i=0; i<numsLength; i++) {
            if (numsCount.ContainsKey(nums[i])) {
                numsCount[nums[i]] ++;
            }
            else {
                numsCount[nums[i]] = 1;
            }
        }

        foreach (KeyValuePair<int,int> kvp in numsCount) {
            if (bucketArray[kvp.Value] == null){
                bucketArray[kvp.Value] = new List<int>();
            }
            bucketArray[kvp.Value].Add(kvp.Key);
        }
        
        int kth = 0;
        for (int i=bucketArray.Length-1; i >=0; i--) {
            if (bucketArray[i] != null) {
                for (int j=0; j<bucketArray[i].Count; j++) {
                    output[kth] = bucketArray[i][j];
                    kth++;
                    if (kth >= k) {
                        return output;
                    }
                }
            }
        }
        return output;
    }
}