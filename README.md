# Affordable-vacation-code-wars
Solution to the "Affordable Vacation" Problem on CodeWars 
![image](https://github.com/user-attachments/assets/e0d4935f-c680-4123-996c-e60a27adb352)


The student has big plans for summer vacation after a stressful academic year. He has saved up some `money` and decided to travel to a neighboring city for a few **_consecutive_** `days`. Inspired by the desire to spend time in a new place, he compiled a list of housing rental costs for each of the anticipated days and recorded them in an array named `cost`.

Task
Find the cheapest accommodation for student's vacation.
It is guaranteed that the length of the cost array is greater than or equal to the duration of the vacation.

If there is enough money for travelling, return the answer in the format:
```"money: {minimum_money_for_vacation}"```
Otherwise, return the maximum duration of the vacation in the format:
```"days: {maximum_duration_of_vacation}"```
Help the student find the optimal solution for his summer vacation!

```Examples
| money | days | cost          | result      |
|-------|------|---------------|-------------|
| 10    | 1    | [5]           | "money: 5"  |
| 10    | 1    | [3, 2, 4]     | "money: 2"  |
| 10    | 2    | [3, 7, 6]     | "money: 10" |
| 10    | 1    | [20, 15, 30]  | "days: 0"   |
| 10    | 2    | [9, 6, 7, 4]  | "days: 1"   |
| 50    | 3    | [10, 40, 5]   | "days: 2"   |
```
Constraints for random tests (depends on language)
```
|                      | small   | medium | extra_large  |
|----------------------|---------|--------|--------------|
| tests                | 10      | 10     | 10           |
| money                | 1-10    | 1-50   | 1 to 30-300M |
| days                 | 1-4     | 1-20   | 1 to 0.03-3M |
| cost.length          | 1-10    | 1-50   | 1 to 0.1-15M |
| cost[i]              | 1-10    | 1-10   | 1 to 400     |
| cost.length >= days  | true    | true   | true         |
Solutions with a time complexity slower than O(n) will fail to pass extra large tests
```
