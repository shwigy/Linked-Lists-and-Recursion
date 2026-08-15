from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    roster = LinkedList()

    # 2) Insert some sample employee IDs
    roster.insert_at_end(101)
    roster.insert_at_end(102)
    roster.insert_at_end(103)
    roster.insert_at_front(100)

    # 3) Display the list to verify insertion
    print("Employee roster:")
    roster.display()

    # 4) Call recursive_sum and print the result
    print(f"Sum of all IDs: {roster.recursive_sum()}")

    # 5) Call recursive_search with a target and print result
    search_id = 102
    found = roster.recursive_search(search_id)
    print(f"Searching for ID {search_id}: {'Found' if found else 'Not found'}")

    missing_id = 999
    found_missing = roster.recursive_search(missing_id)
    print(f"Searching for ID {missing_id}: {'Found' if found_missing else 'Not found'}")

    # 6) Call recursive_reverse, then display the reversed list
    roster.recursive_reverse()
    print("Reversed roster:")
    roster.display()
