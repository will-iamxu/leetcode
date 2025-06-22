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
    "binary search": "patterns/binary_search",
    "depth-first search": "patterns/depth-first_search_(dfs)",
    "breadth-first search": "patterns/breadth_first_search_(bfs)",
    "backtracking": "patterns/backtracking",
    "greedy": "patterns/greedy",
    "divide and conquer": "patterns/divide_and_conquer",
    "monotonic stack": "patterns/monotonic_stack",
    "prefix sum": "patterns/prefix_sum",
    "suffix sum": "patterns/suffix_sum"
}

# Define mappings to standardize terminology between similar concepts
# Maps variant names to the standard name in one of the directories above
TERM_MAPPING = {
    # Data structure aliases
    "hash map": "hash table",
    "hashmap": "hash table",
    "hashtable": "hash table",
    "dictionary": "hash table",
    "map": "hash table",
    
    "linked-list": "linked list",
    
    "arrays": "array",
    "vector": "array",
    "list": "array",
    
    "binary tree": "tree",
    "binary search tree": "tree",
    "bst": "tree",
    "avl tree": "tree",
    "red-black tree": "tree",
    "trie": "tree",  # Consider if you want trie as a separate structure
    
    "priority queue": "heap",
    "min heap": "heap",
    "max heap": "heap",
    
    "directed graph": "graph",
    "undirected graph": "graph",
    "dag": "graph",  # Directed Acyclic Graph
    
    # Pattern aliases
    "2 pointers": "two pointers",
    "dp": "dynamic programming",
    "memoization": "dynamic programming",
    
    "binary": "binary search",
    "binary search algorithm": "binary search",
    
    "sliding-window": "sliding window",
    "window sliding": "sliding window",
    
    # DFS/BFS aliases
    "dfs": "depth-first search",
    "depth first search": "depth-first search",
    "depth-first-search": "depth-first search",
    "depth_first_search": "depth-first search",
    "bfs": "breadth-first search",
    "breadth first search": "breadth-first search",
    "breadth-first-search": "breadth-first search",
    "breadth_first_search": "breadth-first search",
}

# Define which terms should be treated explicitly as data structures vs patterns
# This helps when a term could be classified as either
DATA_STRUCTURE_TYPES = {
    "array", "linked list", "tree", "graph", "hash table", "heap", "stack", "queue", "trie"
}

