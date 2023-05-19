import os
import datetime
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

VIEW_ID = 'ga:12345678'  # Replace with your Google Analytics View ID
EXCEL_FILE_NAME = 'Real-Time Data.xlsx'  # Replace with the name of your Excel file

# Set up credentials
credentials = Credentials.from_authorized_user_file('credentials.json', ['https://www.googleapis.com/auth/analytics.readonly'])
analytics = build('analytics', 'v3', credentials=credentials)

# Get real-time data
def get_realtime_data(view_id):
    try:
        # Query for real-time data
        results = analytics.data().realtime().get(
            ids=view_id,
            metrics='rt:activeUsers,rt:pageviews',
        ).execute()

        # Extract real-time data
        active_users = results['totalsForAllResults']['rt:activeUsers']
        pageviews = results['totalsForAllResults']['rt:pageviews']

        # Create a DataFrame with the data
        data = pd.DataFrame([[datetime.datetime.now(), active_users, pageviews]], columns=['Timestamp', 'Active Users', 'Pageviews'])

        # Write data to Excel file
        data.to_excel(EXCEL_FILE_NAME, index=False)
        print('Data written to Excel file successfully!')

    except Exception as e:
        print('An error occurred: {}'.format(e))


# Call the function to get real-time data and write to Excel file
get_realtime_data(VIEW_ID)
