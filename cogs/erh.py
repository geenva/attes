from discord.ext import commands
import discord, sys, traceback

class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (
            commands.CommandNotFound,
            discord.errors.NotFound
        )

        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.BadArgument):
            return await ctx.send("Invalid usage of the command, please run `.help command`!")

        elif isinstance(error, commands.CommandOnCooldown):
            return await ctx.send('You\'re on an cooldown!')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'You didn\'t include all required arguments!')

        elif isinstance(error, commands.errors.BadUnionArgument):
            return await ctx.send("Member could not be found.")

        elif isinstance(error, commands.BotMissingPermissions):
            return await ctx.author.send('I am missing permissions to execute this command!')

        elif isinstance(error, commands.MissingPermissions):
            return await ctx.author.send('You do not have sufficient permission(s) to execute this command!')

        elif isinstance(error, commands.NoPrivateMessage):
            return await ctx.send('You may not use this command in dm\'s!')

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(ErrorHandler(bot))
