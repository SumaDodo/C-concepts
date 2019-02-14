#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, nums;
    vector<int> array_;
    cin>>n;
    while (cin>>nums)
    array_.push_back(nums);

    sort(array_.begin(), array_.end());
    for (int i=0; i<array_.size();i++){
        printf("%d\t", array_[i]);
    }
}
