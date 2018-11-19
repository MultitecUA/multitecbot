# coding=utf-8
# MULTITECBOT creado por Esteban Escobar.
# Basado en la API de creación de bots en python. Para más información consultar su repositorio en github (https://github.com/python-telegram-bot/python-telegram-bot).
import webbrowser
import telegram
import logging
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler


TOKEN = '755869851:AAFBJEPnW5kyV8xmK-We-Pj7fGRam4XRP8o' # Asignamos a la variable TOKEN el hash de nuestro bot para facilitar su utilización más adelante.

AYUDA = 'Hola! soy el bot oficial de Multitec, me encargo de gestionar los grupos y el canal de la asociación, puedes utilizar los siguientes comandos : \n\n/comandos - Lista de comandos. \n/chiste - Que el bot te cuente un chiste \n/eventos - Informacion sobre Eventos \n/pagina web - Nuestra web \n/inscripcion - Link del formulario de inscripción\n/redes_sociales - Enlaces a las redes sociales de la Comunidad' # Mensaje de ayuda y bienvenida.

#COMANDOS
COMANDOS = '/comandos - lista de comandos. \n/chiste - Que el bot te cuente un chiste \n/eventos - Informacion sobre Eventos \n/pagina web - Nuestra web \n/inscripcion - Link del formulario de inscripción\n/redes_sociales - Enlaces a las redes sociales de la Comunidad'

#EVENTOS
EVENTOS = 'CALENDARIO DE EVENTOS\n\n📆 1 de diciembre hay Ludum Dare y ya se ha abierto el plazo para sugerir temas:https://ldjam.com/events/ludum-dare/43/theme\nLudum Dare is one of the worlds largest and longest running Game Jam events. Every 4 months, we challenge creators to make a game from scratch in a weekend\n\nTORREVIEJA\n-Nueva edición Hackea Tu Destino! https://www.eventbrite.es/e/entradas-hackea-tu-destino-2018-52450812793\nCentrada en la innovación en turismo y el desarrollo de aplicaciones y tecnologías que resuelvan problemas actuales y aporten nuevos puntos de vista relacionados con el ambito turístico.\n📆 ¿Cuándo? Del 24 de noviembre de 2018 a las 10:00h hasta el 25 de noviembre de 2018 a las 18:00h.'

#EVENTOS
REDES_SOCIALES = 'Página de Facebook: https://bit.ly/2A4jADu\n Página de instagram: https://www.instagram.com/multitecua'


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

# Con esto el bot hará echo de todo lo que le escribamos por el chat.
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
