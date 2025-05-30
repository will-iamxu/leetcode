# Data Structures/Stacks

This directory contains LeetCode problems related to data structures/stacks.


## Implementation Examples

This section demonstrates how to use `std::stack` in C++.

```cpp
#include <stack>
#include <iostream>
using namespace std;

int main() {
    // Declare a stack of integers
    stack<int> s;

    // Push elements onto the stack
    s.push(10);
    s.push(20);
    s.push(30); // Stack is now [10, 20, 30] with 30 on top

    // Access the top element
    cout << "Top element: " << s.top() << endl; // Outputs 30

    // Remove the top element
    s.pop(); // Stack is now [10, 20]

    // Check if the stack is empty
    if (s.empty()) {
        cout << "Stack is empty." << endl;
    } else {
        cout << "Stack is not empty." << endl;
    }

    // Get the size of the stack
    cout << "Stack size: " << s.size() << endl; // Outputs 2

    // Iterate through the stack (must pop to access elements)
    cout << "Stack contents (from top to bottom): ";
    while (!s.empty()) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;

    // Using stack with custom data types
    struct Point {
        int x, y;
    };

    stack<Point> points;
    points.push({1, 2});
    points.push({3, 4});

    // Access custom object at the top
    Point p = points.top();
    cout << "Top point: (" << p.x << ", " << p.y << ")" << endl;

    return 0;
}
```
## LeetCode Problems

| Problem | Difficulty |
|---------|------------|
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) | Easy |
| [Min Stack](https://leetcode.com/problems/min-stack/) | Easy |
| [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/) | Medium |
| [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/) | Medium |