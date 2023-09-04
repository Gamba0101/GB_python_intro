def count_crafts(total_crafts):
    # Calculate the total crafts made by child1 and child2
    crafts_child1_and_child2 = total_crafts // 3  # Dividing equally among 3 children
    
    # Calculate the crafts made by child3
    crafts_child3 = crafts_child1_and_child2 * 2
    
    # Calculate the crafts made by each child
    crafts_child1 = crafts_child1_and_child2 // 2
    crafts_child2 = crafts_child1_and_child2 // 2
    
    # Display the results
    print(f"Child 1 made {crafts_child1} crafts.")
    print(f"Child 2 made {crafts_child2} crafts.")
    print(f"Child 3 made {crafts_child3} crafts.")

# Example input
total_crafts = int(input("Enter the total number of crafts: "))
count_crafts(total_crafts)
