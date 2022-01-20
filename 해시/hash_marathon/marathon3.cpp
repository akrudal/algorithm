#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";

	unordered_map<string, int> mapNames;

	for (auto itr : completion) {
		if (mapNames.find(itr) == mapNames.end()) { //없는 경우
			mapNames.insert(make_pair(itr, 1)); //한 명 있는 경우로 추가
		}
		else {
			mapNames[itr]++; //여러명 있는 경우
		}
	}

	for (auto itr : participant) {
		if (mapNames.find(itr) == mapNames.end()) {//없는 경우 => 답
			answer = itr;
			break;
		}
		else {
			mapNames[itr]--;
			if (mapNames[itr] == 0) {
				mapNames.erase(itr);
			}
		}
	}

	return answer;
}