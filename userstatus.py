# Module by DeCoded
# EW: https://endway.su/@decoded
# TG: https://t.me/whynothacked
# Канал с модулями: https://t.me/DeBot_userbot

from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest

from userbot import client

info = {'category': 'chat', 'pattern': '.afk|.work', 'description': 'Плашка AFK в нике|Плашка WORK в нике'}


@client.on(events.NewMessage(outgoing=True, pattern='.afk'))
async def afk(event):
    if event.fwd_from:
        return
    me = await event.client.get_me()
    first_name = me.first_name
    second_name = me.last_name
    if '[AFK] ' not in first_name:
        first_name = f'[AFK] {first_name}'
        await client(UpdateProfileRequest(
            first_name=first_name,
            last_name=second_name
        ))
        await event.edit('🛑 AFK статус активен')
    else:
        first_name = first_name.replace('[AFK] ', '')
        await client(UpdateProfileRequest(
            first_name=first_name,
            last_name=second_name
        ))
        await event.edit('🛑 AFK статус выключен')


@client.on(events.NewMessage(outgoing=True, pattern='.work'))
async def afk(event):
    if event.fwd_from:
        return
    me = await event.client.get_me()
    first_name = me.first_name
    second_name = me.last_name
    if '[WORK] ' not in first_name:
        first_name = f'[WORK] {first_name}'
        await client(UpdateProfileRequest(
            first_name=first_name,
            last_name=second_name
        ))
        await event.edit('🟢 WORK статус активен')
    else:
        first_name = first_name.replace('[WORK] ', '')
        await client(UpdateProfileRequest(
            first_name=first_name,
            last_name=second_name
        ))
        await event.edit('🟢 WORK статус выключен')
