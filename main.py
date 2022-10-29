import discord
from replit import db
import random
# import requests

from keep_alive import keep_alive


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        try:
            print('Message from {0.author}: {0.content}'.format(message))
            if message.author != self.user:
                if message.content.startswith("+help"):
                    await message.channel.send("Go help yourself...")
                elif message.content.startswith("+u"):
                    await message.channel.send("your username is {}".format(
                        message.author))

                elif message.content.startswith("+add"):
                    if message.author.guild_permissions.administrator:
                        key = message.content.split(" ")[1]
                        if db.get(key) != None:
                            keys = db.get(key)
                            keys = list(keys) + message.content.split(
                                "+add {}".format(key), 1)[1].split("\n")
                            await message.channel.send(
                                "Added {} key(s) successfully".format(key))
                        else:
                            keys = message.content.split(
                                "+add {}".format(key), 1)[1].split("\n")
                            await message.channel.send(
                                "```Added {} key(s) successfully```".format(
                                    key))
                        db[key] = keys
                    else:
                        await message.channel.send(
                            "```You do not permissin to do that```")

                elif message.content.startswith("+stock"):
                    embed = discord.Embed(
                        title="Available Keys",
                        description="Steam : Unlimited\nUbisoft : Unlimited",
                        color=0x00ff00)
                    await message.channel.send(embed=embed)
                elif message.content.startswith("+reveal"):
                    if message.author.guild_permissions.administrator:
                        for i in db.keys():
                            if (db.get(i)[0] == ''):
                                del db.get(i)[0]
                            data = i + " : " + str(list(db.get(i)))
                            await message.channel.send("```" + str(data) +
                                                       "```")
                        if len(db.keys()) == 0:
                            await message.channel.send("```No Data```")
                    else:
                        await message.channel.send(
                            "```You do not permissin to do that```")

                elif message.content.startswith("+get"):
                    key = message.content.split(" ")[1]
                    s = "QWERTYUIOPLKJHGFDSAZXCVBNM01234567899"
                    if ((key == "ubisoft") or (key == "steam")):
                        if db.get(key) == None:
                            db[key] = []
                    else:
                        raise Exception
                    if key == "ubisoft":
                        j = 0
                        while (True):
                            j += 1
                            rl = ""
                            c = 0
                            end = random.choice([19, 23])
                            k = 4 if end == 19 else 3
                            print(k)
                            for i in range(end):
                                if len(rl) != 0 and len(rl) % (k) == c:
                                    rl = rl + "-"
                                    c, k = c + 1, k + 4
                                else:
                                    rl = rl + s[random.randint(0, len(s) - 1)]
                            # print(j)
                            print(rl)
                            if rl not in db[key]:
                                db[key].append(rl)
                                # print(rl)
                                print(db[key])
                                await message.channel.send(rl)
                                break
                    elif key == "steam":
                        j = 0
                        while (True):
                            j += 1
                            rl = ""
                            c, k = 0, 5
                            for i in range(random.choice([17, 29])):
                                if len(rl) != 0 and len(rl) % (k) == c:
                                    rl = rl + "-"
                                    c, k = c + 1, k + 5
                                else:
                                    rl = rl + s[random.randint(0, len(s) - 1)]
                            # print(j)
                            print(rl)
                            if rl not in db[key]:
                                db[key].append(rl)
                                print(rl)
                                print(db[key])
                                await message.author.send(
                                    "Your Steam Key: {0}".format(rl))
                                break
        except Exception as e:
            await message.channel.send("```Invalid Syntax```")
            print(e)


client = MyClient()
client.run('OTUzNjg3MDA3MTY1NTUwNjMy.YjIMPQ.rlI46LVPqwWdY6KFgVzLY9z2GDY')
keep_alive()
