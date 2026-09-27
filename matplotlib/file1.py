import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],

    "Sales": [120, 135, 128, 150, 170, 165,
              180, 195, 185, 210, 225, 240],

    "Profit": [20, 25, 22, 30, 35, 32,
               40, 45, 38, 50, 55, 60],

    "Customers": [80, 90, 85, 100, 110, 105,
                  120, 130, 125, 140, 150, 160],

    "Advertising": [10, 12, 11, 15, 18, 17,
                    20, 22, 21, 25, 27, 30],

    "Expenses": [100, 110, 106, 120, 135, 133,
                 140, 150, 147, 160, 170, 180]
}

df = pd.DataFrame(data)
# print(df.columns)

## Line Graph
# plt.plot(df['Sales'],df['Profit'])
# plt.title("Sales vs Profit")
# plt.xlabel("Sales")
# plt.ylabel("Profit")
# plt.show()

## Bar Graph
# plt.bar(df['Month'],df['Profit'])
# plt.title("Month vs Profit")
# plt.xlabel("Month")
# plt.ylabel("Profit")
# plt.show()

## Histogram
# plt.hist(df['Sales'],bins=5)
# plt.title("Histogram for Sales")
# plt.xlabel("Sales")
# plt.ylabel("Frequency")
# plt.show()

## Scatterplot
# plt.scatter(df['Sales'],df['Profit'])
# plt.title("Sales vs Profit")
# plt.xlabel("Sales")
# plt.ylabel("Profit")
# plt.show()

## Piechart
# plt.pie(df['Sales'],labels=df['Month'],autopct='%1.1f%%')
# plt.title("Sales Month-Wise")
# plt.show()

## Boxplot
plt.boxplot (df['Sales'])
plt.title("Sales")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()