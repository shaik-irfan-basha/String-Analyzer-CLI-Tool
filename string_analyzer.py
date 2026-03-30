"""
JASIQ Labs - Python Master Implementation Guide (Phase 0)
Project: String Analyzer CLI Tool
Part of JASIQ Labs Internship (Work + Learning, Job Ready Internship)
"""

def analyze_string():
    # 1. Take user input using input()
    # .strip() is used to remove accidental leading/trailing spaces
    user_input = input("Enter a string: ").strip()
    
    if not user_input:
        print("Input cannot be empty!")
        return

    # 2. Total characters (using len())
    total_chars = len(user_input)
    
    # 3. Total words (using .split() to handle multiple spaces)
    total_words = len(user_input.split())
    
    # 4. Number of vowels (using a loop to analyze content)
    vowels = "aeiou"
    vowel_count = 0
    # Use .lower() to ensure we catch 'A' as well as 'a'
    for char in user_input.lower():
        if char in vowels:
            vowel_count += 1
            
    # 5. Reversed string (using slicing [::-1])
    reversed_str = user_input[::-1]
    
    # 6. Palindrome Check
    # A string is a palindrome if it reads the same forwards and backwards
    # We compare the lower-cased versions for better accuracy (e.g., "Madam")
    is_palindrome = "Yes" if user_input.lower() == reversed_str.lower() else "No"
    
    # Final Output - formatted to match sample output
    print(f'Input: "{user_input}"')
    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Vowels: {vowel_count}")
    print(f"Reversed: {reversed_str}")
    print(f"Palindrome: {is_palindrome}")

if __name__ == "__main__":
    analyze_string()
