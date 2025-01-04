import os
import base64

# Base64 encode files
def encode_file(filepath):
    with open(filepath, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode('utf-8')
    return encoded

# Create the single Python file
def create_single_py(index_file, folders, output_file):
    with open(output_file, 'w') as out:
        # Add index.py content
        with open(index_file, 'r') as index:
            out.write('# --- Start of index.py content ---\n')
            out.write(index.read())
            out.write('\n# --- End of index.py content ---\n\n')

        # Embed files from folders
        for folder in folders:
            out.write(f"# --- Embedding files from: {folder} ---\n")
            for root, _, files in os.walk(folder):
                for file in files:
                    filepath = os.path.join(root, file)
                    variable_name = file.replace('.', '_')
                    encoded_content = encode_file(filepath)
                    out.write(f"{variable_name} = '{encoded_content}'\n\n")

        # Add decode utility
        out.write("""
# Utility to decode and save files
import base64
def save_file(encoded_data, output_path):
    with open(output_path, 'wb') as file:
        file.write(base64.b64decode(encoded_data.encode('utf-8')))
        """)
    print(f"Single Python file created: {output_file}")

# Input
index_py = 'index.py'
folders_to_embed = ['images', 'songs', 'other_folders']  # Replace with actual folder names
output_py = 'single_output.py'

# Generate single file
create_single_py(index_py, folders_to_embed, output_py)
