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

## Getting Started

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install required dependencies: `pip install -r requirements.txt`
4. Use the utility scripts to create and organize your LeetCode solutions.

### Utility Scripts

This repository includes several scripts to help manage your LeetCode practice:

#### 1. Automatic Problem Sorting

Sort your LeetCode solutions into the appropriate directories based on difficulty level and algorithms/data structures used.

**Using the Python script directly:**
```
python sort_problem.py your_solution.cpp https://leetcode.com/problems/problem-name/ --api-key YOUR_OPENAI_API_KEY
```

#### 2. OpenAI Integration

The sorting script can use OpenAI's API to automatically determine the algorithm and data structure used in your solution.

**Setting up OpenAI API key:**
```
python helpers.py --setup-api
```

This will store your API key in a `.env` file (which is gitignored).

#### 3. Repository Structure

To view the structure of the repository for easy reference:

```
python helpers.py --structure
```

This will output the organized folder structure of this repository.

## Contributing

Feel free to contribute by adding new problems, solutions, or improving existing documentation. Please ensure that your contributions adhere to the project's structure.

## License

This project is open-source and available under the MIT License.

## Issues
*Issues encountered while solving problems in this category (leave blank for now)*

## Videos  
*Helpful video resources for problems in this category (leave blank for now)*