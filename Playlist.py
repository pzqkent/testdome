# A playlist is considered a repeating playlist if any of the songs contain a reference to a previous song in the playlist. Otherwise, the playlist will end with the last song which points to None.

# Implement a function is_repeating_playlist that, efficiently with respect to time used, returns true if a playlist is repeating or false if it is not.

# For example, the following code prints "True" as both songs point to each other.

'''first = Song("Hello")
# second = Song("Eye of the tiger")
    
# first.next_song(second);
# second.next_song(first);
    
print(first.is_repeating_playlist())
'''
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        if not self:
            return False
        if not self.next:
            return False
        node = self
        try:
            node1 = self.next.next
        except:
            return False
        
        while node and node1:
            if node == node1:
                return True
            node = node.next
            try:
                node1 = node1.next.next
            except:
                return False
            
        return False
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        return None
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second);
second.next_song(first);
    
print(first.is_repeating_playlist())