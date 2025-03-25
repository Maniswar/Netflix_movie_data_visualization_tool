# Task: Create a Data Visualization Tool

# Build a tool that takes a dataset and generates interactive visualizations using libraries such as Matplotlib, Seaborn, or Plotly.
# This task will enhance their understanding of data visualization principles and plotting techniques.

# Taking Matplotlib for Data Visualization

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
df = pd.read_csv("C:\\Users\\DELL\\Desktop\\My Files\\Internships\\Python Development\\Level_3\\netflix.csv")  #change path according to your dataset
# print(df)
# Creating the DataFrame
count_df = pd.DataFrame({'type': ['Movie', 'TV Show'], 'count': [6126, 2664]})

# Plot the bar chart
labels = np.array(['movie','Tv Show'])
plt.figure(figsize=(6, 4))  # Set figure size
plt.bar(count_df['type'], count_df['count'], color=['blue', 'green'], label = labels)

# Add labels and title
plt.xlabel("Type")
plt.ylabel("Count")
plt.title("Distribution of TV Shows and Movies")
plt.yticks(range(1,6500, 300), fontsize=5,fontweight='bold')  # Y-ticks from 1 to 3000 with step 5
plt.legend()
# Show the plot
plt.show()

# # Creating the DataFrame
count_df = pd.DataFrame({'type': ['Movie', 'TV Show'], 'count': [6126, 2664]})

# Calculate the total count
Total = count_df['count'].sum()  # Sum of the counts

# Create a DataFrame for the total
total_df = pd.DataFrame({'type': ['Total'], 'count': [Total]})

# Concatenate the total first, then the original data
count_df = pd.concat([total_df, count_df], ignore_index=True)

# Plot the bar chart
labels = np.array(['Total', 'movie','Tv Show'])
plt.figure(figsize=(6, 4))  # Set figure size
plt.bar(count_df['type'], count_df['count'], color=['red', 'blue', 'green'], label = labels)  # Bars for Total, Movies, TV Shows

# Add labels and title
plt.xlabel("Type")
plt.ylabel("Count")
plt.yticks(range(1,8999, 300), fontsize=5,fontweight='bold')  # Y-ticks from 1 to 3000 with step 5
plt.title("Distribution of Total, TV Shows, and Movies")
plt.legend()

# Show the plot
plt.show()

# # Creating the DataFrame
count_df = pd.DataFrame({'type': ['Movie', 'TV Show'], 'count': [6126, 2664]})

# Calculate the total count
Total = count_df['count'].sum()

# Plotting the stacked bar chart
plt.figure(figsize=(6, 4))  # Set figure size

# Plotting the total as a separate bar
plt.bar('Total', Total, color='red', label='Total')

# Plotting the individual counts first (Movies + TV Shows)
plt.bar('Movies and TV Shows', count_df['count'][0], color='g', label='Movies')  # Movies
plt.bar('Movies and TV Shows', count_df['count'][1], bottom=count_df['count'][0], color='b', label='TV Shows')  # TV Shows

# Adding labels and title
plt.xlabel("Type")
plt.ylabel("Count")
plt.title("Stacked Bar Graph for Movies and TV Shows with Total")
plt.yticks(range(1,8999, 300), fontsize=5,fontweight='bold')  # Y-ticks from 1 to 8000 with step 300

# Adding legend
plt.legend()

# Show the plot
plt.show()

# Group by 'country' and 'type', and count occurrences of each combination
country_counts = df.groupby(['country', 'type']).size().unstack(fill_value=0)

# Reset the index to turn the 'country' into a regular column
country_counts = country_counts.reset_index()
# Now, create the bar chart using plt.bar()
plt.figure(figsize=(10, 6))

# Bar width
# bar_width = 1.5
index = range(len(country_counts))  # X-axis positions for countries

# Plot Movies as blue bars with adjusted width
plt.bar(index, country_counts['Movie'], color='red', label='Movies', align='center')

# Plot TV Shows as green bars, stacking on top of Movies
plt.bar(index, country_counts['TV Show'], bottom=country_counts['Movie'], color='blue', label='TV Shows', align='center')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Stacked Bar Graph of Movies and TV Shows per Country')

