#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        """Initialize a Shoe with a brand and size."""
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "Used"
    
    @property
    def size(self):
        """Get the size."""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
    
    def cobble(self):
        """Repair the shoe and set condition to 'New'."""
        print("Your shoe is as good as new!")
        self.condition = "New"