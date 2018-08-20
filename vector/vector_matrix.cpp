#include <bits/stdc++.h>

using namespace std;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr, int n) {
    int sum = 0;
    int sum1 = 0;
    //vector<vector<int>> :: iterator row;
    //vector<vector<int>> :: iterator col;
    for(int i=0; i<=arr.end();i++ )
    {
        for (int j= 0;j<=arr.end();i++)
        {
            if(i == j)
                sum += arr[i][j];
            if(i = n-j-1 )
                sum1 += arr[i][j];
        }
        
    }
    return abs(sum-sum1);

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> arr(n);
    for (int i = 0; i < n; i++) {
        arr[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = diagonalDifference(arr, n);

    fout << result << "\n";

    fout.close();

    return 0;
}
