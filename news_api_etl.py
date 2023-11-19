import requests
import csv
import s3fs

def fetch_news_headlines():
    # Specify your API key, S3 bucket name, and S3 object key here
    api_key = '*************************'
    s3_bucket_name = '*********************t'
    s3_object_key = 'bucket_name/news_headlines.csv'

    base_url = 'https://newsapi.org/v2/top-headlines'

    params = {
        'apiKey': api_key,
        'country': 'us',
        'pageSize': 5,
    }

    try:
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            articles = data['articles']
            headlines = [article['title'] for article in articles]

            csv_filename = 'news_headlines.csv'
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['headline']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for headline in headlines:
                    writer.writerow({'headline': headline})

            print(f"News headlines saved to '{csv_filename}'")

            fs = s3fs.S3FileSystem()
            with fs.open(f'{s3_bucket_name}/{s3_object_key}', 'wb') as s3_file:
                s3_file.write(open(csv_filename, 'rb').read())

            print(f"CSV file uploaded to S3 bucket: {s3_bucket_name}/{s3_object_key}")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage without main function
fetch_news_headlines()
