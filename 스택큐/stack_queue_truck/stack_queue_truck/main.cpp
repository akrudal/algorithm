//
//  main.cpp
//  stack_queue_truck
//
//  Created by 마경미 on 2022/01/27.
//

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 1;
    queue<pair<int,int>> wait;
    queue<pair<int,int>> cross;
    
    for(int i=0;i<truck_weights.size();i++){
        wait.push(make_pair(truck_weights[i],i));
    }
    
    int allTime=truck_weights.size()*(bridge_length+1);
    while(answer<=allTime){
        if(wait.empty()&&cross.empty()) break;
        int weights=wait.front().first;
        cross.push(make_pair(weights, bridge_length)); //(4,2)
        cout<<"cross_first:: answer : "<<answer<<" weights : "<<weights<<" sec : "<<cross.front().second<<endl;
        for(int i=1;i<=bridge_length;i++){
            weights+=truck_weights[wait.front().second+i]; //5
            if(weights<weight){
                answer++;
                if(cross.front().second>0)
                    cross.push(make_pair(wait.front().first,--cross.front().second));
                cross.pop();
                break;
                
            }else{
                answer+=cross.front().second;
                cross.pop();
                break;
            }
        }
        wait.pop();
    }
    return answer;
}

int main(int argc, const char * argv[]) {
    cout<<solution(2,10,{7,4,5,6});
}
