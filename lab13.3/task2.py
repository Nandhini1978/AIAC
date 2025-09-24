def read_file(filename):
    """
    Read and return the contents of a file safely.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        str: The contents of the file
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        PermissionError: If there are insufficient permissions to read the file
        IOError: For other file-related errors
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
        return None
    except IOError as e:
        print(f"Error reading file '{filename}': {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Test with a file
    content = read_file("poem.txt")
    if content:
        print("File contents:")
        print(content)
    else:
        print("Failed to read file.")