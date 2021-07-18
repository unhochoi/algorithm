#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 100
using namespace std;

// 모눈종이 크기 
int r, c;

// 모눈종이
int grid_paper[MAX][MAX];

// 분리된 영역의 넓이를 저장할 vector
vector<int> area_dim;

// 인접한 영역을 저장할 Queue
queue<pair<int,int>> adj_queue;

// 상하좌우 탐색 시 사용할 방향 배열
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

// 입력 받은 영역과 인접한 직사각형 외부 탐색
void BFS(int in_x, int in_y){

    // 해당 영역의 전체 넓이
    int dimension = 0;

    // 입력 받은 영역은 방문한 것으로 수정
    grid_paper[in_x][in_y] = 2;

    // 입력 받은 영역은 queue 에 삽입
    adj_queue.push(make_pair(in_x, in_y));

    // 인접한 영역을 모두 탐색할 때까지
    while (!adj_queue.empty()){

        // 인접 영역 Queue 의 front 위치 영역을 저장
        int x = adj_queue.front().first;
        int y = adj_queue.front().second;

        // 인접 영역 Queue 의 front 요소 제거
        adj_queue.pop();

        // 해당 영역의 넓이 + 1
        dimension++;

        // front 영역과 인접한 영역 탐색
        for (int i=0; i<4; ++i){
            int new_x = x + dx[i];
            int new_y = y + dy[i];

            // 인접한 영역이 모눈종이 내부인지 확인
            if (0 <= new_x && new_x < r && 0 <= new_y && new_y < c){

                // 해당 영역을 탐색한 적이 없다면
                if (grid_paper[new_x][new_y]==0){

                    // 해당 영역은 방문한 것으로 수정
                    grid_paper[new_x][new_y] = 2;
                    // 해당 영역은 인접 영역 Queue 에 삽입
                    adj_queue.push(make_pair(new_x, new_y));
                }
            }
        }
    }

    // 해당 영역의 넓이를 vector 에 저장
    area_dim.push_back(dimension);

}


int main(){

    // 분리된 영역 개수
    int isolated_area = 0;

    // 직사각형 개수
    int rectangle_count;

    // 직사각형의 왼쪽 아래 꼭짓점
    int l_x, l_y;

    // 직사각형의 오른쪽 위 꼭짓점
    int r_x, r_y;

    // 모눈종이 크기, 직사각형 개수
    cin >> r >> c >> rectangle_count;

    // 모눈종이에 직사각형 그리기
    for (int i=0; i<rectangle_count; ++i){

        // 직사각형 좌표
        cin >> l_x >> l_y >> r_x >> r_y;
        // 직사각형 그리기
        for (int j = r - r_y; j < r - l_y; ++j){
            for (int k = l_x; k < r_x; ++k){
                grid_paper[j][k]=1;
            }
        }
    }

    // 모눈종이 전부 탐색
    for (int i=0; i<r;++i){
        for (int j=0; j<c; ++j){
            // 해당 영역이 직사각형 외부라면
            if (grid_paper[i][j] == 0){
                // 해당 영역과 인접한 직사각형 외부를 전부 탐색
                BFS(i,j);
                // 분리된 영역 개수 + 1
                isolated_area++;
            }
        }
    }

    // 분리된 영역 개수 출력
    cout << isolated_area << endl;

    // 분리된 영역에 따른 넓이를 오름차순 정렬
    sort(area_dim.begin(), area_dim.end());

    // 오름차순 정렬 된 영역 넓이 출력
    for (int i=0; i<area_dim.size(); ++i){
        cout << area_dim[i] << " ";
    }

}