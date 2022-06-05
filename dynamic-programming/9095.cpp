#include <iostream>
#include <vector>

using namespace std;

// 1 ~ n 까지, 각 정수가 몇 개의 조합으로 이루어져있는지를 저장해놓는 변수
vector<int> case_number;

// 입력 받은 n 이, 몇 개의 조합으로 이루어져있는지를 출력
int dp(int n){

    // 4 ~ n 까지, 각 정수가 몇 개의 조합으로 이루어져있는지, 차례대로 계산
    for (int i=4; i<=n; ++i){
        int new_case = case_number[i-3] + case_number[i-2] + case_number[i-1];
        case_number.push_back(new_case);
    }
    // 입력 받은 n 이, 몇 개의 조합으로 이루어져있는지 출력
    return case_number[n];
}

int main(){

    // 테스트 케이스 개수
    int test_case;
    cin >> test_case;

    for (int i=0; i<test_case; ++i){

        // 각 테스트 케이스
        int n;
        cin >> n;

        // 0 ~ 3 까지, 각 정수가 몇 개의 조합으로 이루어져있는지를 초기값으로 저장
        case_number = {0, 1, 2, 4};

        // 입력 받은 정수가 3 이하라면, 이미 계산되어있는 초기값을 배열에서 반환
        if (n <= 3){
            cout << case_number[n] << endl;
        }
        // 입력 받은 정수가 3 초과라면, 해당 정수를 만들 수 있는 조합을 계산
        else{
            cout << dp(n) << endl;
        }
    }
}