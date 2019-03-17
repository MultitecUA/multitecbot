# coding=utf-8
# MULTITECBOT creado por Esteban Escobar.
# Basado en la API de creación de bots en python. Para más información consultar su repositorio en github (https://github.com/python-telegram-bot/python-telegram-bot).
import webbrowser
import telegram
import logging
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


TOKEN = '755869851:AAFBJEPnW5kyV8xmK-We-Pj7fGRam4XRP8o' # Asignamos a la variable TOKEN el hash de nuestro bot para facilitar su utilización más adelante.

AYUDA = 'Hola! soy el bot oficial de Multitec, me encargo de gestionar los grupos y el canal de la asociación, puedes utilizar los siguientes comandos : \n\n/comandos - Lista de comandos. \n/chiste - Que el bot te cuente un chiste \n/eventos - Informacion sobre Eventos \n/pagina - Nuestra web \n/inscripcion - Link del formulario de inscripción\n/redes_sociales - Enlaces a las redes sociales de la Comunidad\n/stickers - Pack de stickers de Multitec UA' # Mensaje de ayuda y bienvenida.

#COMANDOS
COMANDOS = '/comandos - lista de comandos. \n/chiste - Que el bot te cuente un chiste \n/eventos - Informacion sobre Eventos \n/pagina - Nuestra web \n/inscripcion - Link del formulario de inscripción\n/redes_sociales - Enlaces a las redes sociales de la Comunidad\n/stickers - Pack de stickers de Multitec UA'

#EVENTOS
EVENTOS = 'CALENDARIO DE EVENTOS\n\n📆 1 de diciembre hay Ludum Dare y ya se ha abierto el plazo para sugerir temas:https://ldjam.com/events/ludum-dare/43/theme\nLudum Dare is one of the worlds largest and longest running Game Jam events. Every 4 months, we challenge creators to make a game from scratch in a weekend\n\nTORREVIEJA\n-Nueva edición Hackea Tu Destino! https://www.eventbrite.es/e/entradas-hackea-tu-destino-2018-52450812793\nCentrada en la innovación en turismo y el desarrollo de aplicaciones y tecnologías que resuelvan problemas actuales y aporten nuevos puntos de vista relacionados con el ambito turístico.\n📆 ¿Cuándo? Del 24 de noviembre de 2018 a las 10:00h hasta el 25 de noviembre de 2018 a las 18:00h.'

#EVENTOS
REDES_SOCIALES = '¡Síguenos en nuestras redes sociales!\nNuestra Web\nmultitecua.ml\nTwitter\n  twitter.com/multitecua\nLinkedIn\nlinkedin.com/company/multitecua\nInstagram\ninstagram.com/multitecua/\nFacebook\nfacebook.com/MultitecUA\nYouTube \nyoutube.com/channel/UComtzTLqL-jHvRhiQVrzPJg?sub_confirmation=1\nDiscord \n https://discord.gg/pcyuxX9'

#inscripcion
INSCRIPCION = 'https://docs.google.com/forms/d/18s-7T9IxWPlnRpncwwZjqm6utwLan9IkMOORfk2ytNs/viewform?edit_requested=true'

#pagina
PAGINA = 'Aquí tienes nuestra página web, pronto ofrecerá muchos más servicios: multitecua.ml'

#stickers
STICKERS = 'https://t.me/addstickers/multitecua'


#Chistes
CHISTE1 = 'Aprobar todas con primera matrícula'
CHISTE2 = '-¿En qué se parecen un ingeniero y un arquitecto?\n-Los dos trabajan en el burguer'
CHISTE3 = '-Pone Ud en su currículum que se le da bien la construcción.\n-Desde Lego.'
CHISTE4 = 'Tu cara sí que es un chiste'
CHISTE5 = '¿Qué es un terapeuta? – 1024 Gigapeutas.'
CHISTE6 = '¿Que le dicen un bit al otro? Nos vemos en el bus.'
CHISTE7 = 'Están 1023 gigabytes en una fiesta, llegan 1048576 más y dicen: ¿Nos hacemos un peta?.'
CHISTE8 = 'No te despedirán del trabajo, si nunca comentas tu código y además eres el único que sabe cómo funciona.'
CHISTE9 = ' Sólo hay 10 tipos de personas en este mundo, las que entienden binario y las que no.'
CHISTE10 = 'Dios es real, a no ser que lo declares como integer.'
CHISTE11 = '¿Cuántos programadores hacen falta para cambiar una bombilla? – Ninguno, porque es un problema hardware.'

CHISTES = [CHISTE1, CHISTE2, CHISTE3, CHISTE4, CHISTE5, CHISTE6, CHISTE7, CHISTE8, CHISTE9, CHISTE10, CHISTE11]

############################################################################################

bot = telegram.Bot(token = TOKEN) # Creamos nuestro objeto bot con el TOKEN anterior.


updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Codigo que ejecuta el comando /start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=AYUDA)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

#COMANDO CHISTE.
def chiste(bot, update):
    i = random.randint(0,10)
    bot.send_message(chat_id = update.message.chat_id, text = CHISTES[i])

start_handler= CommandHandler('chiste', chiste)
dispatcher.add_handler(start_handler)

#Comando eventos
def eventos(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = EVENTOS)

start_handler = CommandHandler('eventos', eventos)
dispatcher.add_handler(start_handler)

#comando lista de comandos
def comandos(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = COMANDOS)

start_handler = CommandHandler('comandos', comandos)
dispatcher.add_handler(start_handler)

#Comando redes sociales
def redes_sociales(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = REDES_SOCIALES)

start_handler = CommandHandler('redes_sociales', redes_sociales)
dispatcher.add_handler(start_handler)

#Inscripcion
def inscripcion(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = INSCRIPCION)

start_handler = CommandHandler('inscripcion', inscripcion)
dispatcher.add_handler(start_handler)

#Pagina
def pagina(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = PAGINA)

start_handler = CommandHandler('pagina', pagina)
dispatcher.add_handler(start_handler)

#Stickers
def stickers(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = STICKERS)

start_handler = CommandHandler('stickers', stickers)
dispatcher.add_handler(start_handler)

#por si alguien pone un comando inexistente
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Lo siento, no entiendo ese comando")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# Con esto el bot hará echo de todo lo que le escribamos por el chat.
def echo(bot, update):
    chatbot = ChatBot('Ron Obvious')
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    # Train the chatbot based on the spanish corpus
    trainer.train("chatterbot.corpus.spanish")
    trainer.train("chatterbot.corpus.spanish.greetings")
    trainer.train("chatterbot.corpus.spanish.conversations")
    trainer.train("chatterbot.corpus.spanish.trivia")

    # Get a response to an input statement
    respuesta=chatbot.get_response(update.message.text)
    print(respuesta)
    bot.send_message(chat_id=update.message.chat_id, text=respuesta.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
