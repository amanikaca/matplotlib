import matplotlib.pyplot as plt

# Data
fruits = ['Apple', 'Banana', 'Mango', 'Orange']
counts = [25, 30, 15, 20]

#line plot
plt.subplot(1,3,1)
plt.plot(fruits,counts,marker='o',linestyle='--',linewidth=2,color='blue')
plt.grid(True,linestyle='-',alpha=0.2)
plt.title("count of fruits")
plt.xlabel("fruits")
plt.ylabel("counts")

# pie chart
plt.subplot(1,3,2)
plt.pie(counts, labels=fruits, autopct='%1.1f%%', startangle=90, colors=['red', 'yellow', 'gold', 'orange'])
plt.axis('equal')
plt.title("count of fruits")

#bar chart
plt.subplot(1,3,3)
color=['red','yellow','gold','orange']
plt.bar(fruits,counts,color=color)
plt.title("count of fruits")
plt.xlabel("fruits")
plt.ylabel("counts")
plt.grid(True,linestyle='--',alpha=0.2)


# Show chart
plt.tight_layout()
plt.show()
