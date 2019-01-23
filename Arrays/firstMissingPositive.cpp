class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        int index;
        for (int i =0; i< nums.size(); i++){
            if(nums[i]<1)
                nums[i] = n + 1;
        }
        
        for(int i =0; i<nums.size(); i++){
            index = abs(nums[i]) - 1;
            if (index < nums.size() && 0 < nums[index])
                nums[index] = -nums[index];
        }
        
        for (int i = 0; i < nums.size(); i++){
            if (nums[i]>-1)
                return i+1;
        }
        return n+1;
    }
};
