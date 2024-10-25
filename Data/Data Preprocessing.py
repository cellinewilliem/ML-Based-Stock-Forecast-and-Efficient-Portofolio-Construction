import pandas as pd

files = [
    "2010-2011.xlsx",
    "2012-2013.xlsx",
    "2014-2015.xlsx",
    "2016-2017.xlsx",
    "2018-2019.xlsx",
    "2020-2021.xlsx",
    "2022.xlsx"
]

# Load the data again
data_frames = [pd.read_excel(file) for file in files]
#combined_data = pd.concat(data_frames)

combined_data['Trading Date'] = pd.to_datetime(combined_data['Trading Date'])

# Group by 'Stock Code', resample by month, and get the last observation of each month
combined_data.set_index(['Trading Date', 'Stock Code'], inplace=True)
monthly_data = combined_data.groupby('Stock Code').resample('M', level='Trading Date').last()
monthly_data.reset_index(inplace=True)

# Show the restructured monthly data
#print(monthly_data.head())

# Add a new column for 'Month' derived from the 'Trading Date'
monthly_data['Month'] = monthly_data['Trading Date'].dt.to_period('M')

# Rearrange columns to include only the necessary ones and in the specified order
monthly_data = monthly_data[['Stock Code', 'P/E Ratio', 'P/B Ratio', 'Month']]

# Specify the path where you want to save the Excel file
output_file_path = "Monthly_PE_PBV_Data.xlsx"

# Write the DataFrame to an Excel file without the index
monthly_data.to_excel(output_file_path, index=False)
