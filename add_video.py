#!/usr/bin/env python3
"""
Video Link Updater for LeetCode Repository

This script helps you easily add video links to README files across all directories
when you create tutorial videos for LeetCode problems.

Usage:
    python add_video.py "problem name" "video_url"
    python add_video.py "Two Sum" "https://youtube.com/watch?v=abc123"

The script will:
1. Search all README files for the matching problem
2. Update the Videos column in the table
3. Show you which files were updated

Example:
    python add_video.py "Container With Most Water" "https://youtu.be/UuiTKBwPgAo"
"""

import os
import sys
import re
import argparse
from typing import List, Tuple
from difflib import SequenceMatcher

def normalize_problem_name(name: str) -> str:
    """
    Normalize problem name for matching by removing special characters,
    converting to lowercase, and standardizing spacing.
    """
    # Remove common LeetCode problem number prefixes like "1. Two Sum"
    name = re.sub(r'^\d+\.\s*', '', name)
    
    # Convert to lowercase and replace special characters with spaces
    name = re.sub(r'[^\w\s]', ' ', name.lower())
    
    # Normalize whitespace
    name = ' '.join(name.split())
    
    return name

def similarity(a: str, b: str) -> float:
    """Calculate similarity between two strings."""
    return SequenceMatcher(None, normalize_problem_name(a), normalize_problem_name(b)).ratio()

def find_readme_files() -> List[str]:
    """Find all README.md files in the repository."""
    readme_files = []
    
    # Search in algorithms, data_structures, and patterns directories
    search_dirs = ['algorithms', 'data_structures', 'patterns']
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            for root, _, files in os.walk(search_dir):
                if 'README.md' in files:
                    readme_files.append(os.path.join(root, 'README.md'))
    
    return readme_files

def extract_problems_from_readme(readme_path: str) -> List[Tuple[str, str, int, str]]:
    """
    Extract problems from a README file.
    Returns list of (problem_name, problem_url, line_number, current_video) tuples.
    """
    problems = []
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for i, line in enumerate(lines):
            # Look for markdown table rows with problem links
            # Format: | [Problem Name](url) | Difficulty | Issues/Mistakes | Videos |
            match = re.search(r'\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|[^|]*\|[^|]*\|([^|]*)\|', line)
            if match:
                problem_name = match.group(1).strip()
                problem_url = match.group(2).strip()
                current_video = match.group(3).strip()
                problems.append((problem_name, problem_url, i, current_video))
    
    except Exception as e:
        print(f"Error reading {readme_path}: {e}")
    
    return problems

def find_matching_problems(target_problem: str, threshold: float = 0.7) -> List[Tuple[str, str, str, int, str, float]]:
    """
    Find problems that match the target problem name across all README files.
    Returns list of (readme_path, problem_name, problem_url, line_number, current_video, similarity) tuples.
    """
    matches = []
    readme_files = find_readme_files()
    
    for readme_path in readme_files:
        problems = extract_problems_from_readme(readme_path)
        
        for problem_name, problem_url, line_num, current_video in problems:
            sim = similarity(target_problem, problem_name)
            if sim >= threshold:
                matches.append((readme_path, problem_name, problem_url, line_num, current_video, sim))
    
    # Sort by similarity (highest first)
    matches.sort(key=lambda x: x[5], reverse=True)
    
    return matches

def update_readme_with_video(readme_path: str, line_num: int, video_url: str) -> bool:
    """
    Update a specific line in a README file to add the video URL.
    Returns True if successful, False otherwise.
    """
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if line_num >= len(lines):
            print(f"Error: Line {line_num} doesn't exist in {readme_path}")
            return False
        
        original_line = lines[line_num]
        
        # Parse the current line to extract components
        match = re.search(r'(\|\s*\[[^\]]+\]\([^)]+\)\s*\|[^|]*\|[^|]*\|)([^|]*)\|', original_line)
        if not match:
            print(f"Error: Could not parse table format in {readme_path} at line {line_num + 1}")
            return False
        
        prefix = match.group(1)
        
        # Create the video link markdown
        if video_url.strip():
            video_link = f" [Video]({video_url}) "
        else:
            video_link = " "
        
        # Reconstruct the line
        new_line = f"{prefix}{video_link}|\n"
        lines[line_num] = new_line
        
        # Write back to file
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
    
    except Exception as e:
        print(f"Error updating {readme_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Add video links to LeetCode problem README files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python add_video.py "Two Sum" "https://youtu.be/abc123"
  python add_video.py "Container With Most Water" "https://youtube.com/watch?v=xyz789"
  python add_video.py "Binary Search" ""  # Remove video link
        """
    )
    
    parser.add_argument("problem_name", help="Name of the LeetCode problem")
    parser.add_argument("video_url", help="URL of the video (use empty string to remove)")
    parser.add_argument("--threshold", type=float, default=0.7, 
                       help="Similarity threshold for matching problems (0.0-1.0, default: 0.7)")
    parser.add_argument("--dry-run", action="store_true", 
                       help="Show what would be updated without making changes")
    
    args = parser.parse_args()
    
    if not args.problem_name.strip():
        print("Error: Problem name cannot be empty")
        return 1
    
    print(f"Searching for problem: '{args.problem_name}'")
    print(f"Video URL: '{args.video_url}'")
    print(f"Similarity threshold: {args.threshold}")
    print()
    
    # Find matching problems
    matches = find_matching_problems(args.problem_name, args.threshold)
    
    if not matches:
        print("No matching problems found.")
        print("\nTips:")
        print("- Try a shorter or more general problem name")
        print("- Check the spelling")
        print("- Lower the threshold with --threshold 0.5")
        return 1
    
    print(f"Found {len(matches)} matching problem(s):\n")
    
    updated_count = 0
    
    for i, (readme_path, problem_name, problem_url, line_num, current_video, sim) in enumerate(matches):
        print(f"{i + 1}. {problem_name}")
        print(f"   File: {readme_path}")
        print(f"   Similarity: {sim:.2%}")
        print(f"   Current video: {'None' if not current_video.strip() else current_video}")
        print(f"   New video: {'Remove' if not args.video_url.strip() else args.video_url}")
        
        if args.dry_run:
            print("   [DRY RUN - No changes made]")
        else:
            if update_readme_with_video(readme_path, line_num, args.video_url):
                print("   ✅ Updated successfully")
                updated_count += 1
            else:
                print("   ❌ Update failed")
        
        print()
    
    if not args.dry_run:
        print(f"Successfully updated {updated_count} out of {len(matches)} README files.")
    else:
        print(f"Dry run completed. Would update {len(matches)} README files.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())