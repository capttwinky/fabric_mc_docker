import os

# Directory paths
directories = [
    "./data",
    "./mods",
    "./config/cobblemon",
    "./config/other-config-files"
]

# URLs for the required files
mod_urls = {
    "Fabric API": "https://www.curseforge.com/minecraft/mc-mods/fabric-api",
    "Cobblemon Mod": "https://www.curseforge.com/minecraft/mc-mods/cobblemon",
    "IChunUtil": "https://www.curseforge.com/minecraft/mc-mods/ichunutil",
    "Content Creator Integration Mod": "https://www.curseforge.com/minecraft/mc-mods/content-creator-integration-fabric"
}   

# Create directories
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Print URLs for the required files
print("\nRequired mod files can be downloaded from the following URLs:")
for mod_name, url in mod_urls.items():
    print(f"{mod_name}:\n\t{url}")
print("")   

print("""Choose the most up-to-date version of the mods and check the compatible Minecraft version.
      \tTake note of the most recent version of Minecraft that is supported by all of the plugins.
      \tThis will be the version of Minecraft that you will need to run your server.

      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
      \t    \tTAKE NOTE OF THIS MINECRAFT VERSION.
      !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

      \tFor each mod, visit the link and download the most recent version which is compatible with this version of Minecraft.
      \tPlace the downloaded mods in the './mods' directory.""")

while True:
    _ver = input("Which version of Minecraft is supported by all of the plugins? ")
    mresp = input(f"Are you sure that you want to use Minecraft version {_ver}? (y/n/quit) ").lower()
    match mresp:
        case "y":
            with open("./config/mc_server_version.env", "w") as f:
                f.write(f"VERSION={_ver}")
            print(f"Minecraft server version set to: {_ver}.")
            break
        case "quit":
            print("Minecraft server version not set.")
            break
        case _:
            continue
print("Edit ./config/mc_server_version.env to change the version of Minecraft server.")        
