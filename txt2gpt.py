import os

def split_text_file(input_file, output_file):
    # Read the input file into a string
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()

    # Calculate the total number of parts needed
    text_length = len(text)
    chunk_size = 2046
    num_parts = (text_length // chunk_size) + (1 if text_length % chunk_size != 0 else 0)

    # Write the output to a new file with the specified format
    with open(output_file, 'w', encoding='utf-8') as outfile:
        start = 0
        end = 0
        for part in range(1, num_parts + 1):
            header = f'[part {part} of {num_parts}] '
            available_size = 2048 - len(header) - 1  # Subtract header length and newline character
            end = start + available_size
            outfile.write(header + text[start:end] + '\n')
            start = end

# Ask the user for the input file name
input_file = input("Enter the input file name: ")

# Generate the output file name by appending '_GPT' to the input file name (excluding its extension)
file_name, file_extension = os.path.splitext(input_file)
output_file = f"{file_name}_GPT{file_extension}"

split_text_file(input_file, output_file)
