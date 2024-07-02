import os

def list_files_in_directory(directory_path, output_file):
    try:
        # Get the list of all files in the directory
        files = os.listdir(directory_path)
        
        # Write the file names to the output file
        with open(output_file, 'w') as f:
            for file in files:
                leetcode_url = 'https://leetcode.com/problems/' + file[5:len(file)-2] + '/description/'
                f.write(leetcode_url + '\n')
        
        print(f"File names have been written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_directory_path' with the path of your directory
    directory_path = '../code'
    # Replace 'output_file.txt' with the name of the output text file
    output_file = 'leetcode_urls.txt'
    
    list_files_in_directory(directory_path, output_file)
