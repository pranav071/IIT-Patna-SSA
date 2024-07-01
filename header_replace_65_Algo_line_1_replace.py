import os

def replace_header_in_csv_files(prefix_pattern):
    # Directory containing the CSV files
    directory = "."

    # Find the file containing the pattern ABC_test.csv
    test_file = None
    for filename in os.listdir(directory):
        if f"{prefix_pattern}_test.csv" in filename:
            test_file = filename
            break

    # Check if the test file exists
    if test_file is None:
        print(f"No file matching pattern {prefix_pattern}_test.csv found in the current directory.")
        return

    # Read the first line of the test file
    with open(test_file, 'r') as f:
        header = f.readline()

    # Loop through all CSV files in the current directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and f"{prefix_pattern}_feature.csv" not in filename:
            if filename != test_file:
                with open(filename, 'r') as f:
                    content = f.readlines()

                # Replace the first line with the header
                content[0] = header

                # Write the updated content back to the file
                with open(filename, 'w') as f:
                    f.writelines(content)

    print("Header replaced in all applicable files.")

# Example usage
prefix_pattern = "SSA"
replace_header_in_csv_files(prefix_pattern)
