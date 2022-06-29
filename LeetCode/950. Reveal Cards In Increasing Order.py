# Input: deck = [17,13,11,2,3,5,7]
# Output: [2,13,3,11,5,17,7]
# Explanation: 
# We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
# After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
# We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
# We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
# We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
# We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
# We reveal 13, and move 17 to the bottom.  The deck is now [17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is correct.
# Example 2:
# Input: deck = [1,1000]
# Output: [1,1000]
# deque // queue // important // review // pattern array matching// matching// array patter // review //important
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = collections.deque()
        for x in sorted(deck)[::-1]:
            if d:
                d.appendleft(d.pop())
            d.appendleft(x)
        return list(d)
                        
