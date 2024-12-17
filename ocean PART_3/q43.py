import csv

# Open the file
with open(r'D:\coding files\OceanVerse\PART 3\sensex.csv', 'r') as fh:
    ro = csv.reader(fh)
    next(ro)  # Skip header row

    # Variables to track min and max prices and corresponding rows
    min_price = float('inf')
    max_price = 0
    min_row = None
    max_row = None

    # Iterate through the rows to find the minimum and maximum prices
    for row in ro:
        current_price = float(row[4])  

        # Check for minimum price (potential buy)
        if current_price < min_price:
            min_price = current_price
            min_row = row  # Save the row for the minimum price
        
        # Check for maximum price (potential sell) after the minimum price
        if min_row and current_price > max_price:
            max_price = current_price
            max_row = row  # Save the row for the maximum price

# Output the results
if min_row and max_row:
    print("Buy on:")
    print(f"Date: {min_row[0]}, Price: {min_row[4]}")  
    print("Sell on:")
    print(f"Date: {max_row[0]}, Price: {max_row[4]}")
    print(f"Maximum Return: {max_price - min_price} Rupees")
else:
    print("Not enough data to calculate buy and sell points.")