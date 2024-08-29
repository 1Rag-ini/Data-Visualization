# Dataset


import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker for generating sample data
fake = Faker()
# Define lists of Indian fruits and vegetables
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Papaya', 'Guava', 'Pineapple', 'Pomegranate', 'Grapes', 'Custard Apple']
vegetables = ['Potato', 'Onion', 'Tomato', 'Cauliflower', 'Spinach', 'Brinjal', 'Carrot', 'Beans', 'Capsicum', 'Cucumber']
# Define seasonal availability
seasons = ['Winter', 'Summer', 'Monsoon']
# Generate random data
data = []
for _ in range(500):
    item = random.choice(fruits + vegetables)
    category = 'Fruit' if item in fruits else 'Vegetable'
    price = round(random.uniform(10.0, 150.0), 2)  # Price between ₹10 and ₹150
    quantity = random.randint(1, 50)  # Quantity between 1 and 50 kg
    date = fake.date_this_year()
    season = random.choice(seasons)
    
    data.append([item, category, price, quantity, date, season])
# Create DataFrame
df = pd.DataFrame(data, columns=['Item', 'Category', 'Price (₹)', 'Quantity (kg)', 'Date', 'Season'])
# Save to CSV
df.to_csv('indian_fruits_vegetables_price_analysis.csv', index=False)

print("Dataset created successfully!")

