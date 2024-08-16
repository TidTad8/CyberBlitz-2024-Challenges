# Use an official Node.js runtime as a parent image
FROM node:22.3.0

ENV VITE_API_URL=http://localhost:8000/api/

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that Vite will run on
EXPOSE 80

RUN npm run build

# Run the preview server
CMD ["npm", "run", "preview"]
