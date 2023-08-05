import pandas as pd
from datetime import datetime

def read_log_file(filename):
    # Initialize a dictionary to store extracted data in lists
    data = {'SongID': [], 'UserID': [], 'Country': []}

    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            # Use enumerate to get the line number for error reporting
            for line_num, line in enumerate(file, 1):
                # Remove leading/trailing whitespaces and newlines from each line
                line = line.strip()
                if line:
                    # Split the line using the '|' delimiter
                    elements = line.split('|')

                    # Check if the line has the expected number of elements (3)
                    if len(elements) != 3:
                        # Print an error message if the format is incorrect and skip to the next line
                        print(f"Skipping line {line_num}: Invalid format. Expected 3 elements, got {len(elements)}")
                        continue  # Skip this line and proceed to the next one

                    # Extract the three elements from the line: sng_id, user_id, and country
                    sng_id, user_id, country = elements

                    # Try to convert sng_id and user_id to integers (if not already integers)
                    try:
                        sng_id = int(sng_id)
                        user_id = int(user_id)
                    except ValueError as ve:
                        # Print an error message if the conversion fails and skip to the next line
                        print(f"Skipping line {line_num}: {ve}")
                        continue  # Skip this line and proceed to the next one

                    # Convert country to uppercase
                    country = country.upper()

                    # Append the extracted data to the corresponding lists in the data dictionary
                    data['SongID'].append(sng_id)
                    data['UserID'].append(user_id)
                    data['Country'].append(str(country))  # Convert country to string

    except FileNotFoundError:
        # If the file is not found, print an error message and return None
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        # For any other unexpected exception, print an error message and return None
        print(f"An error occurred: {e}")
        return None

    # Create a pandas DataFrame from the collected data
    df = pd.DataFrame(data)

    # Return the DataFrame containing the extracted data
    return df

def create_top_50_files(df, current_date):
    # Group by "Country" and "SongID" and calculate the number of streams for each song in each country
    group_df = df.groupby(['Country', 'SongID']).size().reset_index(name='Streams')

    # Sort the groups within each country based on the number of streams in descending order
    group_df = group_df.sort_values(by=['Country', 'Streams'], ascending=[True, False])

    # Create a new DataFrame that contains the top 50 songs for each country with their respective stream counts
    top_50_df = group_df.groupby('Country').head(50).reset_index(drop=True)

    # Convert the SongID column to strings
    top_50_df['SongID'] = top_50_df['SongID'].astype(str)

    # Write the data for each country to a separate text file
    for country, country_data in top_50_df.groupby('Country'):
        file_name = f"country_top50_{current_date}.txt"
        with open(file_name, 'a') as file:
            top_songs_str = ",".join([f"{song}:{streams}" for song, streams in zip(country_data['SongID'], country_data['Streams'])])
            file.write(f"{country}|{top_songs_str}\n")


if __name__ == "__main__":
    # Ask the user to enter the filename of the log file to process
    filename = input("Enter the filename: ")

    # Call the 'read_log_file' function to read the log file and extract data into a DataFrame
    df = read_log_file(filename)

    # Check if the DataFrame is not empty (i.e., the log file was successfully read and data extracted)
    if df is not None:
        # Check if the DataFrame contains any missing (NaN) values
        if df.isnull().values.any():
            # If there are missing values, drop those rows from the DataFrame
            df.dropna(inplace=True)

        # Get the current date in the format 'YYYYMMDD'
        current_date = datetime.now().strftime('%Y%m%d')

        # Use the current date to create the output text file with the top 50 records
        create_top_50_files(df, current_date)

        # Print a success message after the file is created
        print(f"The file was created correctly under the name of '{filename}'.")

