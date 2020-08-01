'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

'''

def isAlienSorted(self, words: List[str], order: str) -> bool:
    orderdict = {}
    for i,ch in enumerate(order):
        orderdict[ch] = i
    #print(orderdict)
    for i in range(len(words)-1):
        #Using transitive property and comparing only 2 words at a time
        #The words are sorted lexicographically 
        #if and only if adjacent words are.
        #This is because order is transitive: a <= b and b <= c implies a <= c.
        w1 = words[i] #w1 = "hello"
        w2 = words[i+1] #w2 = "leetcode"
        #looping over the min of words to not go out of range
        for j in range(min(len(w1),len(w2))):
            if w1[j] != w2[j]:
                if (orderdict[w1[j]] > orderdict[w2[j]]):
                    return False
                break
        else:
            #We are using this else block for "for loop"
            #this can only be done in python
            if len(w1) > len(w2):
                return False
    return True
