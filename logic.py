import matplotlib.pyplot as plt

# Take income input and convert to a float
income = float(input("Enter the income: "))

# Calculate the 50/30/20 breakdown
needs = income * 0.5
wants = income * 0.3
savings = income * 0.2

# Define data and labels for the chart
values = [needs, wants, savings]
labels = [
    f"Needs:£{int(needs)} (50%)",
    f"Wants: £{int(wants)} (30%)",
    f"Savings: £{int(savings)} (20%)"
        ]
colors = ["#4CAF50", "#FF9800", "#2196F3"]

# Create and show the pie chart
plt.pie(
    values, 
    labels=labels, 
    colors=colors, 
    startangle=140
)
plt.title(f"Budget Breakdown for £{income: .2f}")
plt.show()
