import datetime
from telethon import TelegramClient
from telethon.sessions import StringSession

from config import config

async def start_telegram_session(api_id, api_hash, session_file='session.txt'):
    try:
        with open(session_file, 'r') as file:
            session_string = file.read().strip()
            client = TelegramClient(
                StringSession(session_string), api_id, api_hash
            )

    except (FileNotFoundError, ValueError):
        client = TelegramClient('new_session', api_id, api_hash)
    
    await client.start(config.phone)

    session_string = client.session.save()
    with open(session_file, 'w') as file:
        file.write(session_string)

    print("Session started and saved successfully.")
    return client

async def get_messages_from_chat(client: TelegramClient, chat_id: int):
    yesterday = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=1)
    chat = await client.get_entity(chat_id)
    messages = []
    async for msg in  client.iter_messages(chat, limit=1000):
        if msg.date > yesterday:
            messages.append(msg)
    return messages