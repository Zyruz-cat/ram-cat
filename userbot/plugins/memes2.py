from ..utils import admin_cmd, edit_or_reply, sudo_cmd

A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)

B = (
    "`╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `\n"
    "`╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `\n"
    "`╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `\n"
    "`╱┗━━━┛╰━━━╯┗━━━┛╱ `\n"
)


C = (
    "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
    "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
    "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
)

D = (
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n >🌹 *`"
    "`\n                    `"
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n🌹<\ *`"
)

E = (
    "`\n█████████`"
    "`\n█▄█████▄█`"
    "`\n█▼▼▼▼▼`"
    "`\n█  Hello Man`"
    "`\n█▲▲▲▲▲`"
    "`\n█████████`"
    "`\n ██   ██`"
)


@bot.on(admin_cmd(pattern=r"ml$"))
@bot.on(sudo_cmd(pattern="ml$", allow_sudo=True))
async def survivor(event):
    message = event.pattern_match.group(1)
    await edit_or_reply(
        event,
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`",
    )


@bot.on(admin_cmd(pattern=r"elove$"))
@bot.on(sudo_cmd(pattern="elove$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "░░▄███▄███▄\n░░█████████\n░░▒▀█████▀░\n░░▒░░▀█▀\n░░▒░░█░\n░░▒░█\n░░░█\n░░█░░░░███████\n░██░░░██▓▓███▓██▒\n██░░░█▓▓▓▓▓▓▓█▓████\n██░░██▓▓▓(◐)▓█▓█▓█\n███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█\n▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█\n░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█\n░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█\n░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█\n░▒░░▒░░░█▓▓▓█░░░█▓▓▓█\n░▒░░▒░░██▓██░░░██▓▓██\n██████████████████████\n█─████─▄▄─██─█─██─▄▄─█\n█─██▀█─██─██─█─██─▄█▀█\n█▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀",
    )


@bot.on(admin_cmd(pattern=r"gay$"))
@bot.on(sudo_cmd(pattern="gay$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
        "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
        "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
        "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈",
    )


@bot.on(admin_cmd(pattern=r"bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
        "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `",
    )


@bot.on(admin_cmd(pattern=r"hai$"))
@bot.on(sudo_cmd(pattern="hai$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HELLO!┊😀`"
        "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HELLO!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
        "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`",
    )


@bot.on(admin_cmd(pattern=r"nou$"))
@bot.on(sudo_cmd(pattern="nou$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
        "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
        "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
        "`\n┗━━┻━┛`",
    )


@bot.on(admin_cmd(pattern=r"sayhi$"))
@bot.on(sudo_cmd(pattern="sayhi$", allow_sudo=True))
async def survivor(event):
    await edit_or_reply(
        event,
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛",
    )


@bot.on(admin_cmd(pattern=r"fail$"))
@bot.on(sudo_cmd(pattern="fail$", allow_sudo=True))
async def survivor(fail):
    await edit_or_reply(fail, A)


@bot.on(admin_cmd(pattern=r"lool$"))
@bot.on(sudo_cmd(pattern="lool$", allow_sudo=True))
async def survivor(lool):
    await edit_or_reply(lool, C)


@bot.on(admin_cmd(pattern=r"lol$"))
@bot.on(sudo_cmd(pattern="lol$", allow_sudo=True))
async def survivor(lol):
    await edit_or_reply(lol, B)


@bot.on(admin_cmd(pattern=r"hallo$"))
@bot.on(sudo_cmd(pattern="hallo$", allow_sudo=True))
async def survivor(hallo):
    await edit_or_reply(hallo, E)


@bot.on(admin_cmd(pattern=r"nih$"))
@bot.on(sudo_cmd(pattern="nih$", allow_sudo=True))
async def survivor(nih):
    await edit_or_reply(nih, D)
