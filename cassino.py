import random
import time
import os

class CacaNiquel:
    def __init__(self):
        self.saldo = 1000
        self.simbolos = ["🍒", "🍋", "🔔", "⭐", "7️⃣", "🍉", "💎"]
        print("🎰 Bem-vindo ao Caça-Níquel Pythonico!")
        print(f"Você começa com R${self.saldo:.2f}\n")

    def limpar_tela(self):
        os.system("cls" if os.name == "nt" else "clear")

    def apostar(self):
        while True:
            try:
                valor = float(input("Quanto deseja apostar? R$"))
                if valor <= 0:
                    print("A aposta deve ser maior que zero.")
                elif valor > self.saldo:
                    print("Saldo insuficiente!")
                else:
                    return valor
            except ValueError:
                print("Digite um valor válido.")

    def girar_rolo(self):
        """Simula o giro dos símbolos com animação"""
        for _ in range(15):  # número de "frames" da rotação
            resultado_temp = [random.choice(self.simbolos) for _ in range(3)]
            print("\r | ".join(resultado_temp), end="", flush=True)
            time.sleep(0.1)
            self.limpar_tela()
        # Resultado final
        resultado = [random.choice(self.simbolos) for _ in range(3)]
        print("🎰 Resultado final:")
        print(" | ".join(resultado))
        return resultado

    def jogar(self):
        while True:
            print(f"\n💰 Saldo atual: R${self.saldo:.2f}")
            print("1. Jogar")
            print("2. Sair")
            opcao = input(">> ")

            if opcao == "1":
                aposta = self.apostar()
                self.limpar_tela()
                print("🎲 Girando os rolos...")
                time.sleep(0.5)

                resultado = self.girar_rolo()
                self.analisar_resultado(resultado, aposta)

            elif opcao == "2":
                print("Até a próxima! 👋")
                break
            else:
                print("Opção inválida!")

    def analisar_resultado(self, resultado, aposta):
        time.sleep(0.5)
        if len(set(resultado)) == 1:
            ganho = aposta * 10
            print(f"🎊 JACKPOT! Três iguais! Você ganhou R${ganho:.2f}!")
            self.saldo += ganho - aposta
        elif len(set(resultado)) == 2:
            ganho = aposta * 2
            print(f"✨ Dois iguais! Você ganhou R${ganho:.2f}!")
            self.saldo += ganho - aposta
        else:
            print("💀 Nenhuma combinação. Você perdeu.")
            self.saldo -= aposta


if __name__ == "__main__":
    jogo = CacaNiquel()
    jogo.jogar()
