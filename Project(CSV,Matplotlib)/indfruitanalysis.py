# Analysis
# Topic::Fresh Insights: Analyzing Fruits and Vegetables Price Trends
print('Topic::𝙁𝙧𝙚𝙨𝙝 𝙄𝙣𝙨𝙞𝙜𝙝𝙩𝙨: 𝘼𝙣𝙖𝙡𝙮𝙯𝙞𝙣𝙜 𝙁𝙧𝙪𝙞𝙩𝙨 𝙖𝙣𝙙 𝙑𝙚𝙜𝙚𝙩𝙖𝙗𝙡𝙚𝙨 𝙋𝙧𝙞𝙘𝙚 𝙏𝙧𝙚𝙣𝙙𝙨')
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('indian_fruits_vegetables_price_analysis.csv')
# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Pandas Function.
# 1. View Basic Information
print('View Basic Information::')
print(df.head())
print('===============================================================')
# Show the summary of the dataset
print('Show the summary of the dataset::')
print(df.info())
print('===============================================================')
# Describe numerical columns
print('Describe numerical columns::')
print(df.describe())
print('===============================================================')


# 2. Calculate Total and Average Prices by Category
total_price_by_category = df.groupby('Category')['Price (₹)'].sum()
print("Total Price by Category:")
print(total_price_by_category)
print('===============================================================')
avg_price_by_category = df.groupby('Category')['Price (₹)'].mean()
print("\nAverage Price by Category:")
print(avg_price_by_category)
print('===============================================================')


# 3. Find Maximum and Minimum Prices
max_price = df['Price (₹)'].max()
print(f"Maximum Price: ₹{max_price}")
print('===============================================================')
min_price = df['Price (₹)'].min()
print(f"Minimum Price: ₹{min_price}")
print('===============================================================')


# 4. Calculate Total Quantity by Season
total_quantity_by_season = df.groupby('Season')['Quantity (kg)'].sum()
print("\nTotal Quantity by Season:")
print(total_quantity_by_season)
print('===============================================================')


# 5. Filter Data
# Filter for high-priced items (price greater than ₹100)
high_price_items = df[df['Price (₹)'] > 100]
print("\nHigh-Priced Items:")
print(high_price_items.head())
print('===============================================================')
# Filter for items in a specific season (e.g., Summer)
summer_items = df[df['Season'] == 'Summer']
print("\nItems in Summer:")
print(summer_items.head())
print('===============================================================')


# 6. Count the Number of Items by Category
item_count_by_category = df['Category'].value_counts()
print("\nItem Count by Category:")
print(item_count_by_category)
print('===============================================================')


# 7. Calculate Correlation Between Price and Quantity
correlation = df[['Price (₹)', 'Quantity (kg)']].corr().iloc[0, 1]
print(f"\nCorrelation between Price and Quantity: {correlation:.2f}")
print('===============================================================')


# 8. Group and Aggregate Data
# Average price and quantity by category
avg_price_quantity_by_category = df.groupby('Category').agg({
    'Price (₹)': 'mean',
    'Quantity (kg)': 'mean'
})
print("\nAverage Price and Quantity by Category:")
print(avg_price_quantity_by_category)
print('===============================================================')


# Cleaning
# Check for missing values
print('Check for missing values::')
print(df.isnull().sum())
print('===============================================================')
# Drop rows with missing values (if any)
df = df.dropna()
# Check for duplicate rows
print('Check for duplicate rows::')
print(df.duplicated().sum())
print('===============================================================')
# Drop duplicate rows
df = df.drop_duplicates()
# Handle Inconsistent Data
# Example: Standardize the 'Season' column if there are inconsistencies
df['Season'] = df['Season'].str.strip().str.title()
# Verify unique values in the 'Season' column
print('Verify unique values in the "Season" column::')
print(df['Season'].unique())
print('===============================================================')



