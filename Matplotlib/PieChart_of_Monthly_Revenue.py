# Draw a piechart of dataset (month-revenue)
        # Month   Revenue
        # Jan     2.5 cr
        # Feb     4.0 cr
        # Mar     2.0 cr
        # Apr     1.0 cr 
from matplotlib import pyplot as plt

month =["Jan","Feb","Mar","Apr"]
revenue_label =["2.5 cr","4.0 cr","2.0 cr","1.0 cr"]
revenue = [2, 4, 2, 1]
plt.pie(revenue,labels=month,autopct= "%1.1f%%")
plt.title("Month wise Revenue Pie Chart")
plt.show()