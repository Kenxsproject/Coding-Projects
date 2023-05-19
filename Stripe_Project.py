import stripe
import csv

# Set your API key here
stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

# Create a list to store all the transactions
transactions = []

# Get all customers
customers = stripe.Customer.list(auto_advance=True)

# Loop through each customer and retrieve their transactions and charges
for customer in customers:
    # Get all charges for this customer
    charges = stripe.Charge.list(customer=customer.id, limit=100)
    for charge in charges:
        transaction = {
            "customer_id": customer.id,
            "customer_email": customer.email,
            "charge_id": charge.id,
            "amount": charge.amount,
            "currency": charge.currency,
            "description": charge.description,
            "created": charge.created,
            "type": "charge",
        }
        transactions.append(transaction)

    # Get all subscriptions for this customer
    subscriptions = stripe.Subscription.list(customer=customer.id, limit=100)
    for subscription in subscriptions:
        transaction = {
            "customer_id": customer.id,
            "customer_email": customer.email,
            "subscription_id": subscription.id,
            "amount": subscription.plan.amount,
            "currency": subscription.plan.currency,
            "description": subscription.plan.nickname,
            "created": subscription.created,
            "type": "subscription",
        }
        transactions.append(transaction)

# Print out the transactions to the terminal
for transaction in transactions:
    print(transaction)

# Save the transactions to a CSV file
with open("Workspace.csv", "w", encoding= 'UTF8') as csvfile:
    fieldnames = [
        "customer_id",
        "customer_email",
        "charge_id",
        "subscription_id",
        "amount",
        "currency",
        "description",
        "created",
        "type",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for transaction in transactions:
        writer.writerow(transaction)



