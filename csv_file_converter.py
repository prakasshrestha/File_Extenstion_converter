import os
import time


def read_files_in_folder_and_write_to_csv(folder_path, file_extension):
    """
    Recursively reads files in a folder and its subfolders, then writes the data to a CSV file.
    Args:
        folder_path (str): folder path 
        file_extension (_type_): file extension : csv,tmp
    """

    # Check if the folder exists
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # print(f"Checking files in {folder_path}")
        # List all files in the folder
        files = os.listdir(folder_path)

        # Iterate through files in the folder
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)

            # Check if the file is a regular file and not a directory
            if os.path.isfile(file_path):
                # Check if a corresponding CSV file already exists
                split_path = os.path.splitext(file_path)
                split_path = split_path[0] + ".csv"
                if os.path.exists(split_path):
                    print(
                        f"CSV file already exists for {file_path}. Skipping.")
                    pass
                else:
                    try:
                        # Read the content of the file
                        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
                            # igoner the csv file read onyl tmp file
                            csv_output_path = os.path.splitext(file_path)
                            csv_output_path = csv_output_path[0] + \
                                "."+file_extension
                            os.rename(file_path, csv_output_path)
                    except FileNotFoundError:
                        print(f"Error: File '{file_path}' not found.")
                    except FileExistsError:
                        print(
                            f"Error: File '{csv_output_path}' already exists.")
                    except Exception as e:
                        print(f"Error: Unable to rename file. {e}")
            else:
                # If it's a directory, recursively call the function
                read_files_in_folder_and_write_to_csv(file_path)
    else:
        print(f"Folder {folder_path} does not exist.")


if __name__ == "__main__":
    root_folder = 'give the folder path'
    extension = "csv"
    # Call the function with the root folder and output CSV path
    read_files_in_folder_and_write_to_csv(root_folder, extension)
    time.sleep(10)
