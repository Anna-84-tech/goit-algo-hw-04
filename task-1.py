def total_salary(path):
    total = 0
    count = 0
    
    try:
        # Use the 'with' context manager and specify utf-8 encoding
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Skip empty lines
                line = line.strip()
                if not line:
                    continue
                
                # Split the line by comma into name and salary
                try:
                    name, salary = line.split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    # Skip lines with an incorrect format
                    continue
                    
        # Check in case of an empty file to avoid division by zero
        if count == 0:
            return 0, 0
            
        average = total / count
        return total, average
        
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
        return 0, 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0, 0


# === Test Block ===
if __name__ == "__main__":
    # Path to your file in the same directory
    file_path = "salary_file.txt"
    
    print("--- Running Test ---")
    
    # Call the function with your file
    total, average = total_salary(file_path)
    
    # Print the results matching the task requirements
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")