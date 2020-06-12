import java.util.Map;
import java.util.HashMap;

/*
Problem 205: Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the
order of characters. No two characters may map to the same character but a character may map
to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note: You may assume both s and t have the same length.
*/

class IsomorphicStringsSolution {
    public boolean isIsomorphic(String s, String t) {
        // This hash map maps each char in s to the corresponding char in t.
        Map<Character, Character> sToT = new HashMap<>();
        
        // This hash map maps each char in t to the corresponding char in s.
        Map<Character, Character> tToS = new HashMap<>();
        
        int strLen = s.length();
        for (int i = 0; i < strLen; i++) {
            Character sChar = s.charAt(i);
            Character tChar = t.charAt(i);
            
            // If the value for the current char in s in sToT is different from the
            // current char in t, s and t are not isomorphic.
            Character sValue = sToT.putIfAbsent(sChar, tChar);
            if (sValue != null && !sValue.equals(tChar)) return false;
            
            // If the value for the current char in t in tToS is different from the
            // current char in s, s and t are not isomorphic.
            Character tValue = tToS.putIfAbsent(tChar, sChar);
            if (tValue != null && !tValue.equals(sChar)) return false;
        }
        
        return true;
    }
}
