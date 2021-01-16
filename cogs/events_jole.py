from discord.ext import commands

def sqlify(path):
    return ''.join(open(path, 'r').readlines())

class Event_jole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.bot.pool.execute(sqlify('./sql_files/guild_join.sql'), False, guild.id, None, None, None)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        await self.bot.pool.execute(sqlify('./sql_files/guild_leave.sql'), guild.id)

def setup(bot):
    bot.add_cog(Event_jole(bot))
