class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int cols = obstacleGrid[0].size();
        int rows = obstacleGrid.size();
        std::vector<int>path (cols, 1);
        
        for (int i=0; i<rows; i++){
            for (int j =0; j<cols; j++){
                if (obstacleGrid[i][j]==1){
                    path[j] = 0;
                    continue;
                }
                if (i==0 && j>0)
                    path[j] = path[j-1];
                if (i>0 && j>0)
                    path [j]+= path[j-1];
                
            }
        }
        return path[cols-1];
    }
};
