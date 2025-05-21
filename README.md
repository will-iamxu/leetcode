# LeetCode Practice Repository

This repository is designed to help you practice and improve your coding skills through various LeetCode problems. It is organized into sections based on algorithms, data structures, and common coding patterns.

## Project Structure

- **algorithms/**: Contains folders for different difficulty levels of LeetCode problems.
  - **easy/**: Descriptions and solutions for easy-level problems.
  - **medium/**: Descriptions and solutions for medium-level problems.
  - **hard/**: Descriptions and solutions for hard-level problems.

- **data_structures/**: Contains folders for different data structures.
  - **arrays/**: Information and examples related to arrays.
  - **linked_lists/**: Information and examples related to linked lists.
  - **trees/**: Information and examples related to trees.
  - **graphs/**: Information and examples related to graphs.
  - **hash_tables/**: Information and examples related to hash tables.
  - **heaps/**: Information and examples related to heaps.

- **patterns/**: Contains folders for common coding patterns.
  - **two_pointers/**: Explanations and examples of the two pointers pattern.
  - **sliding_window/**: Explanations and examples of the sliding window pattern.
  - **dynamic_programming/**: Explanations and examples of the dynamic programming pattern.
  - **binary_search/**: Explanations and examples of the binary search pattern.

- **utils/**: Contains utility functions that can be used across different algorithms and data structures.

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install required dependencies: `pip install -r requirements.txt`
4. Use the utility scripts to create and organize your LeetCode solutions.

### Utility Scripts

This repository includes several scripts to help manage your LeetCode practice:

#### 1. Create New Solutions

Create a new solution file with the proper template for your preferred language.

**Using the batch script (Windows):**
```
create_solution.bat
```

**Using the Python script directly:**
```
python utils/create_solution.py "Problem Name" --language cpp --url https://leetcode.com/problems/problem-slug/
```

#### 2. Find LeetCode Problems

Search for LeetCode problems by name to get their URLs and difficulty levels.

**Using the batch script (Windows):**
```
find_problem.bat
```

**Using the Python script directly:**
```
python utils/find_problem.py "problem name"
```

#### 3. Automatic Problem Sorting

Sort your LeetCode solutions into the appropriate directories based on difficulty level and algorithms/data structures used.

**Using the batch script (Windows):**
```
sort_leetcode.bat
```

**Using the Python script directly:**
```
python utils/sort_problem.py your_solution.cpp https://leetcode.com/problems/problem-name/ --api-key YOUR_OPENAI_API_KEY
```

Or for manual classification:
```
python utils/sort_problem.py your_solution.cpp https://leetcode.com/problems/problem-name/ --manual
```

#### 4. OpenAI Integration

The sorting script can use OpenAI's API to automatically determine the algorithm and data structure used in your solution.

**Setting up OpenAI API key:**
```
python utils/helpers.py --setup-api
```

This will store your API key in a `.env` file (which is gitignored).

## Contributing

Feel free to contribute by adding new problems, solutions, or improving existing documentation. Please ensure that your contributions adhere to the project's structure.

## License

This project is open-source and available under the MIT License.