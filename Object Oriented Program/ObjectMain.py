from Objects import FortniteBot

bot1 = FortniteBot("Claude")
bot2 = FortniteBot("Chat")
bot3 = FortniteBot("Gemini")
bot4 = FortniteBot("Wonder")

bot1.take_damge(5)
bot2.take_damge(20)
bot3.take_damge(45)
bot4.take_damge(100)

print(bot1.name, bot2.name, bot3.name, bot4.name)
print(bot1.health, bot2.health, bot3.health, bot4.health)