#!/usr/bin/env python3
"""
Log Parser - Task 1: Data Structures & File Operations

This script demonstrates:
- Reading files line by line
- Using dictionaries to count occurrences
- String operations and searching
- Writing output to files
- Working with lists and dictionaries
"""

def parse_log_file(log_file_path):
    """
    Parse a log file and count different types of log entries.
    
    Args:
        log_file_path (str): Path to the log file
        
    Returns:
        dict: Dictionary with counts of different log levels
    """
    # Dictionary to store counts - this is your main data structure
    log_counts = {
        'ERROR': 0,
        'WARNING': 0,
        'INFO': 0,
        'DEBUG': 0,
        'CRITICAL': 0
    }
    
    # List to store actual error messages for detailed reporting
    error_messages = []
    warning_messages = []
    
    # Total lines processed
    total_lines = 0
    
    # Open and read the file
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                total_lines += 1
                
                # Check for different log levels in the line
                # Using 'in' operator to search in strings
                if 'ERROR' in line:
                    log_counts['ERROR'] += 1
                    error_messages.append(line.strip())
                elif 'WARNING' in line or 'WARN' in line:
                    log_counts['WARNING'] += 1
                    warning_messages.append(line.strip())
                elif 'INFO' in line:
                    log_counts['INFO'] += 1
                elif 'DEBUG' in line:
                    log_counts['DEBUG'] += 1
                elif 'CRITICAL' in line:
                    log_counts['CRITICAL'] += 1
    
    except FileNotFoundError:
        print(f"Error: File {log_file_path} not found!")
        return None
    except PermissionError:
        print(f"Error: No permission to read {log_file_path}")
        return None
    
    # Return a dictionary with all the results
    return {
        'counts': log_counts,
        'total_lines': total_lines,
        'errors': error_messages,
        'warnings': warning_messages
    }


def print_summary(results):
    """
    Print a formatted summary of the log analysis.
    
    Args:
        results (dict): Results dictionary from parse_log_file
    """
    if results is None:
        return
    
    print("\n" + "="*50)
    print("LOG ANALYSIS SUMMARY")
    print("="*50)
    print(f"Total lines processed: {results['total_lines']}")
    print("\nLog Level Breakdown:")
    print("-"*50)
    
    # Iterate through dictionary items
    for level, count in results['counts'].items():
        # Format output with string formatting
        print(f"{level:12} : {count:5} occurrences")
    
    # Calculate percentage of errors
    total_logs = sum(results['counts'].values())
    if total_logs > 0:
        error_percentage = (results['counts']['ERROR'] / total_logs) * 100
        print(f"\nError rate: {error_percentage:.2f}%")
    
    # Show first 5 errors if any exist
    if results['errors']:
        print("\n" + "-"*50)
        print("Recent Errors (first 5):")
        print("-"*50)
        for error in results['errors'][:5]:  # List slicing
            print(f"  - {error[:100]}...")  # Truncate long lines


def save_report(results, output_file):
    """
    Save the analysis report to a file.
    
    Args:
        results (dict): Results dictionary from parse_log_file
        output_file (str): Path to output file
    """
    if results is None:
        return
    
    try:
        with open(output_file, 'w') as f:
            f.write("LOG ANALYSIS REPORT\n")
            f.write("="*50 + "\n\n")
            f.write(f"Total lines: {results['total_lines']}\n\n")
            
            f.write("Counts by level:\n")
            for level, count in results['counts'].items():
                f.write(f"  {level}: {count}\n")
            
            f.write("\n" + "="*50 + "\n")
            f.write("ERROR MESSAGES:\n")
            f.write("="*50 + "\n")
            for error in results['errors']:
                f.write(f"{error}\n")
        
        print(f"\nReport saved to: {output_file}")
    
    except PermissionError:
        print(f"Error: Cannot write to {output_file}")


def main():
    """Main function to run the log parser."""
    # Example usage - you can change this path
    log_file = "/var/log/syslog"
    
    # For testing, let's also try a sample file if syslog doesn't exist
    import os
    if not os.path.exists(log_file):
        print(f"{log_file} not found. Using sample log file instead.")
        log_file = "sample.log"
    
    print(f"Parsing log file: {log_file}")
    
    # Parse the log file
    results = parse_log_file(log_file)
    
    # Print summary to console
    print_summary(results)
    
    # Save detailed report
    if results:
        save_report(results, "log_analysis_report.txt")


# This is the standard way to make a script runnable
if __name__ == "__main__":
    main()
