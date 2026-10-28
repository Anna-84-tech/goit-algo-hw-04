def get_cats_info(path: str) -> list[dict]:
    """
    Reads a file containing cat information and returns a list of dictionaries.
    """
    cats_list = []
    
    try:
        # Open the file safely using context manager and UTF-8 encoding
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Remove whitespace and skip empty lines
                line = line.strip()
                if not line:
                    continue
                
                # Split the line by comma into id, name, and age
                cat_id, name, age = line.split(',')
                
                # Create a dictionary for the current cat and append it to the list
                cat_dict = {
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }
                cats_list.append(cat_dict)
                
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
    except ValueError as e:
        print(f"Error parsing line format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    return cats_list


# --- Testing block ---
if __name__ == "__main__":
    file_path = "cats.txt"
    cats_info = get_cats_info(file_path)
    for cat in cats_info:
        print(cat)