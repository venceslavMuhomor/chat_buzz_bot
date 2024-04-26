import asyncio
from channel_parser import get_messages_from_chat, start_telegram_session
from config import config
from word_analysis import common_words_list, words_cloud
from sender import send_to_chat

async def main():
    client = await start_telegram_session(
        api_id = config.api_id.get_secret_value(),
        api_hash = config.api_hash.get_secret_value() 
    )
    messages = await get_messages_from_chat(client, -config.chat_id)

    common_words = common_words_list(
        messages=messages,
        words_count=config.words_count 
    )

    w_cloud = words_cloud(common_words)

    await send_to_chat(chat_id=-config.chat_id, file=w_cloud)

if __name__ == '__main__':
    asyncio.run(main())