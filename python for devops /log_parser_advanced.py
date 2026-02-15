#!/usr/bin/env python3
"""
Advanced Log Parser - Shows more Python patterns for DevOps

This version demonstrates:
- Regular expressions for pattern matching
- Dictionary comprehensions
- List comprehensions
- Working with datetime
- Command-line arguments
"""

import re
from datetime import datetime
from collections import defaultdict, Counter


def parse_log_advanced(log_file_path):
    """
    Advanced log parser using regex and more sophisticated data structures.
    
    Returns:
        dict: Comprehensive analysis results
    """
    # defaultdict automatically creates missing keys with default values
    # This is cleaner than checking if keys exist
    stats = {
        'log_levels': defaultdict(int),
        'errors_by_type': Counter(),  # Counter is great for counting things
        'timeline': [],
        'ip_addresses': set(),  # Set automatically handles uniqueness
    }
    
    # Regex patterns - very useful for log parsing
    # Pattern to extract log level
    level_pattern = re.compile(r'\b(ERROR|WARNING|INFO|DEBUG|CRITICAL)\b')
    
    # Pattern to extract timestamp
    timestamp_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    
    # Pattern to find IP addresses
    ip_pattern = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
    
    # Pattern to categorize errors
    error_types = {
        'database': re.compile(r'database|mysql|postgres|redis|connection', re.IGNORECASE),
        'network': re.compile(r'network|timeout|unreachable|connection refused', re.IGNORECASE),
        'kubernetes': re.compile(r'kubernetes|k8s|pod|container|deployment', re.IGNORECASE),
        'disk': re.compile(r'disk|storage|partition|space', re.IGNORECASE),
    }
    
    try:
        with open(log_file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):  # enumerate gives us line numbers
                
                # Extract log level using regex
                level_match = level_pattern.search(line)
                if level_match:
                    level = level_match.group(1)
                    stats['log_levels'][level] += 1
                    
                    # Extract timestamp
                    time_match = timestamp_pattern.search(line)
                    if time_match:
                        timestamp = time_match.group(1)
                        stats['timeline'].append({
                            'timestamp': timestamp,
                            'level': level,
                            'line_num': line_num
                        })
                
                # Find IP addresses
                ip_matches = ip_pattern.findall(line)
                for ip in ip_matches:
                    stats['ip_addresses'].add(ip)  # set automatically deduplicates
                
                # Categorize errors
                if 'ERROR' in line:
                    categorized = False
                    for error_type, pattern in error_types.items():
                        if pattern.search(line):
                            stats['errors_by_type'][error_type] += 1
                            categorized = True
                            break
                    
                    if not categorized:
                        stats['errors_by_type']['other'] += 1
        
        return stats
    
    except Exception as e:
        print(f"Error processing file: {e}")
        return None


def analyze_patterns(stats):
    """
    Analyze patterns in the logs.
    
    Args:
        stats (dict): Statistics from parse_log_advanced
    """
    if not stats:
        return
    
    print("\n" + "="*60)
    print("ADVANCED LOG ANALYSIS")
    print("="*60)
    
    # Dictionary comprehension to calculate percentages
    total = sum(stats['log_levels'].values())
    if total > 0:
        percentages = {
            level: (count / total) * 100 
            for level, count in stats['log_levels'].items()
        }
        
        print("\nLog Level Distribution:")
        for level, percentage in sorted(percentages.items(), 
                                       key=lambda x: x[1], 
                                       reverse=True):
            count = stats['log_levels'][level]
            print(f"  {level:12} : {count:5} ({percentage:5.1f}%)")
    
    # Error categorization
    if stats['errors_by_type']:
        print("\nError Categories:")
        # most_common() is a Counter method that returns sorted list
        for category, count in stats['errors_by_type'].most_common():
            print(f"  {category:15} : {count}")
    
    # Unique IPs
    if stats['ip_addresses']:
        print(f"\nUnique IP addresses found: {len(stats['ip_addresses'])}")
        # List comprehension to format output
        ip_list = ', '.join(sorted(stats['ip_addresses']))
        print(f"  {ip_list}")
    
    # Timeline analysis
    if stats['timeline']:
        print(f"\nTotal log entries with timestamps: {len(stats['timeline'])}")
        
        # List comprehension to filter only errors
        errors_timeline = [
            entry for entry in stats['timeline'] 
            if entry['level'] == 'ERROR'
        ]
        
        if errors_timeline:
            print(f"  First error at line {errors_timeline[0]['line_num']}")
            print(f"  Last error at line {errors_timeline[-1]['line_num']}")


def filter_logs_by_time(log_file, start_hour, end_hour):
    """
    Example of filtering logs by time range.
    
    Args:
        log_file (str): Path to log file
        start_hour (int): Start hour (0-23)
        end_hour (int): End hour (0-23)
    
    Returns:
        list: Filtered log lines
    """
    filtered = []
    time_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} (\d{2}):\d{2}:\d{2})')
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                match = time_pattern.search(line)
                if match:
                    hour = int(match.group(2))
                    if start_hour <= hour <= end_hour:
                        filtered.append(line.strip())
    except Exception as e:
        print(f"Error: {e}")
    
    return filtered


def main():
    """Run the advanced parser."""
    log_file = "sample.log"
    
    print(f"Analyzing: {log_file}")
    
    # Run advanced analysis
    stats = parse_log_advanced(log_file)
    analyze_patterns(stats)
    
    # Example of time-based filtering
    print("\n" + "="*60)
    print("FILTERED VIEW: Logs from 10:00 to 11:00")
    print("="*60)
    morning_logs = filter_logs_by_time(log_file, 10, 11)
    print(f"Found {len(morning_logs)} entries in this time range")
    
    # Show first 3 using list slicing
    for log in morning_logs[:3]:
        print(f"  {log}")


if __name__ == "__main__":
    main()
