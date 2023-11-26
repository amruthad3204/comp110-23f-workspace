"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Get the data of the head node."""
        return self.data
    
    def tail(self) -> Node | None:
        """Get a new linked list without the head."""
        if self.next:
            new_node = Node(self.next.data, self.next.next)
            return new_node
        else:
            return None
    
    def last(self) -> int:
        """Get the data of the last node in the linked list."""
        if not self.next:
            return self.data
        else:
            return self.next.last()