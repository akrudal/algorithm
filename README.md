## 알고리즘

--------------------------------------------

<공부 일정>

|순차시|날짜|내용|1차 시도|2차 시도|3차 시도|사용 언어|
|---|-----|-----|-----|-----|-----|-----|
|1|2022.1.19|해시_완주하지 못한 선수|50점|100점|100점|C++|
|2|2022.1.20|해시_전화번호 목록|91점|91.7점|100점|C++|
|3|2022.1.21|해시_위장|96.4점|100점|---|Python|



-------------------------------------------------

#### 2. 해시_전화번호 목록

✨ 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.
예를 들어 ["1235", "123", "12348", "012"]을 입력으로 받으면, sorted(["1235", "123", "12348", "012"])는 ["012", "123", "12348", "1235"]가 된다. ✨


#### 3. 해시_위장

✨ 조합을 사용할 필요가 없이, 선택하지 않은 경우를 고려하여 +1을 생각한다. 예를 들어 headgear에 ["yellowhat", "green_turban"]가 존재한다면 이 경우의 수는 2가지가 아니라 headgear가 선택되지 않았을 경우까지 해서 3가지로 생각한다. 그리고 **마지막에 모두 선택되지 않을 경우를 고려하여 -1을 해준다.** ✨
