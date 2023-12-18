# Use the official Python image
FROM python:latest

# Set the working directory
WORKDIR /app

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire source code to the working directory
COPY src/ .

RUN apt-get install -y tzdata
ENV TZ=Europe/Andorra
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Specify the command to run your application
CMD ["python", "main.py"]