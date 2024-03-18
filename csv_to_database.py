import sys
import csv  # Add this import statement
from app.models import SEO

def load_data_from_csv(csv_file_path):
    try:
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Check if 'visits' is empty or null
                if 'visits' not in row or not row['visits']:
                    print("Skipping row with missing 'visits' value:", row)
                    continue
                
                seo_instance = SEO(
                    domain=row['domain'],
                    visits=row['visits'],
                )
                seo_instance.save()
        print("Data loaded successfully!")
        sys.stdout.flush()
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.stdout.flush()

# Specify the path to your CSV file
csv_file_path = 'C:/Users/admin/Downloads/Book1.csv'

# Call the function to load data into the database
load_data_from_csv(csv_file_path)
