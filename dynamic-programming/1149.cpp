#include <iostream>
#define MAX 1001
using namespace std;

// 비용 2차원 배열
int cost[MAX][4];

// 누적 비용 2차원 배열
int accum_cost[MAX][4];

// 2가지 값들 중, 최소값을 반환하는 함수
int min(int a, int b){
    return a < b ? a : b;
}

// 3가지 값들 중, 최소값을 반환하는 함수 (위 함수를 오버로딩)
int min(int a, int b, int c){
    int temp = min(a, b);
    return temp < c ? temp : c;
}

// 1번째 집부터 N번째 집까지 칠하는 비용의 최소값을 출력하는 함수
int dp(int n){

    // 1번째 집은, 이전 집이 존재하지 않으므로, 1번째 집의 누적 비용을, 색깔 별 비용으로 초기화
    accum_cost[1][1] = cost[1][1];
    accum_cost[1][2] = cost[1][2];
    accum_cost[1][3] = cost[1][3];

    // 2번째 집부터 n번째 집까지, 모든 색깔 별 비용을 탐색하며, 누적 비용 배열을 갱신
    for (int i=2; i<=n; ++i){
        for (int j=1; j<=3; ++j){
            
            // i번째 집을 빨간색으로 칠한다면, 이전 집으로는 초록색, 파란색이 가능하기 때문에, 
            // i-1번째 집의 초록색, 파란색의 누적 비용 중, 최소 누적 비용을 구한 뒤
            // [i번째 빨간집의 비용 + i-1번째 집까지의 최소 누적 비용]으로 누적 비용을 갱신
            if (j==1){
                 accum_cost[i][1] = cost[i][1] + min(accum_cost[i-1][2], accum_cost[i-1][3]);
            }
            // i번째 집을 초록색으로 칠한다면, 이전 집으로는 빨간색, 파란색이 가능하기 때문에, 
            // i-1번째 집의 빨간색, 파란색의 누적 비용 중, 최소 누적 비용을 구한 뒤
            // [i번째 초록집의 비용 + i-1번째 집까지의 최소 누적 비용]으로 누적 비용을 갱신
            else if (j==2){
                accum_cost[i][2] = cost[i][2] + min(accum_cost[i-1][1], accum_cost[i-1][3]);
            }
            // i번째 집을 파란색으로 칠한다면, 이전 집으로는 빨간색, 초록색이 가능하기 때문에, 
            // i-1번째 집의 빨간색, 초록색의 누적 비용 중, 최소 누적 비용을 구한 뒤
            // [i번째 파란색의 비용 + i-1번째 집까지의 최소 누적 비용]으로 누적 비용을 갱신
            else{
                accum_cost[i][3] = cost[i][3] + min(accum_cost[i-1][1], accum_cost[i-1][2]);
            }
        }
    }

    // 1번째 집부터 N번째 집까지 칠하는 비용 == N 번째 집의 누적 비용이므로,
    // N 번째 집의 누적 비용 중, 최소값을 반환
    return min(accum_cost[n][1], accum_cost[n][2], accum_cost[n][3]);
}

int main(){

    // 집의 수
    int n;
    cin >> n;

    // 1번째 집부터 N번째 집까지의 빨강, 초록, 파랑 비용을 저장
    for (int i=1; i<=n; ++i){
        for (int j=1; j<=3; ++j){
            cin >> cost[i][j];
        }
    }

    // 1번째 집부터 N번째 집까지 칠하는 비용의 최소값 출력
    cout << dp(n);
}