# Graphs
# 1. Histogram in Subplots for Price Distribution of Fruits and Vegetables
fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
# Plot price distribution for fruits
df[df['Category'] == 'Fruit']['Price (₹)'].plot(kind='hist', bins=20, alpha=0.7, ax=axes[0], color='orange')
axes[0].set_title('Price Distribution of Fruits')
axes[0].set_xlabel('Price (₹)')
axes[0].set_ylabel('Frequency')
axes[0].grid(True)
# Plot price distribution for vegetables
df[df['Category'] == 'Vegetable']['Price (₹)'].plot(kind='hist', bins=20, alpha=0.7, ax=axes[1], color='green')
axes[1].set_title('Price Distribution of Vegetables')
axes[1].set_xlabel('Price (₹)')
axes[1].set_ylabel('Frequency')
axes[1].grid(True)
plt.tight_layout()
plt.show()


# 2. Histogram in Subplots for Quantity Distribution of Fruits and Vegetables
fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)
# Plot quantity distribution for fruits
df[df['Category'] == 'Fruit']['Quantity (kg)'].plot(kind='hist', bins=20, alpha=0.7, ax=axes[0], color='orange')
axes[0].set_title('Quantity Distribution of Fruits')
axes[0].set_xlabel('Quantity (kg)')
axes[0].set_ylabel('Frequency')
axes[0].grid(True)
# Plot quantity distribution for vegetables
df[df['Category'] == 'Vegetable']['Quantity (kg)'].plot(kind='hist', bins=20, alpha=0.7, ax=axes[1], color='green')
axes[1].set_title('Quantity Distribution of Vegetables')
axes[1].set_xlabel('Quantity (kg)')
axes[1].set_ylabel('Frequency')
axes[1].grid(True)
plt.tight_layout()
plt.show()


# 3. Line Chart for Price Trends Over Time
monthly_avg_price = df.groupby([pd.Grouper(key='Date', freq='M'), 'Category'])['Price (₹)'].mean().unstack()
plt.figure(figsize=(14, 7))
monthly_avg_price.plot()
plt.title('Average Monthly Price Trends')
plt.xlabel('Date')
plt.ylabel('Average Price (₹)')
plt.legend(['Fruits', 'Vegetables'])
plt.grid(True)
plt.show()


# 4. Bar Chart for Seasonal Price Variation
seasonal_avg_price = df.groupby(['Season', 'Category'])['Price (₹)'].mean().unstack()
plt.figure(figsize=(10, 6))
seasonal_avg_price.plot(kind='bar')
plt.title('Average Price by Season and Category')
plt.xlabel('Season')
plt.ylabel('Average Price (₹)')
plt.legend(['Fruits', 'Vegetables'])
plt.grid(True)
plt.show()


# 5. Pie Chart for Price Distribution by Category
price_by_category = df.groupby('Category')['Price (₹)'].sum()
plt.figure(figsize=(8, 8))
price_by_category.plot(kind='pie', autopct='%1.1f%%', colors=['orange', 'green'], startangle=140)
plt.title('Price Distribution by Category')
plt.ylabel('')  # Hide the y-label
plt.show()


# 6. Pie Chart for Price Distribution by Season
price_by_season = df.groupby('Season')['Price (₹)'].sum()
plt.figure(figsize=(8, 8))
price_by_season.plot(kind='pie', autopct='%1.1f%%', colors=['blue', 'yellow', 'green'], startangle=140)
plt.title('Price Distribution by Season')
plt.ylabel('')  # Hide the y-label
plt.show()


# 7. Scatter Chart of Price vs. Quantity
plt.figure(figsize=(10, 6))
# Scatter plot for Fruits
df[df['Category'] == 'Fruit'].plot(kind='scatter', x='Quantity (kg)', y='Price (₹)', color='orange', alpha=0.6, label='Fruits', s=100, edgecolors='w')
# Scatter plot for Vegetables
df[df['Category'] == 'Vegetable'].plot(kind='scatter', x='Quantity (kg)', y='Price (₹)', color='green', alpha=0.6, label='Vegetables', s=100, edgecolors='w', ax=plt.gca())
plt.title('Price vs. Quantity for Fruits and Vegetables')
plt.xlabel('Quantity (kg)')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(True)
plt.show()


