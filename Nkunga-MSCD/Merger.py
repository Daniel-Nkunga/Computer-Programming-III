import os
import csv

def combine_csv_files(folder_path, output_file):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # Ensure output file ends with .csv
    if not output_file.endswith('.csv'):
        output_file += '.csv'

    # Open the output CSV file in write mode
    with open(output_file, 'w', newline='') as combined_file:
        writer = csv.writer(combined_file)

        # Flag to indicate if header has been written
        header_written = False

        # Iterate through each CSV file
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            # Open the current CSV file
            with open(file_path, 'r', newline='') as current_file:
                reader = csv.reader(current_file)

                # Skip the header if it has already been written
                if not header_written:
                    header = next(reader)
                    writer.writerow(header)
                    header_written = True

                # Write the rows from the current CSV file
                for row in reader:
                    writer.writerow(row)

    print(f"Combined {len(files)} CSV files into {output_file}")

# Use the current directory as the folder path
folder_path = '.'
output_file = 'Caves.csv'
combine_csv_files(folder_path, output_file)
