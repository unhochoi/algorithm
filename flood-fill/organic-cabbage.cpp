#include <iostream>
#include <queue>
#define MAX 50

using namespace std;

// 배추밭 크기 
int r,c;

// 배추밭
int cabbage_field[MAX][MAX];

// 어떤 배추와 인접한 배추들을 탐색할 BFS 함수
void BFS(int in_x, int in_y){

    // 어떤 배추와 인접한 배추 위치를 담을 Queue
    queue<pair<int,int>> adj_queue;

    // 상하좌우 탐색 시 사용할, 방향 배열
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    // 입력 받은 배추의 위치를 adj_queue 에 삽입
    adj_queue.push(make_pair(in_x,in_y));    

    // 해당 배추는 방문한 위치로 수정
    cabbage_field[in_x][in_y] = 0;

    // adj queue 에 있는 배추의 위치를 전부 탐색할 때까지
    while(!adj_queue.empty()){
        
        // adj_queue 의 front 에 위치한 배추의 위치 저장
        int x = adj_queue.front().first;
        int y = adj_queue.front().second;

        // adj_queue 의 front 에 위치한 배추 제거
        adj_queue.pop();
        
        // 해당 배추와 상하좌우로 인접한 배추들을 모두 탐색 후, adj queue 에 삽입
        for (int i=0; i<4; ++i){
            
            // 탐색할 배추 위치
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            // 해당 위치가 배추밭 내부에 있는지 확인
            if (0<= new_x && new_x < r && 0 <= new_y && new_y < c){
                
                // 해당 위치에 배추가 있다면
                if (cabbage_field[new_x][new_y]==1){
                    
                    // 해당 배추는 방문한 위치로 수정
                    cabbage_field[new_x][new_y] = 0;
                    // adj queue 에 해당 배추 위치를 삽입
                    adj_queue.push(make_pair(new_x, new_y));
                }
            }
        }
    }
}
int main(){

    // 테스트 케이스 개수
    int testcase;

    // 배추 위치
    int x,y;

    // 배추 개수
    int cabbage_count;

    // 테스트 케이스 개수
    cin >> testcase;

    // 테스트 케이스 개수만큼 반복
    for (int t=0 ; t<testcase; ++t){
        
        // 배추밭 크기, 배추 개수
        cin >> r >> c >> cabbage_count;

        // 배추 위치 입력
        for (int i=0; i<cabbage_count; ++i){
            cin >> x >> y;
            cabbage_field[x][y] = 1;
        }

        // 배추흰지렁이 개수 초기화
        int worm = 0;

        // 배추밭을 탐색하며, 배추흰지렁이 개수 파악
        for (int i=0; i<r; ++i){
            for (int j=0; j<c; ++j){
                if (cabbage_field[i][j]==1){
                    BFS(i,j);
                    worm++;
                }
            }
        }

        // 배추흰지렁이 개수 출력
        cout << worm << endl;
    }
}