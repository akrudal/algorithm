#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

bool solution(vector<string> phone_book) {
	bool answer = true;

	sort(phone_book.begin(), phone_book.end());

	for (int i = 0; i < phone_book.size(); i++) {
		if (phone_book[i] < phone_book[i + 1] && phone_book[i + 1].substr(phone_book[i].length()) == phone_book[i]){
			answer = false;
			break;
		}
	}

	return answer;
}

int main()
{
	int t;
	cin >> t;

	string temp;
	vector<string> phone_book;
	for (int i = 0; i < t; i++) {
		cin >> temp;
		phone_book.push_back(temp);
	}

	cout << solution(phone_book);

	return 0;
}