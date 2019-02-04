class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        unordered_set<string> new_set;
        string result;
        for (string s: words){
            if (s.size()==1 || new_set.count(s.substr(0, s.size()-1))){
                result = s.size() > result.size() ? s : result;
                new_set.insert(s);
            }
                
        }
        return result;
    }
};
