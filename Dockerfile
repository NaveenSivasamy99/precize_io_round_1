# Use an official Python runtime as a parent image
FROM python3.9-slim

# Set the working directory in the container
WORKDIR app

# Copy the current directory contents into the container at app
COPY . app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir requests

# Make the output directory
RUN mkdir output

# Run generate_report.py when the container launches
CMD [python, generate_report.py]
