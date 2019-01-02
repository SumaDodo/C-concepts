class Solution {
public:
    string convert(string s, int numRows) {
        string result;
        if (numRows == 1)
            return s;
        
        vector<string>v(numRows,"");
        int depth = 1;
        int row = 0;
        for(auto c: s){
            v[row].push_back(c);
            row+= depth;
            if (row == numRows-1)
                depth = -1;
            if (row == 0)
                depth = 1;
        }
        for(auto val:v) result.append(val);
        return result;
    }
};
