class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> path(n, 1);
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (i>0 && j>0)
                    path[j] += path[j-1];
            }
        }
        return path[n-1];
    }
};
