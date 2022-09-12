public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> sCount = new Dictionary<char, int>();
        Dictionary<char, int> tCount = new Dictionary<char, int>();
        if(s.Length != t.Length) {
            return false;
        }
        else {
            for (int i=0; i<s.Length; i++) {
                if (!sCount.ContainsKey(s[i])) {
                    sCount[s[i]] = 1;
                }
                else {
                    sCount[s[i]] ++;
                }
                if (!tCount.ContainsKey(t[i])) {
                    tCount[t[i]] = 1;
                }
                else {
                    tCount[t[i]] ++;
                }
            }
            return this.areDictsEqual(sCount, tCount);
        }
    }
    
    private bool areDictsEqual(Dictionary<char, int> sCount,Dictionary<char, int> tCount) {
        foreach( KeyValuePair<char,int> kvp in sCount ) {
            if (!tCount.ContainsKey(kvp.Key) || tCount[kvp.Key] != kvp.Value) {
                return false;
            }
        }
        return true;
    }
}