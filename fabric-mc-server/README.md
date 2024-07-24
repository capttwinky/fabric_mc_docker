
# Minecraft Fabric Server with Cobblemon Mod

This project sets up a Dockerized Java Minecraft server running Fabric with the Cobblemon mod. 

Versions used:
- Minecraft: 1.20.1
- Fabric Loader: 0.11.7
- Fabric API: 0.92.2+1.20.1
- Cobblemon Mod: 1.5.2
- Docker: 20.10.8
- Docker Compose: 1.29.2
- Java: 16


This document also includes instructions for setting up the client to connect to the server using Fabric and Cobblemon.

## Prerequisites

- Docker and Docker Compose installed on the server

## Server Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Download the Fabric API mod**

   Download the Fabric api mod:
   https://www.curseforge.com/minecraft/mc-mods/fabric-api/files/all?page=1&pageSize=20&version=1.20.1
   the current version during development is 0.92.2+1.20.1.

3. **Download the Cobblemon mod**

   Download the Cobblemon mod:
   https://www.curseforge.com/minecraft/mc-mods/cobblemon/files/5375408 
   is the current version during development.

4. **move the downloads to the mods directory**

   ```bash
   mkdir -p mods
   mv <FABRIC_API_MOD_NAME> mods
   mv <COBBLEMON_MOD_NAME> mods
   ```

5. **Restart Docker Compose**

   Rebuild the Docker image if necessary.

   ```bash
   docker-compose down
   docker-compose build
   ```

6. **Run Docker Compose**

   Start the Docker Compose setup.

   ```bash
   docker-compose up -d
   ```

7. **Check Server Logs**

   Verify that the server starts correctly by checking the logs.

   ```bash
   docker logs fabric-mc-server
   ```

## Client Setup

1. **Install Minecraft Launcher**

   Ensure you have the Minecraft launcher installed on your system. You can download it from the official Minecraft website.

2. **Install Fabric Loader**

   Download and install the Fabric Loader for Minecraft. You can download it from the official Fabric website. 
   https://fabricmc.net/

   - Run the Fabric Installer.
   - Select the Minecraft version that matches your server.
   - Click "Install."

2. **Download Fabric API**

   Download the API for the Fabric mod. You can download it from the official Fabric website. 
   https://www.curseforge.com/minecraft/mc-mods/fabric-api/files/all?page=1&pageSize=20&version=1.20.1
   - Select the Minecraft version that matches your server.
   - Choose the most current version of the api that matches your Minecraft version.
   - Click "Download."
   - the current version during development is 0.92.2+1.20.1.

3. **Download Cobblemon Mod**

   Download the Cobblemon mod from its official source or a trusted mod repository. Make sure the version you download is compatible with the Minecraft version (1.20.1) and Fabric Loader you are using.
   - the current version during development is 1.5.2.
   - https://www.curseforge.com/minecraft/mc-mods/cobblemon/files/5375408

4. **Locate Minecraft Directory**

   Find your Minecraft directory. The location varies by operating system:
   - **Windows:** `C:\Users\<Your Username>\AppData\Roaming\.minecraft`
   - **macOS:** `~/Library/Application Support/minecraft`
   - **Linux:** `~/.minecraft`

5. **Create or Locate the Mods Folder**

   Inside the `.minecraft` directory, there should be a `mods` folder. If it doesn't exist, create it.

6. **Install the Mods**

   Copy the downloaded Cobblemon mod JAR file and any other required mod files into the `mods` folder.

7. **Launch Minecraft with Fabric Loader**

   - Open the Minecraft launcher.
   - In the bottom-left corner, select the profile that uses Fabric Loader.
   - Click "Play" to launch the game with the installed mods.

## Connecting to the Server

1. **Start Minecraft**

   Launch Minecraft using the Fabric Loader profile.

2. **Add Server**

   In the Minecraft main menu, navigate to "Multiplayer" and add a new server.

3. **Enter Server Details**

   Enter the IP address and port of your Dockerized Minecraft server.

4. **Join the Server**

   Connect to the server and enjoy playing with the Cobblemon mod.

## Troubleshooting

- **Server Logs:** Check the server logs for any errors or issues.
- **Mod Compatibility:** Ensure all mods are compatible with the Minecraft version and Fabric Loader you are using.
- **Firewall Settings:** Make sure your firewall settings allow connections to the Minecraft server port.

By following these steps, you should be able to set up and run a Minecraft server with Fabric and Cobblemon, as well as configure your client to connect to the server.
