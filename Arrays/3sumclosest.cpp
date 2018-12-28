class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int length = nums.size();
        int left, right;
        int result = nums[0]+nums[1]+nums[2];
        int cur = abs(result-target);
        for (int i=0; i<length -2; i++){
            int temp = nums[i]-target;
            left = i+1;
            right = length -1;
            while(left<right){
                int temp1 = temp+nums[left]+nums[right];
                if (abs(temp1)<cur){
                    result = nums[i]+nums[left]+nums[right];
                    if(temp1==0){
                       return result;
                    }
                    cur = abs(result-target);
                }
                if (temp1 >0)
                    right--;
                if (temp1 < 0)
                    left++;
                
            }
        }
        return result;
    }
};
