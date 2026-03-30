def analyze_string():
    # Take user input
    user_input = input("Enter a string: ").strip()
    
    if not user_input:
        print("Input cannot be empty!")
        return

    # Total characters
    total_chars = len(user_input)
    
    # Total words
    # .split() handles multiple spaces and leading/trailing whitespace
    total_words = len(user_input.split())
    
    # Number of vowels
    vowels = "aeiou"
    vowel_count = 0
    for char in user_input.lower():
        if char in vowels:
            vowel_count += 1
            
    # Reversed string
    reversed_str = user_input[::-1]
    
    # Palindrome Check
    # Case-insensitive comparison
    # We compare the stripped and lowered versions
    is_palindrome = "Yes" if user_input.lower() == reversed_str.lower() else "No"
    
    # Output results
    print(f"\nInput: \"{user_input}\"")
    print(f"Total characters: {total_chars}")
    print(f"Total words: {total_words}")
    print(f"Vowels: {vowel_count}")
    print(f"Reversed: {reversed_str}")
    print(f"Palindrome: {is_palindrome}")

if __name__ == "__main__":
    analyze_string()
