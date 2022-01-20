//#include <iostream>
//#include <string>
//#include <vector>
//#include <map>
//
//using namespace std;
//
//bool solution(vector<string> phone_book) {
//	bool answer = true;
//
//	map<string, int> numbers;
//
//	for (int i = 0; i < phone_book.size(); i++) {
//		numbers.insert(make_pair(phone_book[i], phone_book[i].length()));
//	}
//
//	for (auto iter1 : numbers) {
//		for (auto iter2 : numbers) {
//			if (iter1!=iter2 &&iter1.second<=iter2.second && iter1.first == iter2.first.substr(0,iter1.second)) {
//				answer = false;
//				return answer;
//			}
//		}
//	}
//
//	return answer;
//}
//
//int main()
//{
//	int t;
//	cin >> t;
//
//	string temp;
//	vector<string> phone_book;
//	for (int i = 0; i < t; i++) {
//		cin >> temp;
//		phone_book.push_back(temp);
//	}
//
//	cout << solution(phone_book);
//
//	return 0;
//}