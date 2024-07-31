
import csv
import random
from datetime import datetime

date_var = datetime(2024, 7, 23).strftime('%Y-%m-%d')
# Function to read customer information from CSV file
def read_customer_info(filename):
    customer_info = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customer_info[row['name']] = {
                'customer_id': int(row['customer_id']),
                'debit_card_number': row['debit_card_number'],
                'debit_card_type': row['debit_card_type'],
                'bank_name': row['bank_name']
            }
    return customer_info

# Function to generate mock data for daily transactions
def generate_mock_transactions(customer_info, num_transactions):
    transactions = []
    for _ in range(num_transactions):
        for name, info in customer_info.items():
            transaction_date = date_var
            amount_spend = round(random.uniform(10, 500), 2)  # Varies for each transaction
            transactions.append([info["customer_id"], name, info["debit_card_number"], info["debit_card_type"], info["bank_name"], transaction_date, amount_spend])
    return transactions

# Function to save transactions data to a CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['customer_id', 'name', 'debit_card_number', 'debit_card_type', 'bank_name', 'transaction_date', 'amount_spend'])
        writer.writerows(data)

# Main function
def main():
    # Read customer information from CSV file
    customer_info = read_customer_info('customer_records.csv')
    
    # Generate transactions for today
    num_transactions = 20  # You can change this number as per your requirement
    transactions = generate_mock_transactions(customer_info, num_transactions)
    
    # Save transactions to a CSV file       
    today_date = date_var
    csv_filename = f"transactions_{today_date}.csv"
    save_to_csv(transactions, csv_filename)
    
    print(f"Mock transactions for {today_date} have been generated and saved to '{csv_filename}'.")

if __name__ == "__main__":
    main()