# 8.Bar Chart for Top 5 and Least 5 Selling Items
# Calculate total sales for each entry
df['Total Sales (₹)'] = df['Price (₹)'] * df['Quantity (kg)']
# Aggregate sales by item
item_sales = df.groupby('Item')['Total Sales (₹)'].sum().reset_index()
# Top 5 items
top_5_items = item_sales.sort_values(by='Total Sales (₹)', ascending=False).head(5)
# Least 5 items
least_5_items = item_sales.sort_values(by='Total Sales (₹)').head(5)
# Plotting Top 5 Items
plt.figure(figsize=(12, 6))
plt.bar(top_5_items['Item'], top_5_items['Total Sales (₹)'], color='lightblue', edgecolor='black')
plt.title('Top 5 Selling Fruits and Vegetables')
plt.xlabel('Item')
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
# Plotting Least 5 Items
plt.figure(figsize=(12, 6))
plt.bar(least_5_items['Item'], least_5_items['Total Sales (₹)'], color='lightpink', edgecolor='black')
plt.title('Least 5 Selling Fruits and Vegetables')
plt.xlabel('Item')
plt.ylabel('Total Sales (₹)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()


# 9.Bar Chart in subplot for top 5 and least 5 selling fruits and vegetables
# Calculate total sales for each entry
df['Total Sales (₹)'] = df['Price (₹)'] * df['Quantity (kg)']
# Separate fruits and vegetables
fruits_df = df[df['Category'] == 'Fruit']
vegetables_df = df[df['Category'] == 'Vegetable']
# Aggregate sales by item
fruits_sales = fruits_df.groupby('Item')['Total Sales (₹)'].sum().reset_index()
vegetables_sales = vegetables_df.groupby('Item')['Total Sales (₹)'].sum().reset_index()
# Top 5 and least 5 items for fruits
top_5_fruits = fruits_sales.sort_values(by='Total Sales (₹)', ascending=False).head(5)
least_5_fruits = fruits_sales.sort_values(by='Total Sales (₹)').head(5)
# Top 5 and least 5 items for vegetables
top_5_vegetables = vegetables_sales.sort_values(by='Total Sales (₹)', ascending=False).head(5)
least_5_vegetables = vegetables_sales.sort_values(by='Total Sales (₹)').head(5)
# Plotting
fig, axs = plt.subplots(2, 2, figsize=(10, 10), sharey=True)
# Top 5 fruits
axs[0, 0].bar(top_5_fruits['Item'], top_5_fruits['Total Sales (₹)'], color='lightgreen')
axs[0, 0].set_title('Top 5 Selling Fruits')
axs[0, 0].set_xlabel('Item')
axs[0, 0].set_ylabel('Total Sales (₹)')
axs[0, 0].tick_params(axis='x', rotation=45)
# Least 5 fruits
axs[0, 1].bar(least_5_fruits['Item'], least_5_fruits['Total Sales (₹)'], color='lightcoral')
axs[0, 1].set_title('Least 5 Selling Fruits')
axs[0, 1].set_xlabel('Item')
axs[0, 1].set_ylabel('Total Sales (₹)')
axs[0, 1].tick_params(axis='x', rotation=45)
# Top 5 vegetables
axs[1, 0].bar(top_5_vegetables['Item'], top_5_vegetables['Total Sales (₹)'], color='lightblue')
axs[1, 0].set_title('Top 5 Selling Vegetables')
axs[1, 0].set_xlabel('Item')
axs[1, 0].set_ylabel('Total Sales (₹)')
axs[1, 0].tick_params(axis='x', rotation=45)
# Least 5 vegetables
axs[1, 1].bar(least_5_vegetables['Item'], least_5_vegetables['Total Sales (₹)'], color='lightpink')
axs[1, 1].set_title('Least 5 Selling Vegetables')
axs[1, 1].set_xlabel('Item')
axs[1, 1].set_ylabel('Total Sales (₹)')
axs[1, 1].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()
