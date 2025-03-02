FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files into the container
COPY script.py . 
COPY IF-1.txt . 
COPY AlwaysRememberUsThisWay-1.txt . 

# Create an output directory inside the container & install dependencies
RUN mkdir -p /home/data/output && pip install --no-cache-dir --no-deps requests

# Define the command to run the script
CMD ["python", "script.py"]