public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        IList<IList<string>> output = new List<IList<string>>();
        Dictionary<int[], List<string>> anagrams = new Dictionary<int[], List<string>>(new MyEqualityComparer());
        for (int i=0; i<strs.Length; i++) {
            int[] sortArray = new int[26];
            for (int j=0; j<strs[i].Length; j++) {
                int asciiIndex = (int) strs[i][j] - (int) 'a';
                sortArray[asciiIndex] ++;
            }
            if (anagrams.ContainsKey(sortArray)) {
                anagrams[sortArray].Add(strs[i]);
            }
            else {
                anagrams[sortArray] = new List<string>();
                anagrams[sortArray].Add(strs[i]);
            }
        }
        foreach (KeyValuePair<int[], List<string>> kvp in anagrams) {
            output.Add(kvp.Value);
        }
        return output;
    }
}

public class MyEqualityComparer : IEqualityComparer<int[]>
{
    public bool Equals(int[] x, int[] y)
    {
        if (x.Length != y.Length)
        {
            return false;
        }
        for (int i = 0; i < x.Length; i++)
        {
            if (x[i] != y[i])
            {
                return false;
            }
        }
        return true;
    }

    public int GetHashCode(int[] obj)
    {
        int result = 17;
        for (int i = 0; i < obj.Length; i++)
        {
            unchecked
            {
                result = result * 23 + obj[i];
            }
        }
        return result;
    }
}