class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        # Morse code mapping for letters 'a' through 'z'
        morse_map = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        unique_transformations = set()
        
        for word in words:
            
            transformation = []
            for char in word:
                
                index = ord(char) - ord('a')
                transformation.append(morse_map[index])
            
            
            unique_transformations.add("".join(transformation))
            
        # The size of the set represents the number of unique transformations
        return len(unique_transformations)