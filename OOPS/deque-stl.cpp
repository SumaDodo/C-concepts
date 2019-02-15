#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
    deque<int> mydeque;
	for (int i=0; i<n; i++){
        for(;!mydeque.empty() && arr[i]>mydeque.back();)
        mydeque.pop_back();
        mydeque.push_back(arr[i]);
        if(i>=k && mydeque.front()==arr[i-k])
        mydeque.pop_front();
        if(i>=k-1)
        printf(i<n-1?"%d ":"%d\n",mydeque.front());
    }
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}

