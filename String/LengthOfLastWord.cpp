class Solution {
public:
    int lengthOfLastWord(string s) {
        int l = s.length()-1;
        int len = 0;
        while (s[l]==' ' && l>=0){
            l--;
        }
        while(l>=0 && s[l]!= ' '){
            len++;
            l--;
        }
        return len;
    }
};
