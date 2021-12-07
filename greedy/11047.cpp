#include <iostream>
#include <vector>
using namespace std;

vector<int> coin_list;

// 목표 금액까지 몇 개의 동전이 필요한지 출력해주는 함수
int greedy(int remain_cost){

    // 목표 금액까지 필요한 동전 개수
    int count = 0;

    // 동전 배열을 끝에서부터 탐색하기 위한 idx
    int idx = coin_list.size()-1;
    
    while (remain_cost != 0){
        
        // 해당 idx 의 동전보다 남은 금액이 크거나 같으면, 남은 금액해서 해당 idx 금액을 차감하고 동전 개수 + 1
        if (remain_cost >= coin_list[idx]){
            remain_cost -= coin_list[idx];
            count += 1;
        }
        else{
            idx -= 1;
        }
    }
    return count;
}

int main(){

    // 동전의 종류와 목표 금액 입력
    int n, k;
    cin >> n >> k;
    
    // 동전
    int coin;
    
    // 동전 리스트에 동전 삽입
    for (int i=0; i<n; ++i){
        cin >> coin;
        coin_list.push_back(coin);
    }

    cout << greedy(k) << endl;

}