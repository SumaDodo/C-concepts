class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dictionary(256,-1);
        int start = -1, max_length=0;
        
        for (int i=0; i<s.length(); i++){
            if(dictionary[s[i]]>start)
                start = dictionary[s[i]];
            dictionary[s[i]]= i;
            max_length = max(max_length, i-start);
        }
        return max_length;
    }
};

//Solution learnt from @lightmark on leetcode
