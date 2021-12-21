#include <iostream>
#include <queue>
#include <vector>
#include <string.h>

using namespace std;

#define MAX_NODE 52 // 전체 알파벳 개수, 소문자(26개)와 대문자(26개)는 다르게 구별
#define INF 1e9 // 최대 유량 비교 시 사용

// 용량 배열
int capacity[MAX_NODE][MAX_NODE];

// 유량 배열
int flow[MAX_NODE][MAX_NODE];

// BFS 탐색 시, 인접한 노드를 확인하기 위한 배열
vector<int> neighbor_node[MAX_NODE];

// BFS 탐색 시, 방문했던 노드를 기록하기 위한 배열
int visited[MAX_NODE];

// 최대 유량 결과
int result_max_flow;

// 문자를 숫자로 바꾸는 함수
int ctoi(char c){

    // 대문자라면 0~25 의 범위로 변환
    if (c <= 'Z'){
        return c - 'A';
    }
    // 소문자라면 26~51 의 범위로 변환
    return c - 'a' + 26;
}

// BFS 를 사용한 source 에서 sink 로의 최단 경로 탐색
int maximum_flow(int source_node, int sink_node){

    // source 에서 sink 까지의 증가경로가 없을때까지 반복
    while(1){
        
        // 방문 노드 배열을 -1 로 초기화
        memset(visited, -1, sizeof(visited));
        // BFS 탐색 시 사용되는 queue
        queue<int> q;
        // source 를 queue 에 삽입
        q.push(source_node);

        // source 에서 sink 까지 BFS 탐색이 끝날 때까지 반복
        while(!q.empty()){
            
            // 현재 노드
            int current_node = q.front();
            // 현재 노드는 queue 에서 제거
            q.pop();

            // 현재 노드와 인접한 노드들을 queue 에 삽입
            for (int i=0; i<neighbor_node[current_node].size(); ++i){

                // 인접 노드
                int next_node = neighbor_node[current_node][i];

                // 인접 노드 경로에, 잔여 용량이 남아있고, 아직 방문하지 않았다면(-1 이라면)
                if ((capacity[current_node][next_node] - flow[current_node][next_node] > 0) && (visited[next_node] == -1) ){
                    
                    // 인접 노드를 queue 에 삽입
                    q.push(next_node);
                    
                    // 인접 노드가 현재 노드로부터 방문됐다는 내용을 기록
                    visited[next_node] = current_node;

                    // 인접 노드가 sink 라면, 경로를 찾았으므로, BFS 탐색 종료
                    if (next_node == sink_node) break;  
                }
            }
            // source 에서 sink 까지의 경로를 찾았으므로, BFS 탐색 종료
            if (visited[sink_node] != -1) break;
        }

        // BFS 탐색이 끝났음에도 불구하고, sink_node 가 방문되지 않았다는 건
        // 더 이상 source 에서 sink 로 가는 경로가 없다는 의미이므로, 탐색 종료
        if (visited[sink_node] == -1) break;

        // source 에서 sink 로 가는 증가 경로가 있는 경우
        int temp_max_flow = INF;
        int residual_capacity;

        // 방문 노드 배열을 역순으로 탐색하며, 최대 유량 확인
        for (int i=sink_node; i != source_node; i=visited[i]){
            // 잔여 용량 계산
            residual_capacity = capacity[visited[i]][i] - flow[visited[i]][i];
            // 최대 유량과 최소 비교 후 변환
            temp_max_flow = min(temp_max_flow, residual_capacity);                
        }

        // 최대 유량을 찾았다면, 다시 방문 노드 배열을 역순으로 탐색하며, 유량 증가
        for (int i=sink_node; i != source_node; i=visited[i]){
            
            // 이전 노드에서 다음 노드로 가는 유량 증가
            flow[visited[i]][i] += temp_max_flow;

            // 다음 노드에서 이전 노드로 가는 유량 증가 (역간선)
            flow[i][visited[i]] -= temp_max_flow;
        }

        // 해당 경로에서 발견된 최대 유량을 결과에 추가
        result_max_flow += temp_max_flow;
    }   
    return result_max_flow;
}


int main(){

    // 간선 개수 입력
    int edge_count;
    cin >> edge_count;

    // 간선 및 용량 입력
    char char_start_node, char_end_node;
    int input_capacity;
    
    for (int i=0; i<edge_count; ++i){
        
        cin >> char_start_node >> char_end_node >> input_capacity;
        // 문자 노드를 숫자 노드로 변경
        int int_start_node = ctoi(char_start_node);
        int int_end_node = ctoi(char_end_node);

        // 입력에 따라, 인접 노드 등록
        neighbor_node[int_start_node].push_back(int_end_node);
        neighbor_node[int_end_node].push_back(int_start_node);

        // 양방향 간선이므로, 양쪽으로 용량 할당
        capacity[int_start_node][int_end_node] += input_capacity;
        capacity[int_end_node][int_start_node] += input_capacity;
    }

    // A 부터 Z 까지의 최대 유량 탐색
    cout << maximum_flow(ctoi('A'),ctoi('Z')) << endl;

}