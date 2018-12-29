class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        typedef pair<int, int> Pair;
        vector<vector<int>> res;
        vector<int> result;
        int n = nums.size();
        // using hash map to store the values and key pair
        // key will be the sum of the pair of elements
        // value is the pair of indices 
        unordered_map<int, vector<Pair>> map;
        for (int i=0; i< n-1; i++){
            for (int j=i+1; j< n; j++){
                // Calculate the remaining sum to loop up into the hash table
                int sum_remaining = target - (nums[i]+nums[j]);
                
                //check in hash map
                if (map.find(sum_remaining) != map.end()){
                    //checking every pair having the sum remaining
                    for (auto pair : map.find(sum_remaining)->second){
                        int x = pair.first;
                        int y = pair.second;
                        
                        //not repeating
                        if((x!=i && x!=j) && (y!=i && y!=j)){
                            vector<int> v{nums[i],nums[j],nums[x],nums[y]}; 
                            sort(v.begin(), v.end()); 
                            res.push_back(vector<int> {v});
                        }
                    }
                }
                map[nums[i]+nums[j]].push_back({i,j});
            }
        }
        std::sort(res.begin(), res.end());
        res.erase(std::unique(res.begin(), res.end()), res.end());
        return res;
    }
};
