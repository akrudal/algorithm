//
//  main.cpp
//  stack_queue_printer
//
//  Created by 마경미 on 2022/01/26.
//

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

typedef struct{
    int index;
    int prior;
}Document;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<Document> documents;
    
    for(int i=0;i<priorities.size();i++){
        Document doc;
        doc.index=i;
        doc.prior=priorities[i];
        documents.push_back(doc);
    }
    
    int loc=0;
    while(!priorities.empty()){
        Document doc;
        doc.index=documents.front().index;
        doc.prior=documents.front().prior;
        
        documents.erase(documents.begin());
        
        bool check=false;
        
        for(auto iter:priorities){
            if(doc.prior<iter){
                check=true;
                break;
            }
        }

        if(check){
            documents.push_back(doc);
        }else{
            loc++;
            if(doc.index==location){
                answer=loc;
                break;
            }
        }
    }
    
    return answer;
}

int main()
{
    vector<int> priorities={1,2,3,4,5};
    int location=0;
    cout<<solution(priorities,location);
}
