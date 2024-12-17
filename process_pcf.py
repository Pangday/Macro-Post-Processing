import os

# Function to remove specific sections from .pcf files based on start and stop section headers
def remove_sections(lines, start_sections, stop_sections):
    new_lines = []
    skip_lines = False
    
    for line in lines:
        # Strip leading/trailing whitespaces and lowercase for comparison
        stripped_line = line.strip().lower()

        # Check if the current line is a section header that needs to be removed
        if any(stripped_line == section for section in start_sections):
            skip_lines = True
        
        # If we are skipping lines, stop when encountering a stop section
        if skip_lines:
            # Check if the line exactly matches any stop section (e.g., 'pipe', not 'pipe-fixed')
            if any(stripped_line == section for section in stop_sections):
                skip_lines = False
            
            # Continue skipping lines while in the skip mode
            if skip_lines:
                continue

        # If not skipping lines, add the line to new_lines
        new_lines.append(line)
    
    return new_lines

# Function to edit individual .pcf files based on your requirements
def edit_pcf_file(file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines in the file

    # Define the start and stop sections
    start_sections = ["gasket", "bolt", "instrument-angle", "pipe-fixed", "cap", "instrument", "support", "instrument-dial", "flange-reducing-concentric", "coupling", "misc-component"]
    stop_sections = ["pipe", "flow-arrow", "weld", "elbow", "iso-split-point", 
                     "reducer-eccentric", "olet", "flange", "reference-dimension", 
                     "end-position-open", "tee"]
    
    # Remove specified sections
    lines = remove_sections(lines, start_sections, stop_sections)
    
    # Additional processing: Replace 'COMPONENT-ATTRIBUTE1' with 'MAT-CODE' in the file
    new_lines = []
    for line in lines:
        # Modify the lines as per your requirement
        new_line = line.replace('COMPONENT-ATTRIBUTE1', 'MAT-CODE')  # Change this logic as needed
        new_lines.append(new_line)
    
    # Save the edited content back to the file
    with open(file_path, 'w') as file:
        file.writelines(new_lines)

# Function to process all .pcf files in a specified directory
def process_all_pcfs(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file has a .pcf extension
        if filename.endswith('.pcf'):
            file_path = os.path.join(directory, filename)  # Full file path
            print(f"Processing {filename}...")
            edit_pcf_file(file_path)  # Call the function to edit the .pcf file
            print(f"{filename} has been processed.")

# Define the directory where your .pcf files are stored
pcf_directory = 'C:\\Users\\ZIYING.PANG\\OneDrive - Seatrium Ltd\\Production Engineering & Scheduling\\process_pcf'

# Process all .pcf files in the directory
process_all_pcfs(pcf_directory)

print("All .pcf files have been processed.")