# Add country names on x-axis
plt.xticks(index, country_counts['country'], rotation=90, fontsize=8, fontweight='bold', ha='right')
plt.yticks(range(1, 3001, 100), fontsize=5, fontweight='bold')  # Y-ticks from 1 to 3000 with step 5

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout to avoid label overlap
plt.show()

# Step 1: Filter the DataFrame for Movies
movies_df = df[df['type'] == 'Movie']

# Step 2: Filter the DataFrame for TV Shows
tv_shows_df = df[df['type'] == 'TV Show']

# Step 3: If you want a list of countries for Movies and TV Shows
movies_list = movies_df['country'].tolist()
tv_shows_list = tv_shows_df['country'].tolist()

# Step 4: If you want a list of genres (from the 'listed_in' column) for Movies and TV Shows
movies_genres_list = movies_df['listed_in'].tolist()
tv_shows_genres_list = tv_shows_df['listed_in'].tolist()
# # Display the lists
# print("Movies List:")
# print(movies_list)

# print("\nTV Shows List:")
# print(tv_shows_list)

# print("\nMovies Genres List:")
# print(movies_genres_list)

# print("\nTV Shows Genres List:")
# print(tv_shows_genres_list)
# Step 1: Count the occurrences of each country in the Movies list
country_counts = pd.Series(movies_list).value_counts()

# Step 2: Create a bar graph
plt.figure(figsize=(10, 6))  # Set figure size
country_counts.plot(kind='bar', color='blue')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Number of Movies')
plt.title('Number of Movies per Country')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()

# Step 3: Count the occurrences of each country in the TV Shows list
country_counts_tv_shows = pd.Series(tv_shows_list).value_counts()

# Step 4: Create a bar graph
plt.figure(figsize=(10, 6))  # Set figure size
country_counts_tv_shows.plot(kind='bar', color='green')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Number of TV Shows')
plt.title('Number of TV Shows per Country')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()

# Step 1: Filter the DataFrame for Movies
movies_df = df[df['type'] == 'Movie'].copy()  # Using .copy() to avoid the warning

# Step 2: Ensure that 'listed_in' column contains strings using .loc
movies_df.loc[:, 'listed_in'] = movies_df['listed_in'].astype(str)

# Step 3: Split genres by commas and explode the list to create individual genre rows
movies_genres_list = movies_df['listed_in'].str.split(',').explode()

# Step 4: Strip any leading/trailing spaces in genre names
movies_genres_list = movies_genres_list.str.strip()

# Step 5: Count the occurrences of each genre
movie_genre_counts = movies_genres_list.value_counts()

# Step 6: Create a bar graph for Movies
plt.figure(figsize=(10, 6))  # Set figure size
movie_genre_counts.plot(kind='bar', color='purple')

# Add labels and title
plt.xlabel('Genre')
plt.ylabel('Number of Movies')
plt.title('Genre Distribution for Movies')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()

# Step 7: Filter the DataFrame for TV Shows
tv_shows_df = df[df['type'] == 'TV Show'].copy()  # Using .copy() to avoid the warning

# Step 8: Ensure that 'listed_in' column contains strings using .loc
tv_shows_df.loc[:, 'listed_in'] = tv_shows_df['listed_in'].astype(str)

# Step 9: Split genres by commas and explode the list to create individual genre rows
tv_shows_genres_list = tv_shows_df['listed_in'].str.split(',').explode()

# Step 10: Strip any leading/trailing spaces in genre names
tv_shows_genres_list = tv_shows_genres_list.str.strip()

# Step 11: Count the occurrences of each genre
tv_show_genre_counts = tv_shows_genres_list.value_counts()

# Step 12: Create a bar graph for TV Shows
plt.figure(figsize=(10, 6))  # Set figure size
tv_show_genre_counts.plot(kind='bar', color='orange')

# Add labels and title
plt.xlabel('Genre')
plt.ylabel('Number of TV Shows')
plt.title('Genre Distribution for TV Shows')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout()
plt.show()