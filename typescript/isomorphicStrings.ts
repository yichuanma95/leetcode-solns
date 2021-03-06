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

Solution runtime: 76ms, faster than 100% of TypeScript submissions

Solution memory usage: 37.3 MB, less than 100% of TypeScript submissions
*/

function isIsomorphic(s: string, t: string): boolean {
    // This map maps each char in s to the corresponding char in t.
    let sToT = new Map();
    
    // This map maps each char in t to the corresponding char in s.
    let tToS = new Map();
    
    let strLen = s.length;
    for (let i = 0; i < strLen; i++) {
        let sChar = s[i];
        let tChar = t[i];
        
        if (sToT.has(sChar) && sToT.get(sChar) !== tChar) return false;
        else sToT.set(sChar, tChar);
        
        if (tToS.has(tChar) && tToS.get(tChar) !== sChar) return false;
        else tToS.set(tChar, sChar);
    }
    
    return true;
};
