#include <iostream>
#include <stack>
using namespace std;


int main(){

    string input_data ;
    int cnt=0;
    int result=0;
    cin>>input_data;


    for (int i=0; i<input_data.length(); i++){
        if(input_data[i]=='('){
            cnt++;
        }
        else if(input_data[i]==')'){
            if(input_data[i-1]=='('){
                cnt--;
                result+=cnt;

            }
            else if(input_data[i-1]==')'){
                result++;
                cnt--;
            }
        }
        
    }
    
    cout<<result;
    return 0;
}
