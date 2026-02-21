import os
base_path = "/Users/metehancakmak/Documents/GitHub/b1-programming/Week 7/Week_7_lab_Exercise-1" #--> to change working directory, to find products.txt and pricing report in the same folder
input_files = os.path.join(base_path, "products.txt")
output_files = os.path.join(base_path, "pricing_report.txt")

category_discounts = {
    "Electronics": 0.10,
    "Clothing": 0.15,
    "Books": 0.05,
    "Home": 0.12
}

total_products = 0
total_discount_sum = 0

tier_discounts = {
    "Premium": 0.05,
    "Standard": 0.00,
    "Budget": 0.02
}
try:
    with open(input_files, "r") as f_input, open(output_files, "w") as f_output:
        
        f_output.write("PRICING REPORT\n")
        f_output.write("-" * 50 + "\n")

        for line in f_input:
            line = line.strip()
            if line:
                try:
                    parts = line.split(",")
                    name = parts[0]
                    base_price = float(parts[1].strip())
                    category = parts[2]
                    discount_tier = parts[3]

                    category_discount = category_discounts.get(category, 0)
                    tier_discount = tier_discounts.get(discount_tier, 0)
                    total_discount = 1 - (1- category_discount) * (1 - tier_discount)

                    final_price = base_price * (1 - total_discount)

                    total_products += 1
                    total_discount_sum += total_discount

                    f_output.write(f"Product:           {name}\n")
                    f_output.write(f"Base Price:        €{base_price:.2f}\n")
                    f_output.write(f"Category:          {category} ({category_discount*100:.0f}% off)\n")
                    f_output.write(f"Tier:              {discount_tier} ({tier_discount*100:.0f}% off)\n")
                    f_output.write(f"Total Discount:    {total_discount * 100:.2f}%\n")
                    f_output.write(f"Final Price:       €{final_price:.2f}\n")
                    f_output.write("-" * 50 + "\n")
                except ValueError:
                    print(f"Invalid price format - skipping {line}")
        f_output.write("\nEnd of Report\n")

    average_discount = total_discount_sum / total_products if total_products > 0 else 0
    print("SUMMARY:")
    print(f"Total products processed: {total_products}")
    print(f"Average discount applied: {average_discount * 100:.2f}%")

except FileNotFoundError:
    print("Error: products.txt not found")