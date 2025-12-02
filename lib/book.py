#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        """Initialize a Book with a title and page_count."""
        self.title = title
        self._page_count = None
        self.page_count = page_count
    
    @property
    def page_count(self):
        """Get the page_count."""
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """Set the page_count with validation."""
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """Output a message about turning the page."""
        print("Flipping the page...wow, you read fast!")
    
        