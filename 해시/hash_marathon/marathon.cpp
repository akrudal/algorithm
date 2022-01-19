#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int search(string value,vector<string> completion) {
	vector<string>::iterator it;

	it = find(completion.begin(), completion.end(), value);
	int index = it - completion.begin();
	if (it == completion.end()) {
		return -1;
	}
	else {
		return index;
	}
}

string solution(vector<string> participant, vector<string> completion) {
	string answer = "";

	for (int i = 0; i < participant.size(); i++) {
		int num = search(participant[i], completion);
		if (num==-1) { //participant가 있으면 false, 없으면 true를 넘겨준다.
			answer = participant[i];
			break;
		}
		else {
			completion.erase(completion.begin() + num);
		}
	}

	return answer;
}

vector<string> split(string names,vector<string> temp) {
	names=names.substr(1, names.length() - 2);
	istringstream ss(names);
	string stringBuffer;
	while (getline(ss, stringBuffer, ',')) {
		if (stringBuffer[0] == ' ') {
			stringBuffer = stringBuffer.substr(2, stringBuffer.length() - 3);
		}
		else {
			stringBuffer = stringBuffer.substr(1, stringBuffer.length() - 2);
		}
		temp.push_back(stringBuffer);
	}
	
	return temp;
}

int main() {
	vector<string> participants;
	vector<string> completions;

	string names;

	cout << "참가자 : ";
	getline(cin, names);
	participants=split(names,participants);

	cout << "완주한 선수 : ";
	getline(cin, names);
	completions=split(names, completions);

	cout<<solution(participants, completions);
}
