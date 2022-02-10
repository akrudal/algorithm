## 알고리즘

---

<공부 일정>

| 순차시 | 날짜      | 내용                     | 1차 시도 | 2차 시도 | 3차 시도 | 사용 언어 |
| ------ | --------- | ------------------------ | -------- | -------- | -------- | --------- |
| 1      | 2022.1.19 | 해시\_완주하지 못한 선수 | 50점     | 100점    | 100점    | C++       |
| 2      | 2022.1.20 | 해시\_전화번호 목록      | 91점     | 91.7점   | 100점    | C++       |
| 3      | 2022.1.21 | 해시\_위장               | 96.4점   | 100점    | ---      | Python    |
| 4      | 2022.1.22 | 해시\_베스트앨범         | 100점    | 100점    | ---      | Python    |
| 5      | 2022.1.23 | 스택/큐\_기능개발        | 0점      | 100점    | ---       |C++       |
| 6      | 2022.1.24 | 스택/큐\_프린터         | 0점     | 0점    | 100점      | Python    |
| 7      | 2022.1.27 | 스택/큐\_다리를 지나는 트럭| ---    | ---    | ---      | Python    |
| 8      | 2022.1.31 | 스택/큐\_주식가격        | 100점    | ---    | ---      | Python    |
| 9      | 2022.2.3 | 힙\_더 맵게         | ---    | ---    | ---      | Python    |
| 10      | 2022.2.4 | 힙\_디스크 컨트롤러         | 0점    | 60점    | 100점      | Python    |
| 11      | 2022.2.7 | 힙\_이중우선순위큐         | 100점    | ---    | ---      | Python    |
| 12     | 2022.2.8 | 정렬\_K번째 수         | 100점    | ---    | ---      | Python    |
| 13     | 2022.2.9 | 정렬\_가장 큰 수        | 80점    | 100점    | 100점      | Python    |
|14|2022.2.10|정렬\_H-index|100점|---|---|Python|
---

#### 2. 해시\_전화번호 목록

✨ 만약에 어떤 번호가 다른 번호의 접두어라면 이 둘은 정렬했을 때 앞뒤에 위치하게 된다.
예를 들어 ["1235", "123", "12348", "012"]을 입력으로 받으면, sorted(["1235", "123", "12348", "012"])는 ["012", "123", "12348", "1235"]가 된다. ✨

#### 3. 해시\_위장

✨ 조합을 사용할 필요가 없이, 선택하지 않은 경우를 고려하여 +1을 생각한다. 예를 들어 headgear에 ["yellowhat", "green_turban"]가 존재한다면 이 경우의 수는 2가지가 아니라 headgear가 선택되지 않았을 경우까지 해서 3가지로 생각한다. 그리고 **마지막에 모두 선택되지 않을 경우를 고려하여 -1을 해준다.** ✨


#### 13. 정렬\_가장 큰 수

✨ 숫자의 범위가 1000까지인 것을 이용하여, 자릿수가 4가 되게 숫자를 반복해준다. 또한, [0,0,0...] 이 들어올 경우를 생각하여 방어처리를 해준다. ✨


#### 14. 정렬\_H-index

✨ testcase[1,4]를 주의깊게 살펴보자. 이 테스트케이스에 대한 답은 1인데, 2로 나오는 코드로 제출했음에도 불구하고 통과가 되었다!  예외적인 사항에 대비해준다. ✨
