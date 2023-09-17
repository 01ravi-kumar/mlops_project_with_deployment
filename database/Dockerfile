
# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=mlflow
ENV POSTGRES_PASSWORD=mlflow
ENV POSTGRES_DB=mydatabase

# Expose the PostgreSQL port
EXPOSE 5432


# create image 
# docker build -t my_postgres_image .   

# run container command
# docker run --name postgres_container -d -p 5001:5432 my_postgres_image