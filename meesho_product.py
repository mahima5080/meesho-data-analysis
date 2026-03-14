
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

meesho_data = pd.read_csv('meesho_product_dataset_india.csv')
meesho_data.head(10)

meesho_data.info()
meesho_data.describe()

# 1. How many products are there in each category?

category_counts = meesho_data['Category'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=category_counts.index, y=category_counts.values, palette='viridis')
plt.title('Number of Products in Each Category')
plt.xlabel('Category')
plt.ylabel('Number of Products')
plt.show()


# 2. What is the price distribution of products?

plt.figure(figsize=(10, 6))
sns.histplot(meesho_data['Price'], bins=30, kde=True, color='blue')
plt.title('Price Distribution of Products')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()


# 3.Average product rating by category?
average_ratings = meesho_data.groupby('Category')['Ratings'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Ratings', data=average_ratings, palette='magma')
plt.title('Average Product Rating by Category')
plt.xlabel('Category')
plt.ylabel('Average Ratings')
plt.show()


# 4.Which top 5 products have the highest reviews?
top_reviewed_products = meesho_data.nlargest(5, 'Reviews')[['Product_Name', 'Reviews']]
print("Top 5 Products with Highest Reviews:")

sns.barplot(x='Reviews', y='Product_Name', data=top_reviewed_products, palette='coolwarm')
plt.title('Top 5 Products with Highest Reviews')
plt.xlabel('Number of Reviews')
plt.ylabel('Product Name')
plt.show()


# 5. Compare original price vs discount price
price_data = meesho_data[['Price','Discount_Price']]

sns.boxplot(data=price_data, palette='Set2')
plt.title('Comparison of Original Price vs Discount Price')
plt.ylabel('Price')
plt.xticks([0, 1], ['Price', 'Discount Price'])
plt.show()


# 6.Which sellers list the most products?

top_sellers = meesho_data['Seller_Name'].value_counts().head(5)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_sellers.index, y=top_sellers.values, palette='Set3')
plt.title('Top 5 Sellers with Most Products')
plt.xlabel('Seller Name')
plt.ylabel('Number of Products')
plt.show()


# 7.Distribution of delivery time categories

plt.figure(figsize=(10, 6))
sns.countplot(y='Delivery_Time', data=meesho_data, order=meesho_data['Delivery_Time'].value_counts().index, palette='pastel')
plt.title('Distribution of Delivery Time Categories')
plt.xlabel('Number of Products')
plt.ylabel('Delivery Time')
plt.show()


# 8. Relationship between ratings and number of reviews
plt.figure(figsize=(10, 6))
plt.scatter(meesho_data['Ratings'], meesho_data['Reviews'], alpha=0.5, color='green')
plt.title('Relationship between Ratings and Number of Reviews')
plt.xlabel('Ratings')
plt.ylabel('Number of Reviews')
plt.show()


# 9.Availability status count (In-Stock vs Out-of-Stock)

availability_counts = meesho_data['Availability'].value_counts()

plt.figure(figsize=(8, 5))
plt.pie(availability_counts.values, labels=availability_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Availability Status Count')
plt.show()


# 10.Average discount percentage by category
meesho_data['Discount_Percentage'] = ((meesho_data['Price'] - meesho_data['Discount_Price']) / meesho_data['Price']) * 100

avg_discount = meesho_data.groupby('Category')['Discount_Percentage'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Discount_Percentage', data=avg_discount, palette='Blues_d')
plt.title('Average Discount Percentage by Category')
plt.xlabel('Category')
plt.ylabel('Average Discount Percentage')
plt.show()
