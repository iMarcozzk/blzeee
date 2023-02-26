import requests
import json
import telebot


api = "6110475944:AAEKturKK1K4mrVhrwFK2u0sC_iNPy2RlY0"     #colocar seu token do bot
chat_id = "-1001840459062"                                  #colocar id do chat, para super grupo colocar -100 antes

bot = telebot.TeleBot(api)

bot.send_message(chat_id, text="robôzinho iniciado com sucesso <3")

    
analise_sinal = False
entrada = 0
max_gale = 1                  #escolher a quantidade de gale que o bot vai mandar

resultado = []
check_resultado = []

def reset():
    global analise_sinal
    global entrada
    
    entrada = 0
    analise_sinal = False
    return


def martingale():
    global entrada
    entrada += 1
    
    if entrada <= max_gale:
        bot.send_message(chat_id, text=f"⚠️atenção gale {entrada}⚠️")
    else:
        loss()
        reset()
    return


def api():
    global resultado
    req = requests.get('https://blaze.com/api/roulette_games/recent')
    a = json.loads(req.content)
    jogo = [x['roll'] for x in a]
    resultado = jogo
    return jogo

def win():
    bot.send_message(chat_id, text="✅")                          #para enviar esticker basta trocar para: bot.send_sticker(chat_id, sticker"colocar o id do sticker aqui")
    return 
def loss():
    bot.send_message(chat_id, text="❌")
    return
 
def correcao(results, color):
    if results[0:1] == ['PRETO'] and color == '⚫️':
        win()
        reset()
        return
    
    elif results[0:1] == ['VERMELHO'] and color == '🛑':
        win()
        reset()
        return
    
    elif results[0:1] == ['PRETO'] and color == '🛑':
        martingale()
        return
    
    elif results[0:1] == ['VERMELHO'] and color == '⚫️':
        martingale()
        return
    
    
    elif results[0:1] == ['BRANCO']:
        win()
        reset()

def enviar_sinal(cor, padrao, roll):          
    bot.send_message(chat_id, text=f'''
🚨sinal encontrado🚨

⏯️ Padrão: {padrao}

💶entrar no {cor}

⏯️ultima entrada > {roll}

🦾proteger no ⚪️

🐓1 martingale: (opcional)''')
    return


def estrategy(resultado):
    global analise_sinal
    global cor_sinal
    global cores
    global roll
    
    cores = []
    for x in resultado:
        if x >= 1 and x <= 7:
            color = 'VERMELHO'
            cores.append(color)
        elif x >= 8 and x <= 14:
            color = 'PRETO'
            cores.append(color)
        else:
            color = 'BRANCO'
            cores.append(color)
    print(cores)
    
    
    if analise_sinal == True:
        correcao(cores, cor_sinal)
    else:
        #aqui você coloca suas estratégias, para adicionar mais estratégia, é só copiar o if e colar em baixo na mesma linha, e modificar a estretegia e o nome do padrao
        if cores[0:4] == ['PRETO','VERMELHO','PRETO','VERMELHO']:
            cor_sinal = '🛑'
            padrao = '👻Ghost👻'
            roll = resultado[0]
            enviar_sinal(cor_sinal, padrao, roll)
            analise_sinal = True
            print('sinal enviado')
        
        if cores[0:3] == ['VERMELHO','PRETO','VERMELHO']:
            cor_sinal = '⚫️'
            padrao = '👑King👑'
            roll = resultado[0]
            enviar_sinal(cor_sinal, padrao, roll)
            analise_sinal = True
            print('sinal enviado')  
        
        if cores[0:2] == ['VERMELHO','PRETO']:
            cor_sinal = '⚫️'
            padrao = '🥷🏽Samurai🥷🏽'
            roll = resultado[0]
            enviar_sinal(cor_sinal, padrao, roll)
            analise_sinal = True
            print('sinal enviado') 

while True:
    api()
    if resultado != check_resultado:
        check_resultado = resultado
        #print(resultado)
        estrategy(resultado)


    
        
        
        
        
