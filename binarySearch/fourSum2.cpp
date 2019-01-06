class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> count;
        int sum1 = 0, counter = 0;
        for (int a: A){
            for (int b: B){
                count[a+b]++;    
            }
        }
        
        for (int c: C){
            for(int d: D){
                int target = 0 - (c+d);
                if (count.count(target))
                    counter+=count[target];
            }
        }
        return counter;
    }
};
