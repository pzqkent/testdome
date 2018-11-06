class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        if not self:
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
            node1 = node1.next.next
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