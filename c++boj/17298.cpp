#include <iostream>
#include <stack>
using namespace std;

#define MAX_SIZE 1000000

int main(){
    int arr[MAX_SIZE]={0};
    int result[MAX_SIZE];
    fill(result,result+MAX_SIZE,-1);

    int n,temp;
    cin>>n;

    for(int i=0 ; i<n; i++){
        cin>>temp;
        arr[i]=temp;
    }

    stack<int> my_stack;
    int a;
    for (int i=0; i<n; i++){
        while(my_stack.empty() == false && arr[my_stack.top()] < arr[i]){
            result[my_stack.top()] = arr[i];
            my_stack.pop();
        }
        my_stack.push(i);
    }

    for (int i=0 ;i<n; i++){
        cout<<result[i]<<" ";
    }

}