PATTERN_TYPES = {
    "two pointers", "sliding window", "dynamic programming", "binary search", 
    "greedy", "backtracking", "depth-first search", "breadth-first search",
    "divide and conquer", "monotonic stack", "prefix sum", "suffix sum"
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
    problem_title = problem_info["title"] or "Unknown Problem"    # Prepare the prompt for OpenAI
    prompt = f"""
    Analyze this LeetCode solution for the problem "{problem_title}":
    
    {code_content}
    
    Based on the code and the problem URL ({problem_url}), answer the following questions:
    1. What is the difficulty level of this problem? (easy, medium, or hard)
    
    2. What data structures are primarily used in this solution?
       Common examples include:
       - array/list
       - linked list
       - tree (including binary tree, BST, trie)
       - graph
       - hash table/hash map/dictionary
       - heap/priority queue
       - stack
       - queue
       
    3. What algorithm patterns are used in this solution?
       Common examples include:
       - two pointers
       - sliding window
       - dynamic programming
       - binary search
       - depth-first search (DFS)
       - breadth-first search (BFS)
       - greedy
       - backtracking
       
    Distinguish clearly between data structures (what we use to store data) and algorithm patterns (approaches to solve problems).
    For example, a "hash table" is a data structure while "two pointers" is an algorithm pattern.
    
    Format your response as a JSON object with the following structure:
    {{
        "difficulty": "easy",  // or "medium" or "hard"
        "data_structures": ["array", "hash table"],  // list all data structures that apply
        "patterns": ["two pointers"]  // list all algorithm patterns that apply
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
        
        content = response.choices[0].message.content
        if content is None:
            raise ValueError("OpenAI API returned empty response")
        result = json.loads(content)
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
            if "| Problem | Difficulty | Issues/Mistakes | Videos |" in content:
                # Add the new problem to the table (new format)
                problem_entry = f"\n| [{problem_title}]({problem_url}) | {difficulty.title()} | | |"
                # Find the position where we should insert the new entry (after the table header and separator)
                table_start = content.find("| Problem | Difficulty | Issues/Mistakes | Videos |")
                table_end = content.find("##", table_start)
                if table_end == -1:  # No section after the table
                    table_end = len(content)
                
                # Insert the problem entry right before the next section
                updated_content = content[:table_end] + problem_entry + content[table_end:]
                
                with open(readme_path, 'w') as f:
                    f.write(updated_content)
            elif "| Problem | Difficulty |" in content:
                # Old format - convert to new format
                old_header = "| Problem | Difficulty |"
                old_separator = "|---------|------------|"
                new_header = "| Problem | Difficulty | Issues/Mistakes | Videos |"
                new_separator = "|---------|------------|-----------------|--------|"
                
                # Replace the header and separator
                content = content.replace(old_header, new_header)
                content = content.replace(old_separator, new_separator)
                
                # Add empty columns to existing entries
                lines = content.split('\n')
                updated_lines = []
                in_table = False
                
                for line in lines:
                    if "| Problem | Difficulty | Issues/Mistakes | Videos |" in line:
                        in_table = True
                        updated_lines.append(line)
                    elif in_table and line.startswith('|') and not line.startswith('|------'):
                        # This is a table row, check if it needs updating
                        if line.count('|') == 3:  # Old format with 3 separators
                            # Add two empty columns
                            line = line.rstrip() + " | |"
                        updated_lines.append(line)
                    elif in_table and (line.startswith('##') or line.strip() == ''):
                        # End of table
                        in_table = False
                        # Add the new problem entry before ending the table
                        if line.startswith('##'):
                            updated_lines.append(f"| [{problem_title}]({problem_url}) | {difficulty.title()} | | |")
                        updated_lines.append(line)
                    else:
                        updated_lines.append(line)
                
                # If we didn't add the problem yet (table was at the end), add it now
                if in_table:
                    updated_lines.append(f"| [{problem_title}]({problem_url}) | {difficulty.title()} | | |")
                
                with open(readme_path, 'w') as f:
                    f.write('\n'.join(updated_lines))
            else:
                # Create a new table in the LeetCode Problems section
                problems_section_start = content.find("## LeetCode Problems")
                next_section = content.find("##", problems_section_start + 1)
                if next_section == -1:
                    next_section = len(content)
                
                problem_table = f"\n\n| Problem | Difficulty | Issues/Mistakes | Videos |\n|---------|------------|-----------------|--------|\n| [{problem_title}]({problem_url}) | {difficulty.title()} | | |"
                
                updated_content = content[:next_section] + problem_table + content[next_section:]
                with open(readme_path, 'w') as f:
                    f.write(updated_content)
        else:
            # Add a new LeetCode Problems section at the end
            problem_section = f"\n\n## LeetCode Problems\n\n| Problem | Difficulty | Issues/Mistakes | Videos |\n|---------|------------|-----------------|--------|\n| [{problem_title}]({problem_url}) | {difficulty.title()} | | |"
            
            with open(readme_path, 'a') as f:
                f.write(problem_section)
    else:
        # Create a new README file
        with open(readme_path, 'w') as f:
            f.write(f"# {category_name}\n\n")
            f.write(f"This directory contains LeetCode problems related to {category_name.lower()}.\n\n")
            f.write("## LeetCode Problems\n\n")
            f.write("| Problem | Difficulty | Issues/Mistakes | Videos |\n")
            f.write("|---------|------------|-----------------|--------|\n")
            f.write(f"| [{problem_title}]({problem_url}) | {difficulty.title()} | | |")

def normalize_directory_name(name: str, category: str) -> str:
    """
    Normalize directory name based on term mapping and category.
    
    Args:
        name: The name to normalize
        category: Either 'patterns' or 'data_structures'
    
    Returns:
        Normalized directory name
    """
    # Apply term mapping first
    normalized_name = TERM_MAPPING.get(name.lower(), name.lower())
    
    if category == 'patterns':
        # Check if it's already in PATTERN_DIRS
        if normalized_name in PATTERN_DIRS:
            return PATTERN_DIRS[normalized_name]
        # Handle special DFS/BFS cases
        elif normalized_name == "depth-first search":
            return "patterns/depth-first_search_(dfs)"
        elif normalized_name == "breadth-first search":
            return "patterns/breadth_first_search_(bfs)"
        else:
            # Convert to snake_case for consistency
            return f"patterns/{normalized_name.replace(' ', '_')}"
    elif category == 'data_structures':
        # Check if it's already in DATA_STRUCTURE_DIRS
        if normalized_name in DATA_STRUCTURE_DIRS:
            return DATA_STRUCTURE_DIRS[normalized_name]
        else:
            # Convert to snake_case and add plural form for consistency
            ds_folder_name = normalized_name.replace(' ', '_') + 's'
            return f"data_structures/{ds_folder_name}"
    
    return name  # fallback

def find_similar_existing_directory(proposed_path: str) -> Optional[str]:
    """
    Check if there's already a similar directory that exists with a different name.
    Returns the existing directory path if found, None otherwise.
    
    For example, if proposed_path is 'patterns/hash_map' and 'data_structures/hash_tables' exists,
    this function will return 'data_structures/hash_tables'.
    """
    # Extract the base name from the proposed path (e.g., 'hash_map' from 'patterns/hash_map')
    proposed_base_name = os.path.basename(proposed_path)
    
    # Check if this is possibly a renamed variant of an existing directory
    proposed_category = proposed_path.split('/')[0]  # e.g., 'patterns' or 'data_structures'
    similar_concepts = []
    
    # Build list of all defined directories
    all_dirs = list(DATA_STRUCTURE_DIRS.values()) + list(PATTERN_DIRS.values())
    
    # Find directories that might be similar based on the base name
    for existing_dir in all_dirs:
        existing_base = os.path.basename(existing_dir)
        # Convert to singular form for comparison if needed
        if existing_base.endswith('s'):
            existing_singular = existing_base[:-1]
        else:
            existing_singular = existing_base
            
        proposed_singular = proposed_base_name
        if proposed_singular.endswith('s'):
            proposed_singular = proposed_singular[:-1]
        
        # Check for similarity using some basic rules
        if (proposed_singular == existing_singular or
            proposed_singular.replace('_', '') == existing_singular.replace('_', '') or
            proposed_singular in existing_singular or
            existing_singular in proposed_singular):
            similar_concepts.append(existing_dir)
    
    # Check if the proposed directory is mapped to any existing path
    for term, standard_term in TERM_MAPPING.items():
        # Convert term to directory style
        term_as_dir = term.replace(' ', '_')
        if proposed_base_name == term_as_dir:
            # Check if this standard term has a directory
            if standard_term in DATA_STRUCTURE_DIRS:
                return DATA_STRUCTURE_DIRS[standard_term]
            elif standard_term in PATTERN_DIRS:
                return PATTERN_DIRS[standard_term]
    
    # Return the first similar existing directory, if any
    return similar_concepts[0] if similar_concepts else None

def copy_file_to_destinations(file_path: str, destinations: List[str], problem_title: str, problem_url: str, difficulty: str) -> List[str]:
    """
    Copy the file to multiple destination directories, creating them if they don't exist.
    Updates README.md files in each directory to include the problem.
    Returns a list of paths where the file was copied to.
    """
    file_name = os.path.basename(file_path)
    copied_to = []
    
    # Remove duplicate destinations if any
    unique_destinations = []
    for dest in destinations:
        if dest not in unique_destinations:
            unique_destinations.append(dest)
    
    for dest_dir in unique_destinations:
        # Check if there's a similar existing directory
        similar_dir = find_similar_existing_directory(dest_dir)
        
        # If we found a similar directory that already exists, use that instead
        if similar_dir and similar_dir != dest_dir and os.path.exists(similar_dir):
            print(f"Using existing similar directory '{similar_dir}' instead of creating '{dest_dir}'")
            dest_dir = similar_dir
        
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
      # Normalize data structures using mappings
    normalized_data_structures = []
    for ds in data_structures:
        ds_lower = ds.lower()
        if ds_lower in TERM_MAPPING:
            # If this is a known alias, map it to its standard form
            normalized_ds = TERM_MAPPING[ds_lower]
            print(f"Mapping '{ds}' to standard form '{normalized_ds}'")
            normalized_data_structures.append(normalized_ds)
        else:
            normalized_data_structures.append(ds_lower)
    
    # Normalize patterns using mappings
    normalized_patterns = []
    for pattern in patterns:
        pattern_lower = pattern.lower()
        if pattern_lower in TERM_MAPPING:
            # If this is a known alias, map it to its standard form
            normalized_pattern = TERM_MAPPING[pattern_lower]
            print(f"Mapping '{pattern}' to standard form '{normalized_pattern}'")
            normalized_patterns.append(normalized_pattern)
        else:
            normalized_patterns.append(pattern_lower)
    
    # Detect and resolve potential duplicates between data structures and patterns
    # Some terms might be classified by OpenAI as both a data structure and a pattern
    duplicates = set(normalized_data_structures) & set(normalized_patterns)
    for duplicate in duplicates:
        if duplicate in DATA_STRUCTURE_TYPES:
            # This is primarily a data structure, remove from patterns
            normalized_patterns = [p for p in normalized_patterns if p != duplicate]
            print(f"Resolving duplicate: '{duplicate}' classified as data structure")
        elif duplicate in PATTERN_TYPES:
            # This is primarily a pattern, remove from data structures
            normalized_data_structures = [ds for ds in normalized_data_structures if ds != duplicate]
            print(f"Resolving duplicate: '{duplicate}' classified as algorithm pattern")
        else:
            # If it's not explicitly defined, prefer data structure classification
            normalized_patterns = [p for p in normalized_patterns if p != duplicate]
            print(f"Resolving ambiguous duplicate: '{duplicate}' defaulting to data structure")
    
    # Add data structure directories to destinations
    for ds in normalized_data_structures:
        ds_path = normalize_directory_name(ds, 'data_structures')
        destinations.append(ds_path)
        if ds not in DATA_STRUCTURE_DIRS:
            print(f"Creating new data structure directory for '{ds}': {ds_path}")
    
    # Add algorithm pattern directories to destinations
    for pattern in normalized_patterns:
        pattern_path = normalize_directory_name(pattern, 'patterns')
        destinations.append(pattern_path)
        if pattern not in PATTERN_DIRS:
            print(f"Creating new algorithm pattern directory for '{pattern}': {pattern_path}")
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
        
        # Delete the original file after successful copying
        try:
            os.remove(args.file_path)
            print(f"\nOriginal file '{args.file_path}' has been deleted.")
        except Exception as e:
            print(f"\nWarning: Could not delete original file '{args.file_path}': {e}")
    else:
        print("\nNo valid destinations were identified. The file was not copied.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
