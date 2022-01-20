#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";

	unordered_map<string, int> mapNames;

	for (auto itr : completion) {
		if (mapNames.find(itr) == mapNames.end()) { //���� ���
			mapNames.insert(make_pair(itr, 1)); //�� �� �ִ� ���� �߰�
		}
		else {
			mapNames[itr]++; //������ �ִ� ���
		}
	}

	for (auto itr : participant) {
		if (mapNames.find(itr) == mapNames.end()) {//���� ��� => ��
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