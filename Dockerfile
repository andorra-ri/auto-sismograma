# Use the official Python image
FROM python:latest

# Update package list
RUN apt-get update

# Set the working directory
WORKDIR /app

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the entire source code to the working directory
COPY src/ .

# Set the timezone
RUN apt-get install -y tzdata
ENV TZ=Europe/Andorra
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Configure cron execution
RUN apt-get -y install cron
COPY cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile

# Specify the command to run your application
CMD ["cron", "-f"]
