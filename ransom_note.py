def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.
    
    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.
    
    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    # Build a hash table (dictionary) to count character frequencies in magazine
    char_count = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Check if we can construct the ransom note
    for char in ransomNote:
        # If character is missing or count is 0, we can't construct the note
        if char not in char_count or char_count[char] == 0:
            return False
        # Use one instance of this character
        char_count[char] -= 1
    
    # All characters were available
    return True