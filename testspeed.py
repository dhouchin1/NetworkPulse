import speedtest
import csv
from datetime import datetime

def test_speed():
    # Initialize Speedtest
    s = speedtest.Speedtest()

    # Perform the speed test
    s.download()
    s.upload()
    results = s.results.dict()

    # Extracting relevant data
    download_speed = results["download"] / 1_000_000 * 8 # Bytes to Megabits
    upload_speed = results["upload"] / 1_000_000 * 8 # Bytes to Megabits
    ping = results["ping"]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log data
    log_data(timestamp, download_speed, upload_speed, ping)

def log_data(timestamp, download, upload, ping):
    # Write data to CSV file
    with open('speed_test_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, download, upload, ping])

    # For immediate console output (optional)
    print(f"Timestamp: {timestamp}, Download Speed: {download}, Upload Speed: {upload}, Ping: {ping}")

def main():
    test_speed()

if __name__ == "__main__":
    main()
