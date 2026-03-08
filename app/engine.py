import random

CASA = 0.99

class AviatorEngine:

    def __init__(self, saldo):
        self.saldo = saldo

    def gerar_multiplicador(self):
        r = random.random()
        return CASA / r

    def rodada(self, aposta, cashout):

        if aposta > self.saldo:
            return {"erro": "Saldo insuficiente"}

        mult = self.gerar_multiplicador()

        self.saldo -= aposta

        ganhou = False

        if mult >= cashout:
            ganho = aposta * cashout
            self.saldo += ganho
            ganhou = True

        return {
            "multiplicador": round(mult, 2),
            "ganhou": ganhou,
            "saldo": round(self.saldo, 2)
        }