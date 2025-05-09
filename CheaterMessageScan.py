import discord
import json

# roles of admins, bots, chat mods so they aren't counted
roles = [331493607389397002, 274971100184576010,274971100184576010, 389150267293302784, 1103150321787744276, 638151194606436352, 887080470314090557, 1365359593122697249, 117737991102922752, 286709603750903808, 286711345091706881, 286704030464606208, 328456330086055937, 1234269971006361701]

with open('ServerCheater.json', 'r') as f:
    map = json.load(f)
    
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        content = message.content.lower()
        if "cheat" in content or "hack" in content or "no admins"  in content or "report" in content:
            sender = message.author
            userRoles = sender.roles
            for role in userRoles:
                if role.id in roles:
                    return
            server = message.guild
            print(f"{sender.name} in {server.name}")
            print(f"msg: {content}")
            if server.name not in map:
                map[server.name] = 1
            else:
                map[server.name] += 1   
            with open('ServerCheater.json', 'w') as f:
                json.dump(map, f)


client = MyClient()
with open('token.txt', 'r') as f:
    token = f.read().strip()
if(not token):
    print("Token not found")
    exit(1)
client.run(token)