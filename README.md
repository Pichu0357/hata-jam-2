# hata-jam-2
Making slash commands for hata code jam 2 (related with nekogirl or cat).


## Pichu-bot
The Discord bot which is build in Hata no Kokoro's Discord API wrapper.

While setting up Pichu-bot, create a `.env` file. it should contain following values
```py
Token = ''                # bot token (str).
APPLICATION_ID = 0   	  # application id (int).
GUILD_ID = 0              # guild id for slash commands (int).
CAT_SAD = 0               # sad cat emoji's id (int).
NEKO_PEEK = 0		  # neko peek emoji's id (int).
```


## Features
- /cat: This will give a random cat image.
- /catfact: This will give a random cat fact. It has an optional search for a particular cat fact from the `CAT_FACTS`.
- /nekogirl: This will give you a random nekogirl image.
- /owoify: If you give a text, this is convert into owoify text.
- /textcat: Sends a random cat texts
- /why: Why did I added this? :p


## Requirements
The following packages are required to setting up Pichu-bot,
- [hata](https://www.github.com/HuyaneMatsu/hata)
- [dotenv](https://pypi.org/project/python-dotenv/)
- python3.9.1 or higher
