#!/usr/bin/env python3
"""
Helper functions for LeetCode practice repository
"""

import os
import sys
import argparse
import subprocess
from typing import Dict, List, Tuple, Optional

def print_repository_structure():
    """Print the repository structure for easy reference"""
    print("""
Repository Structure:
- algorithms/
  - easy/
  - medium/
  - hard/
- data_structures/
  - arrays/
  - linked_lists/
  - trees/
  - graphs/
  - hash_tables/
  - heaps/
- patterns/
  - two_pointers/
  - sliding_window/
  - dynamic_programming/
  - binary_search/
    """)

def setup_api_key():
    """Help user set up OpenAI API key for the sorter script"""
    print("Setting up OpenAI API key for automatic problem classification")
      # Check if openai package is installed
    try:
        import openai  # type: ignore
        print("OpenAI package is installed.")
    except ImportError:
        print("OpenAI package is not installed. Installing it now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])
        print("OpenAI package installed successfully.")
    
    api_key = input("Enter your OpenAI API key: ").strip()
    
    if not api_key:
        print("No API key provided. Exiting.")
        return
    
    # Create .env file to store the API key
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    with open(env_path, 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
    
    print(f"\nAPI key saved to {env_path}")
    print("This file is gitignored and won't be committed.")
    print("You can now use the sort_problem.py script with automatic classification.")

def add_video_link():
    """Add a video link to README files for a specific problem"""
    print("Use the add_video.py script to add video links:")
    print("  python3 add_video.py \"Problem Name\" \"video_url\"")
    print("\nExamples:")
    print("  python3 add_video.py \"Two Sum\" \"https://youtu.be/abc123\"")
    print("  python3 add_video.py \"Container With Most Water\" \"https://youtube.com/watch?v=xyz789\"")
    print("  python3 add_video.py \"Binary Search\" \"\"  # Remove video link")
    print("\nOptions:")
    print("  --dry-run    Show what would be updated without making changes")
    print("  --threshold  Set similarity threshold (default: 0.7)")

def main():
    parser = argparse.ArgumentParser(description="Helper utilities for LeetCode practice")
    parser.add_argument("--structure", action="store_true", help="Print the repository structure")
    parser.add_argument("--setup-api", action="store_true", help="Set up OpenAI API key")
    parser.add_argument("--add-video", action="store_true", help="Help with adding video links")
    
    args = parser.parse_args()
    
    if args.structure:
        print_repository_structure()
    elif args.setup_api:
        setup_api_key()
    elif args.add_video:
        add_video_link()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
