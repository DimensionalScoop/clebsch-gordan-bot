import telegram
import logging
import telegram.ext as tex
from sympy.physics.quantum.cg import CG
import sympy
import numpy as np

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = tex.Updater('246042888:AAFmv3oelFG3gVnAYeFo5E7r1QAsJyTZsj0')
dispatcher = updater.dispatcher
bot = updater.bot

print("Started Bot:", bot.getMe())

# Handler functions


def start(bot, update):
    message = "Clebsch Gordan erwacht..."
    bot.sendMessage(chat_id=update.message.chat_id, text=message)


def help(bot, update):
    message = """Commands:
    /help: show this help page
    /start: starts clebschie
    /coeff j1 j2 J M: calculates c-g coefficient of |J M>
    /ee J M: calculates c-g coefficients for two electrons.main.py"""
    bot.sendMessage(chat_id=update.message.chat_id, text=message)


def cgCoefficients(bot, update, args):
    print(args)

    try:
        j1, j2, J, M = map(float, args)
        if j1 == int(j1):
            j1 = int(j1)
        if j2 == int(j2):
            j2 = int(j2)
        if J == int(J):
            J = int(J)
        if M == int(M):
            M = int(M)
    except Exception:
        answer = ":( Your parameters are inconceivable."
    else:
        answer = "|J=" + str(J) + ", M=" + str(M) + "> = \n"
        nCoeff = 0

        try:
            for m1 in np.arange(-j1, j1 + 1):
                for m2 in np.arange(-j2, j2 + 1):
                    print(m1, m2)
                    if m1 == int(m1):
                        m1 = int(m1)
                    if m2 == int(m2):
                        m2 = int(m2)
                    print(m1, m2)
                    coeff = CG(j1, m1, j2, m2, J, M).doit()
                    if coeff != 0:
                        if nCoeff > 0:
                            answer += " + "
                        else:
                            answer += "   "
                        answer += str(coeff) + "\t |" + str(m1) + ", " + str(m2) + ">\n"
                        nCoeff += 1
        except Exception:
            answer = ":("

    bot.sendMessage(chat_id=update.message.chat_id, text=answer)


def ee(bot, update, args):
    args = ['0.5', '0.5'] + args
    cgCoefficients(bot, update, args)

dispatcher.add_handler(tex.CommandHandler('start', start))
dispatcher.add_handler(tex.CommandHandler('help', help))
dispatcher.add_handler(tex.CommandHandler('coeff', cgCoefficients, pass_args=True))
dispatcher.add_handler(tex.CommandHandler('ee', ee, pass_args=True))

updater.start_polling()
