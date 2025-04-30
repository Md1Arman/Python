def find_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  # Ensure b >= a to avoid duplicates
            c = (a**2 + b**2) ** 0.5  # Calculate c
            if c.is_integer() and c <= limit:  # Check if c is a whole number and within range
                triplets.append((a, b, int(c)))
    return triplets

# Set the limit to 30
limit = 30
triplets = find_pythagorean_triplets(limit)

# Print the triplets
for triplet in triplets:
    print(triplet)
