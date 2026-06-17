# Phase0---Projects
Phase 0 — Python fundamentals projects
# String & Number Toolkit

A Python CLI tool built as part of Phase 0 of my FDE Engineering roadmap.

## What it does
- Reverse any string
- Check if a word or phrase is a palindrome
- Find all prime numbers up to N
- Calculate factorial of a number using recursion
- Count word frequency in any text

## Concepts used
- Functions with default arguments, *args, **kwargs
- Recursion
- Dictionary manipulation
- String methods
- CLI menu with while loop

## How to run
python easy_project.py

## Example
Enter choice: 2
Enter string: Race Car
Is palindrome: True

# Student Grade Manager

A Python data pipeline built as part of Phase 0 of my FDE Engineering roadmap.

## What it does
- Reads student marks from a CSV file
- Calculates average marks per student
- Ranks students from highest to lowest average
- Finds the topper for each subject
- Writes a full summary report to a new CSV file

## Concepts used
- CSV reading and writing with DictReader and DictWriter
- Dictionary grouping and aggregation
- Sorting with lambda functions
- enumerate() for ranking
- File handling with context managers

## How to run
python Medium_Project.py

## Input format (students.csv)
name,subject,marks
Raj,Math,85
Raj,Science,90

## Output (summary.csv)
rank,name,average,topper_in_subject
1,Priya,90.0,Math
2,Raj,87.5,Science
3,Amit,80.0,None 