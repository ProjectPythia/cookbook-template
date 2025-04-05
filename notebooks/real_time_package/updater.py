import boto3
import datetime
import time
from botocore import UNSIGNED
from botocore.client import Config
import os

def get_updated_files(year, julian_day, last_modified_cutoff):
    """
    Get files from an S3 bucket that were modified after a given datetime.

    :param year: The year to check.
    :param julian_day: The Julian day to check.
    :param last_modified_cutoff: The cutoff datetime for filtering files.
    :return: A list of file keys that were modified after the given datetime.
    """
    # Initialize the S3 client with anonymous access
    s3_client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    # Define the bucket name
    bucket_name = 'noaa-goes16'

    # List to store the filtered files
    filtered_files = []

    # Iterate over each hour of the day
    for hour in range(24):
        # Construct the S3 prefix
        prefix = f'ABI-L1b-RadF/{year}/{julian_day:03d}/{hour:02d}/'

        # List objects within the specified prefix to get file names
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        # Process the list of files
        if 'Contents' in response:
            for obj in response['Contents']:
                last_modified = obj['LastModified']
                # Ensure last_modified is timezone-aware
                if last_modified.tzinfo is None:
                    last_modified = last_modified.replace(tzinfo=datetime.timezone.utc)
                if last_modified > last_modified_cutoff:
                    filtered_files.append(obj['Key'])

    return filtered_files

def write_path_to_file(file_path, new_paths):
    """
    Write the in-memory data to a file.

    :param file_path: The path to the file to write to.
    :param new_paths: A list of new paths to write.
    """
    with open(file_path, 'w') as f:
        for path in new_paths:
            f.write(f"{path}\n")

def main():
    # Define the path to the file that stores the channel paths
    file_path = 'channel_paths.txt'

    while True:
        # Get the current UTC time
        now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)

        # Extract year and Julian day
        year = now.year
        julian_day = now.timetuple().tm_yday

        # Define the cutoff time for filtering
        # Set the cutoff to 10 minutes before the current time
        last_modified_cutoff = now - datetime.timedelta(minutes=10)

        # Get the list of files modified after the cutoff time
        updated_files = get_updated_files(year, julian_day, last_modified_cutoff)

        # Write the new paths to the file, replacing the old content
        write_path_to_file(file_path, updated_files)

        # Print the current time and the number of updated files
        print(f"{datetime.datetime.now()} - Updated {len(updated_files)} files.")
        
        # Sleep for 10 minutes before checking again
        time.sleep(600)  # 600 seconds = 10 minutes

if __name__ == "__main__":
    main()
