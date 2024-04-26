# ChatBuzzBot

## Overview

ChatBuzzBot is a chatbot that generates a word cloud from the most popular words in a chat each day, providing a visual representation of trending topics and discussions. This bot is designed to enhance user engagement by showcasing the most active themes in your community.

## Features

- **Automated Daily Word Clouds**: Generates word clouds daily to reflect the latest trends in chat discussions.
- **Customization Options**: Allows customization of the word cloud, including exclusions, specific word highlights, and more.
- **Interactive Queries**: Users can interact with the bot to retrieve word clouds for specific dates or topics.
- **User-Friendly**: Simple commands and easy integration with chat platforms.

## How It Works

DailyWordCloudBot scans the chat for frequently mentioned words and uses them to create a visually appealing word cloud. This process involves filtering out common stop words and focusing on meaningful terms that reflect current discussions.
## How It Looks
![image](https://github.com/venceslavMuhomor/chat_buzz_bot/assets/46605823/aec1173c-83c3-4c68-89b1-865530bb3028)

## Installation

1. Clone the repository:

    ```bash
   https://github.com/venceslavMuhomor/chat_buzz_bot.git
2. Create .env file
3. Create stop.json custom stop words file if u need (just list with words ["stop_word", "stop_word2"...])
4. After first start 
      ```bash
      python main.py
5. U must create tg session, paste code that u receive from tg
    ![image_2024-04-26_22-57-44](https://github.com/venceslavMuhomor/chat_buzz_bot/assets/46605823/8010b0a1-8126-474d-a008-35a144a5f834)
6. If u need docker
     ```bash
     docker build -t image_name .
     docker run --rm image_name
