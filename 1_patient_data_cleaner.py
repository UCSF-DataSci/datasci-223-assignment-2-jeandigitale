#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os
import pandas as pd

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    # BUG: No error handling for file not found
    with open(filepath, 'r') as file:
        return json.load(file)

def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []

    seen = set()
    
    for patient in patients:
        # BUG: Typo in key 'nage' instead of 'name'
        patient['name'] = patient['name'].title()
        
        # BUG: Wrong method name (fill_na vs fillna)
        # FIX: Couldn't use fillna because it wasn't a dataframe, Convert age to numeric, allow missing
        age = pd.to_numeric(patient.get('age'), errors='coerce')

        # Skip if age is missing or under 18
        if pd.isna(age) or age < 18:
            continue

        patient['age'] = int(age)  # Cast to int only if valid

        # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
        # FIX: Can't use drop_duplicates because it's not a dataframe 

        # BUG: Wrong comparison operator (= vs ==)
        # FIX: change to ==
        if patient['age'] == 18:
            # BUG: Logic error - keeps patients under 18 instead of filtering them out
            cleaned_patients.append(patient)

        # Convert patient dict to a tuple of items so it can go in a set
        # Identified if it was a duplicate and appended if not
        patient_tuple = tuple(sorted(patient.items()))

        if patient_tuple not in seen:
            seen.add(patient_tuple)
            cleaned_patients.append(patient)

    # BUG: Missing return statement for empty list
    if not cleaned_patients:
        return None
    
    return cleaned_patients

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    # BUG: No error handling for load_patient_data failure
    patients = load_patient_data(data_path)
    
    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No check if cleaned_patients is None
    # Print the cleaned patient data
    print("Cleaned Patient Data:")
    for patient in cleaned_patients:
        # BUG: Using 'name' key but we changed it to 'nage'
        print(f"Name: {patient['name']}, Age: {patient['age']}, Diagnosis: {patient['diagnosis']}")
    
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()