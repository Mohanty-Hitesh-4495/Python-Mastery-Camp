# Draw a Graph of given Dataset (month-revenue)   
        # Month   Revenue
        # Jan     2.5 cr
        # Feb     4.0 cr
        # Mar     2.0 cr
        # Apr     1.0 cr 

from matplotlib import pyplot as plt


month = ["Jan", "Feb", "Mar", "Apr"]
revenue = [2.5, 4.0, 8.2, 1.0]  # Convert revenue to float values
revenue_label = ["2.5 cr", "4.0 cr", "2.0 cr", "1.0 cr"]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Different colors for each bar

plt.bar(month, revenue, color=colors)

# Set y-axis limits
plt.ylim(0, max(revenue) + 1)  # Set the maximum y-axis limit slightly above the maximum revenue

# Add revenue labels above each bar
for i, value in enumerate(revenue):
    plt.text(i, value + 0.1, revenue_label[i], ha='center', va='bottom')

plt.xlabel('Month')
plt.ylabel('Revenue (in cr)')
plt.title('Revenue by Month')
plt.show()

