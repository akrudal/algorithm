#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
	vector<int> answer;
	queue<int> q;
	int cnt;

	for (int i = 0; i < progresses.size(); i++) {
		cnt = 1;

		while (progresses[i] + speeds[i] * cnt < 100) {
			cnt++;
		}

		q.push(cnt);
	}

	int temp = 0;
	while(!q.empty()) {
		if (q.front() > temp) {
			temp = q.front();
			answer.push_back(1);
			q.pop();
		}
		else {
			answer[answer.size() - 1] += 1;
			q.pop();
		}
	}

	return answer;
}

int main() {
	int num;
	cin >> num;

	vector<int> progress;
	vector<int> s;
	vector<int> answer;

	int temp;
	for (int i = 0; i < num; i++) {
		cin >> temp;
		progress.push_back(temp);
	}

	int temp2;
	for (int j = 0; j < num; j++) {
		cin >> temp2;
		s.push_back(temp2);
	}

	answer=solution(progress, s);

	for (int i = 0; i < answer.size(); i++) {
		cout << answer[i]<<" ";
	}
}