FROM openjdk:17-jdk-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y wget curl

# Download Fabric server launcher
RUN wget -O fabric-server-launcher.jar https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.15.11/1.0.1/server/jar
# Accept the EULA
RUN echo "eula=true" > eula.txt

# Expose port
EXPOSE 25565

# Command to print the version
CMD ["java", "-Xmx2g", "-jar", "fabric-server-launch.jar", "nogui"]

