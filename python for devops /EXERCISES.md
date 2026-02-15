# Task 1 Exercises: Data Structures & File Operations

## Learning Objectives
After completing these exercises, you should understand:
- Reading and writing files in Python
- Using dictionaries, lists, sets effectively
- String operations and searching
- Basic data analysis patterns

## Exercise 1: Basic Log Parser (START HERE)
Run the basic log_parser.py script:
```bash
python3 log_parser.py
```

**Challenges to add:**
1. Modify the script to also count "WARN" as warnings
2. Add tracking for "FATAL" level logs
3. Change the output to show percentages instead of just counts
4. Save only ERROR logs to a separate file called "errors_only.log"

## Exercise 2: Advanced Parser
Run the advanced parser:
```bash
python3 log_parser_advanced.py
```

**Challenges:**
1. Add a function to find the hour with the most errors
2. Create a function that groups logs by minute (not just hour)
3. Find and print the most common error message (hint: use Counter)
4. Add detection for security-related keywords (login, auth, security, etc.)

## Exercise 3: Real-World Practice

### Challenge A: Config File Validator
Create a new script `config_validator.py` that:
1. Reads a YAML config file (install pyyaml: pip install pyyaml)
2. Checks for required fields: ['app_name', 'port', 'database']
3. Validates that port is between 1-65535
4. Prints "VALID" or lists what's missing

Sample config.yaml:
```yaml
app_name: myapp
port: 8080
database:
  host: localhost
  port: 5432
```

### Challenge B: Disk Usage Monitor
Create `disk_monitor.py` that:
1. Uses `os.statvfs()` to check disk usage
2. Stores results in a dictionary with keys: total, used, free, percent
3. Prints warning if usage > 80%
4. Writes results to a JSON file

Hint:
```python
import os
stat = os.statvfs('/home')
# Research what stat.f_blocks, f_bfree, f_bsize mean
```

### Challenge C: Multi-Log Analyzer
Create `multi_log_analyzer.py` that:
1. Takes a directory path as input
2. Finds all .log files in that directory
3. Runs analysis on each file
4. Produces a summary comparing all files

Use these Python concepts:
- `os.listdir()` or `glob.glob('*.log')`
- Dictionary to store results for each file
- Loops to process multiple files

## Exercise 4: Data Structure Practice

Without running code first, predict the output:

```python
# What does this print?
errors = ['timeout', 'timeout', 'connection', 'timeout', 'disk full']
error_count = {}
for error in errors:
    if error in error_count:
        error_count[error] += 1
    else:
        error_count[error] = 1
print(error_count)
```

```python
# What about this?
from collections import defaultdict
errors = ['timeout', 'timeout', 'connection', 'timeout', 'disk full']
error_count = defaultdict(int)
for error in errors:
    error_count[error] += 1
print(dict(error_count))
```

```python
# And this?
from collections import Counter
errors = ['timeout', 'timeout', 'connection', 'timeout', 'disk full']
error_count = Counter(errors)
print(error_count.most_common(2))
```

## Exercise 5: String Operations Practice

Try these in a Python shell (type `python3` in terminal):

```python
# Practice 1: Check if string contains keywords
log_line = "ERROR: Database connection timeout"

# Try these:
'ERROR' in log_line
log_line.startswith('ERROR')
log_line.lower().find('database')
log_line.split()
log_line.split(':')

# Practice 2: Extract parts
timestamp = "2024-02-12 10:15:23"
parts = timestamp.split()
date = parts[0]
time = parts[1]

# Can you get just the hour?

# Practice 3: String formatting
level = "ERROR"
count = 42
# Try all these formatting methods:
print(f"{level}: {count} occurrences")
print("{}: {} occurrences".format(level, count))
print("%s: %d occurrences" % (level, count))
```

## Tips for Success

1. **Start Simple**: Run the basic parser first, understand every line
2. **Add Features Gradually**: Don't try to do everything at once
3. **Print Everything**: Use print() to see what your variables contain
4. **Test with Small Data**: Use the sample.log first, it's easier to debug
5. **Read Error Messages**: Python errors tell you exactly what's wrong

## Common Gotchas

```python
# ❌ Wrong: Trying to access dictionary key that doesn't exist
counts = {'ERROR': 5}
print(counts['WARNING'])  # KeyError!

# ✅ Right: Check first or use .get()
if 'WARNING' in counts:
    print(counts['WARNING'])
# Or
print(counts.get('WARNING', 0))  # Returns 0 if key doesn't exist

# ❌ Wrong: Forgetting to close files
f = open('file.txt', 'r')
data = f.read()
# File not closed!

# ✅ Right: Use 'with' statement
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed
```

## Next Steps

Once you're comfortable with these concepts:
1. Try parsing real system logs in /var/log/
2. Add command-line arguments (research: argparse module)
3. Learn about JSON and YAML parsing (json, pyyaml modules)
4. Explore the datetime module for better time handling

Good luck! Remember: Real learning happens when you modify the code and break things.
