#include <bits/stdc++.h>

using namespace std;

// Complete the diagonalDifference function below.
int diagonalDifference(vector<vector<int>> arr) {
    int first_diagonal_sum = 0;
    int sec_diagonal_sum = 0;
    int sum = 0;
    int n = arr.size();

    for (int i=0; i<arr.size();i++){
        for(int j=0; j<arr.size();j++){
            if (i==j){
                first_diagonal_sum= first_diagonal_sum + arr[i][j];
                }
        }
    }

    for(int i=0; i<=arr.size();i++){
        for(int j=0; j<=arr[0].size();j++){
            if (i==n-1-j){
                sec_diagonal_sum+=arr[i][j];
            }
        }
    }
    printf("%d\n", first_diagonal_sum);
    printf("%d", sec_diagonal_sum);
    return abs(first_diagonal_sum-sec_diagonal_sum);
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

    int result = diagonalDifference(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
