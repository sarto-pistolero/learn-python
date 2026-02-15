#!/usr/bin/env python3
"""
Config Validator Template - Challenge from EXERCISES.md

Your task: Complete this script to validate YAML configuration files.

TODO:
1. Read config.yaml file
2. Check for required fields
3. Validate port number range
4. Print validation results
"""

# You'll need to install pyyaml first:
# pip install pyyaml --break-system-packages

import yaml


def load_config(config_file):
    """
    Load YAML configuration file.
    
    Args:
        config_file (str): Path to YAML file
        
    Returns:
        dict: Configuration dictionary or None if error
    """
    # TODO: Implement this function
    # Hint: Use yaml.safe_load()
    # Hint: Don't forget try/except for file errors
    pass


def validate_config(config):
    """
    Validate configuration has required fields and correct values.
    
    Args:
        config (dict): Configuration dictionary
        
    Returns:
        tuple: (is_valid, errors_list)
    """
    # TODO: Implement validation logic
    
    required_fields = ['app_name', 'port', 'database']
    errors = []
    
    # TODO: Check if each required field exists
    # Hint: Use 'in' operator to check dictionary keys
    
    # TODO: Validate port is between 1-65535
    # Hint: Check if config['port'] exists first
    # Hint: Use 'and' for multiple conditions
    
    # Return True if no errors, False otherwise
    is_valid = len(errors) == 0
    return is_valid, errors


def main():
    """Main function."""
    config_file = 'config.yaml'
    
    # TODO: Load the config
    config = load_config(config_file)
    
    if config is None:
        print("Failed to load config file")
        return
    
    # TODO: Validate the config
    is_valid, errors = validate_config(config)
    
    # TODO: Print results
    if is_valid:
        print("✓ Config is VALID")
    else:
        print("✗ Config is INVALID")
        print("Errors found:")
        for error in errors:
            print(f"  - {error}")


if __name__ == "__main__":
    main()


# HINTS FOR IMPLEMENTATION:
#
# Loading YAML:
#   with open(config_file, 'r') as f:
#       config = yaml.safe_load(f)
#
# Checking if key exists:
#   if 'app_name' not in config:
#       errors.append("Missing required field: app_name")
#
# Validating port:
#   if 'port' in config:
#       port = config['port']
#       if not isinstance(port, int) or port < 1 or port > 65535:
#           errors.append("Port must be between 1-65535")
#
# Sample config.yaml to test with:
# ---
# app_name: myapp
# port: 8080
# database:
#   host: localhost
#   port: 5432
# ---
