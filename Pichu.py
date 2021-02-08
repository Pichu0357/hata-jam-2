from hata import Client, Guild, sleep, Embed, Color, Emoji
from hata.ext.slash import setup_ext_slash
from dotenv import load_dotenv
from random import random, choice
from utilities import NekoFacts, neko 
import os

# loading the .env file
load_dotenv()

Token = os.environ.get('Token')
APPLICATION_ID = os.environ.get('APPLICATION_ID')
GUILD = Guild.precreate(os.environ.get('GUILD_ID'))

Pichu = Client(Token, application_id=APPLICATION_ID)
setup_ext_slash(Pichu)


# connecting to the client
@Pichu.events
async def ready(client):
    print(f'{client:f} logged in.')


@Pichu.interactions(guild=GUILD)
async def catfact(client, event, search: ('str', 'search using the keyword') = None):
    """ask me purrr!"""

    CAT_FACTS = NekoFacts.neko_facts()
    CAT_FACT_COLOR = Color.from_rgb(246, 211, 60)
    cat_sad = Emoji.precreate(os.environ.get('CAT_SAD'))

    if search is None:
        yield Embed("Here is your cat fact :cat:", description=choice(CAT_FACTS), color=CAT_FACT_COLOR)

    else:
        # bot is thinking... :p
        await client.interaction_response_message_create(event)
        message = await client.interaction_followup_message_create(event, "*Thinking...*")
        await sleep(1.0 + random() * 4.0)
        await client.interaction_followup_message_delete(event, message)

        # finding the possible facts by using the keyword
        matching = [s for s in CAT_FACTS if search in s]

        if matching:
            yield Embed("Here is your cat fact :cat:", description=choice(matching), color=CAT_FACT_COLOR)

        else:
            yield f"{cat_sad:e} sowwy, couldn't find"

        # cleaning the list
        del matching


@Pichu.interactions(guild=GUILD)
async def textcat(client, event):
    """I will send textcats :3"""
    return neko.textcat()


@Pichu.interactions(guild=GUILD)
async def owoify(client, event, text: ('str', 'Please, enter the message OwO')):
    """owoify :3"""
    OwO_COLOR = Color.from_html("#FF69B4")
    return Embed( color=OwO_COLOR).\
        add_field("Original:", text).\
        add_field("OwOify Text:", neko.owoify(text)).\
        add_footer("purrr!!!")


@Pichu.interactions(guild=GUILD)
async def nekogirl(client, event):
    """Wanna see nekogirls? OwO"""
    NEKOGIRL_COLOR = Color.from_html("#FFB6C1")
    NekoPeek = Emoji.precreate(os.environ.get("NEKO_PEEK"))
    return Embed(f"Here is your nekogirl {NekoPeek:e}", color=NEKOGIRL_COLOR).\
        add_image(neko.nekogirl())


@Pichu.interactions(guild=GUILD)
async def why(client, event):
    """Why are you using this commands?"""
    return neko.why()


# starting the bot
Pichu.start()
