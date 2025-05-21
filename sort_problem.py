#!/usr/bin/env python3
"""
LeetCode Problem Sorter

This script helps sort LeetCode solution files into the appropriate directories based on:
1. Difficulty level (easy, medium, hard)
2. Data structures used (arrays, linked_lists, trees, graphs, hash_tables, heaps)
3. Algorithm patterns (two_pointers, sliding_window, dynamic_programming, binary_search)

The script uses OpenAI API to automatically classify problems.

Usage:
    python sort_problem.py <file_path> <leetcode_url> [--api-key <your_openai_api_key>]

You can also store your OpenAI API key in a .env file with:
OPENAI_API_KEY=your_api_key_here

Example:
    python sort_problem.py contains_duplicate.cpp https://leetcode.com/problems/contains-duplicate/description/
"""

import os
import sys
import argparse
import shutil
import re
import json
import subprocess
from typing import Dict, List, Tuple, Optional, Any

# Define flag to check if OpenAI is available
OPENAI_AVAILABLE = False
REQUESTS_AVAILABLE = False
DOTENV_AVAILABLE = False

# Try to import the packages
try:
    import requests  # type: ignore
    REQUESTS_AVAILABLE = True
except ImportError:
    pass

try:
    import openai  # type: ignore
    OPENAI_AVAILABLE = True
except ImportError:
    pass

try:
    from dotenv import load_dotenv  # type: ignore
    DOTENV_AVAILABLE = True
except ImportError:
    pass

# Function to check and suggest package installation
def check_required_packages():
    missing_packages = []
    
    if not REQUESTS_AVAILABLE:
        missing_packages.append("requests")
    
    if not OPENAI_AVAILABLE:
        missing_packages.append("openai")
        
    if not DOTENV_AVAILABLE:
        missing_packages.append("python-dotenv")
    
    if missing_packages:
        print("\nMissing required packages:", ", ".join(missing_packages))
        print("OpenAI package is required for this script to work.")
        print("To install required packages, run:")
        print(f"    pip install {' '.join(missing_packages)}")
        
        try:
            install = input("\nWould you like to install them now? (y/n): ").lower().strip()
            if install == 'y':
                for package in missing_packages:
                    try:
                        print(f"Installing {package}...")
                        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                        print(f"{package} installed successfully.")
                    except Exception as e:
                        print(f"Error installing {package}: {e}")
                
                print("\nPlease restart the script to use the newly installed packages.")
                sys.exit(0)
            else:
                print("Required packages are needed. Exiting.")
                sys.exit(1)
        except Exception:
            print("Required packages are needed. Exiting.")
            sys.exit(1)
    else:
        print("All required packages are already installed.")

def load_api_key_from_env():
    """
    Load the OpenAI API key from the .env file.
    
    Returns:
        The API key if found, None otherwise.
    """
    if not DOTENV_AVAILABLE:
        print("python-dotenv package is not available. Cannot load API key from .env file.")
        return None
        
    # Look for .env in current directory and up to two parent directories
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    grandparent_dir = os.path.dirname(parent_dir)
    
    env_paths = [
        os.path.join(current_dir, '.env'),
        os.path.join(parent_dir, '.env'),
        os.path.join(grandparent_dir, '.env')
    ]
    
    # Try loading with dotenv first
    for env_path in env_paths:
        if os.path.exists(env_path):
            load_dotenv(env_path)
            api_key = os.environ.get("OPENAI_API_KEY")
            if api_key:
                return api_key
    
    # If that fails, try manually parsing the .env file
    for env_path in env_paths:
        if os.path.exists(env_path):
            try:
                with open(env_path, 'r') as f:
                    for line in f:
                        # Strip comments and whitespace
                        line = line.strip()
                        if line.startswith('//') or line.startswith('#'):
                            continue
                        if '=' in line:
                            key, value = line.split('=', 1)
                            if key.strip() == "OPENAI_API_KEY" and value.strip():
                                return value.strip()
            except Exception as e:
                print(f"Error reading {env_path}: {e}")
    
    return None

# Define the repository structure
DIFFICULTY_DIRS = {
    "easy": "algorithms/easy",
    "medium": "algorithms/medium",
    "hard": "algorithms/hard"
}

DATA_STRUCTURE_DIRS = {
    "array": "data_structures/arrays",
    "linked list": "data_structures/linked_lists", 
    "tree": "data_structures/trees",
    "graph": "data_structures/graphs",
    "hash table": "data_structures/hash_tables",
    "heap": "data_structures/heaps"
}

PATTERN_DIRS = {
    "two pointers": "patterns/two_pointers",
    "sliding window": "patterns/sliding_window",
    "dynamic programming": "patterns/dynamic_programming",
    "binary search": "patterns/binary_search"
}

