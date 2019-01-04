class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dictionary(256,-1); //initialize the vector of length 256 all initialized to -1
        int start = -1, max_length=0;
        
        for (int i=0; i<s.length(); i++){
            if(dictionary[s[i]]>start) //If there is repitition, then update the start to the index of the repitited char
                start = dictionary[s[i]];
            dictionary[s[i]]= i; // else update the vector with the char index
            max_length = max(max_length, i-start);
        }
        return max_length;
    }
};

//Solution learnt from @lightmark on leetcode
