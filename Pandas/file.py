import pandas as pd

data = {
    "Order_ID": [
        1001, 1002, 1003, 1004, 1005,
        1006, 1007, 1008, 1009, 1010,
        1011, 1012, 1013, 1014, 1015,
        1016, 1017, 1018, 1019, 1020
    ],

    "Customer": [
        "Rahul", "Priya", "Amit", "Sneha", "Arjun",
        "Neha", "Rohan", "Ananya", "Vikram", "Pooja",
        "Rahul", "Amit", "Sneha", "Karan", "Neha",
        "Rohan", "Priya", "Arjun", "Pooja", "Vikram"
    ],

    "City": [
        "Mumbai", "Delhi", "Pune", "Bangalore", "Kolkata",
        "Delhi", "Mumbai", "Pune", "Chennai", "Kolkata",
        "Mumbai", "Pune", "Bangalore", "Delhi", "Kolkata",
        "Chennai", "Delhi", "Mumbai", "Pune", "Bangalore"
    ],

    "Product": [
        "Laptop", "Phone", "Keyboard", "Monitor", "Laptop",
        "Mouse", "Phone", "Tablet", "Laptop", "Keyboard",
        "Monitor", "Phone", "Mouse", "Laptop", "Tablet",
        "Phone", "Keyboard", "Monitor", "Laptop", "Mouse"
    ],

    "Category": [
        "Electronics", "Electronics", "Accessories", "Electronics", "Electronics",
        "Accessories", "Electronics", "Electronics", "Electronics", "Accessories",
        "Electronics", "Electronics", "Accessories", "Electronics", "Electronics",
        "Electronics", "Accessories", "Electronics", "Electronics", "Accessories"
    ],

    "Quantity": [
        1, 2, 3, 1, 1,
        4, 1, 2, 1, 3,
        2, 1, 2, 1, 2,
        2, 4, 1, 1, 3
    ],

    "Price": [
        60000, 25000, 1500, 12000, 65000,
        800, 28000, 22000, 55000, 1800,
        13000, 26000, 900, 62000, 20000,
        27000, 1600, 14000, 58000, 850
    ],

    "Rating": [
        4.5, 4.2, 4.0, 4.7, 4.1,
        3.8, 4.4, 4.3, 4.6, 3.9,
        4.5, 4.0, 4.2, 4.8, 4.1,
        4.3, 3.7, 4.6, 4.4, 4.0
    ],

    "Order_Date": [
        "2026-01-05", "2026-01-08", "2026-01-12", "2026-01-15",
        "2026-01-20", "2026-02-03", "2026-02-08", "2026-02-15",
        "2026-02-20", "2026-03-01", "2026-03-05", "2026-03-10",
        "2026-03-15", "2026-03-20", "2026-04-02", "2026-04-07",
        "2026-04-12", "2026-04-18", "2026-04-22", "2026-04-28"
    ],

    "Payment": [
        "UPI", "Credit Card", "Cash", "UPI", "Debit Card",
        "UPI", "Credit Card", "UPI", "Debit Card", "Cash",
        "Credit Card", "UPI", "UPI", "Credit Card", "Debit Card",
        "UPI", "Cash", "Credit Card", "UPI", "Debit Card"
    ],

    "Status": [
        "Delivered", "Delivered", "Cancelled", "Delivered", "Delivered",
        "Delivered", "Returned", "Delivered", "Delivered", "Cancelled",
        "Delivered", "Delivered", "Returned", "Delivered", "Delivered",
        "Cancelled", "Delivered", "Returned", "Delivered", "Delivered"
    ]
}

df = pd.DataFrame(data)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# print(df.columns)

# columns = ['Order_ID', 'Customer', 'City', 'Product', 'Category', 'Quantity',
    #    'Price', 'Rating', 'Order_Date', 'Payment', 'Status']
# print(df.tail())

# print(df.sample(n=2))

# print(df.dtypes)

# print(df.ndim)

# print(df.isnull().sum())

# print(df['Rating'].clip(4.5,4.0))