def get_problem_info_from_leetcode(url: str) -> Dict:
    """
    Extract problem title and difficulty from LeetCode URL by parsing the URL.
    
    Returns:
        Dict with 'title' and 'difficulty'
    """
    try:
        # Extract problem slug from URL
        match = re.search(r'problems/([^/]+)/', url)
        if not match:
            return {"title": None, "difficulty": None}
        
        problem_slug = match.group(1)
        
        # Convert slug to title
        title = problem_slug.replace('-', ' ').title()
        
        # We can't reliably determine difficulty without API, so we'll need to use API or user input
        return {"title": title, "difficulty": None}
    except Exception as e:
        print(f"Error extracting problem info from URL: {e}")
        return {"title": None, "difficulty": None}

def classify_with_openai(api_key: str, file_path: str, problem_url: str) -> Tuple[str, List[str], List[str]]:
    """
    Use OpenAI API to classify the problem's difficulty, data structures, and algorithm patterns.
    
    Returns:
        Tuple of (difficulty, list of data structures, list of algorithm patterns)
    """
    # Check if the openai module is available
    if not OPENAI_AVAILABLE:
        print("OpenAI module is not available. Please install it with:")
        print("    pip install openai")
        sys.exit(1)
    
    # If we get here, openai module is available
    openai.api_key = api_key
    
    # Read the file contents
    with open(file_path, 'r') as f:
        code_content = f.read()
    
    # Extract problem title from URL
    problem_info = get_problem_info_from_leetcode(problem_url)
    problem_title = problem_info["title"] or "Unknown Problem"
      # Prepare the prompt for OpenAI
    prompt = f"""
    Analyze this LeetCode solution for the problem "{problem_title}":
    
    {code_content}
    
    Based on the code and the problem URL ({problem_url}), answer the following questions:
    1. What is the difficulty level of this problem? (easy, medium, or hard)
    2. What data structures are used in this solution? Common examples include: array, linked list, tree, graph, hash table, heap, stack, queue, trie, etc. But identify ANY data structure being used.
    3. What algorithm patterns are used in this solution? Common examples include: two pointers, sliding window, dynamic programming, binary search, etc. But identify ANY algorithm pattern being used.
    
    Format your response as a JSON object with the following structure:
    {{
        "difficulty": "easy",  // or "medium" or "hard"
        "data_structures": ["array", "hash table"],  // list all that apply
        "patterns": ["two pointers"]  // list all that apply
    }}
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are an expert algorithm analyzer focusing only on identifying difficulty levels, data structures, and algorithm patterns in LeetCode solutions."},
                {"role": "user", "content": prompt}
            ]
        )
        
        result = json.loads(response.choices[0].message.content)
        return (
            result.get("difficulty", "").lower() or "easy",
            [ds.lower() for ds in result.get("data_structures", [])],
            [pattern.lower() for pattern in result.get("patterns", [])]
        )
    except Exception as e:
        print(f"Error using OpenAI API: {e}")
        print("Cannot proceed without OpenAI classification.")
        sys.exit(1)

# Function removed as we're only using OpenAI for classification now

def update_readme_with_problem(dest_dir: str, problem_title: str, problem_url: str, difficulty: str) -> None:
    """
    Update the README.md file in the destination directory to include the new problem.
    Creates a README if it doesn't exist.
    """
    readme_path = os.path.join(dest_dir, "README.md")
    
    # Determine the category name from the directory path
    category_parts = dest_dir.split(os.sep)
    category_name = category_parts[-1].replace('_', ' ').title()
    
    # Check if README exists and read its content
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as f:
            content = f.read()
        
        # Check if the problem is already in the README
        if problem_url in content:
            return  # Problem already listed
        
        # Check if the README has a LeetCode Problems section
        if "## LeetCode Problems" in content:
            # Find the problems table and add the new problem
            if "| Problem | Difficulty |" in content:
                # Add the new problem to the table
                problem_entry = f"\n| [{problem_title}]({problem_url}) | {difficulty.title()} |"
                # Find the position where we should insert the new entry (after the table header and separator)
                table_start = content.find("| Problem | Difficulty |")
                table_end = content.find("##", table_start)
                if table_end == -1:  # No section after the table
                    table_end = len(content)
                
                # Insert the problem entry right before the next section
                updated_content = content[:table_end] + problem_entry + content[table_end:]
                
                with open(readme_path, 'w') as f:
                    f.write(updated_content)
            else:
                # Create a new table in the LeetCode Problems section
                problems_section_start = content.find("## LeetCode Problems")
                next_section = content.find("##", problems_section_start + 1)
                if next_section == -1:
                    next_section = len(content)
                
                problem_table = f"\n\n| Problem | Difficulty |\n|---------|------------|\n| [{problem_title}]({problem_url}) | {difficulty.title()} |"
                
                updated_content = content[:next_section] + problem_table + content[next_section:]
                with open(readme_path, 'w') as f:
                    f.write(updated_content)
        else:
            # Add a new LeetCode Problems section at the end
            problem_section = f"\n\n## LeetCode Problems\n\n| Problem | Difficulty |\n|---------|------------|\n| [{problem_title}]({problem_url}) | {difficulty.title()} |"
            
            with open(readme_path, 'a') as f:
                f.write(problem_section)
    else:
        # Create a new README file
        with open(readme_path, 'w') as f:
            f.write(f"# {category_name}\n\n")
            f.write(f"This directory contains LeetCode problems related to {category_name.lower()}.\n\n")
            f.write("## LeetCode Problems\n\n")
            f.write("| Problem | Difficulty |\n")
            f.write("|---------|------------|\n")
            f.write(f"| [{problem_title}]({problem_url}) | {difficulty.title()} |")

def copy_file_to_destinations(file_path: str, destinations: List[str], problem_title: str, problem_url: str, difficulty: str) -> List[str]:
    """
    Copy the file to multiple destination directories, creating them if they don't exist.
    Updates README.md files in each directory to include the problem.
    Returns a list of paths where the file was copied to.
    """
    file_name = os.path.basename(file_path)
    copied_to = []
    
    for dest_dir in destinations:
        # Create the directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copy the file to the destination
        dest_path = os.path.join(dest_dir, file_name)
        shutil.copy2(file_path, dest_path)
        copied_to.append(dest_path)
        
        # Update the README file
        update_readme_with_problem(dest_dir, problem_title, problem_url, difficulty)
    
    return copied_to

def main():
    # Check for required packages first
    check_required_packages()
    
    parser = argparse.ArgumentParser(description="Sort LeetCode problems into appropriate directories")
    parser.add_argument("file_path", help="Path to the solution file")
    parser.add_argument("leetcode_url", help="URL of the LeetCode problem")
    parser.add_argument("--api-key", help="OpenAI API key for classification (optional if set in .env file)")
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.file_path):
        print(f"Error: File '{args.file_path}' not found.")
        return 1
      # Get API key from command line or .env file
    api_key = args.api_key
    if not api_key:
        api_key = load_api_key_from_env()
        
    if not api_key:
        print("Error: OpenAI API key is required.")
        print("Please either:")
        print("1. Provide it with --api-key parameter")
        print("2. Create a .env file with OPENAI_API_KEY=your_api_key")
        return 1
    
    destinations = []
    # Use OpenAI API for classification
    print("Using OpenAI API to classify the problem...")
    difficulty, data_structures, patterns = classify_with_openai(api_key, args.file_path, args.leetcode_url)
    # Add difficulty directory to destinations
    if difficulty and difficulty in DIFFICULTY_DIRS:
        destinations.append(DIFFICULTY_DIRS[difficulty])
    
    # Add data structure directories to destinations
    for ds in data_structures:
        if ds in DATA_STRUCTURE_DIRS:
            destinations.append(DATA_STRUCTURE_DIRS[ds])
        else:
            # Create a new folder path for this data structure
            # Convert to snake_case and plural form for consistency
            ds_folder_name = ds.lower().replace(' ', '_') + 's'
            new_ds_path = f"data_structures/{ds_folder_name}"
            destinations.append(new_ds_path)
            print(f"Creating new data structure directory for '{ds}': {new_ds_path}")
    
    # Add algorithm pattern directories to destinations
    for pattern in patterns:
        if pattern in PATTERN_DIRS:
            destinations.append(PATTERN_DIRS[pattern])
        else:
            # Create a new folder path for this pattern
            # Convert to snake_case for consistency
            pattern_folder_name = pattern.lower().replace(' ', '_')
            new_pattern_path = f"patterns/{pattern_folder_name}"
            destinations.append(new_pattern_path)
            print(f"Creating new algorithm pattern directory for '{pattern}': {new_pattern_path}")
      # Get problem title from URL
    problem_info = get_problem_info_from_leetcode(args.leetcode_url)
    problem_title = problem_info["title"] or os.path.basename(args.file_path).replace(".cpp", "").replace("_", " ").title()
      # Copy the file to all destination directories
    if destinations:
        copied_to = copy_file_to_destinations(args.file_path, destinations, problem_title, args.leetcode_url, difficulty or "easy")
        print(f"\nFile '{args.file_path}' was copied to:")
        
        # Group by directory type for better reporting
        existing_dirs = set(list(DIFFICULTY_DIRS.values()) + list(DATA_STRUCTURE_DIRS.values()) + list(PATTERN_DIRS.values()))
        new_dirs = []
        standard_dirs = []
        
        for path in copied_to:
            if os.path.dirname(path) in existing_dirs:
                standard_dirs.append(path)
            else:
                new_dirs.append(path)
                
        # Print standard directories first if any
        if standard_dirs:
            print("  Standard directories:")
            for path in standard_dirs:
                print(f"    - {path}")
                
        # Print new directories created for this classification
        if new_dirs:
            print("  Newly created directories:")
            for path in new_dirs:
                print(f"    - {path}")
                
        print("\nREADME.md files have been created/updated in each directory.")
    else:
        print("\nNo valid destinations were identified. The file was not copied.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
