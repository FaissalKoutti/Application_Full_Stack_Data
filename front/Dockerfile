# Import node v15 from DockerHub
FROM node:15

# Define the application directory
WORKDIR /

# Copy the file to the Docker image
COPY package.json .

# Install dependencies
RUN npm install --quiet

COPY . .