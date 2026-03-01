#IMPORTAÇÕES:
import time
from datetime import datetime

#apresentação:
print('\33[34m--' * 8)
print('BANCO DO RICARDO')
print('--' * 8)


#CADASTRO:
print('\33[33mPara utilizar o Banco do Ricardo, faça seu cadastro primeiro (apenas para pessoas acima de 18 anos).\33[m')
time.sleep(0.3)

#nome de usuario
nome_usuario = str(input('Nome de usuário: ')).strip()
time.sleep(0.3)

#senha do usuario
senha = ' '
while len(senha) < 8:
    senha = str(input('Digite sua senha (a senha deve conter no mínimo 8 caracteres.): ')).strip()
    time.sleep(0.3)

#idade usuario/verificar idade
data_nascimento = str(input('Qual sua data de nascimento (dd-mm-aaaa)? ')).strip()
transforma_data = datetime.strptime(data_nascimento ,'%d-%m-%Y')
data_hoje = datetime.now()
idade_usuario = data_hoje.year - transforma_data.year
if (data_hoje.month, data_hoje.day) < (transforma_data.month, transforma_data.day):
    idade_usuario -= 1

if idade_usuario >= 18:
    print('\33[32mCadastro finalizado! Você ganhou um bônus de R$50.00 por fazer o cadastro!\33[m')
    time.sleep(0.8)
else:
    print('\33[31mOps! Você precisa ter pelo menos 18 anos para se cadastrar\33[m')
    exit()


#ENTRADA
print()
print('\33[36m---' * 11)
print('Bem-vindo(a) ao Banco do Ricardo!')
print('---' * 11)
print('\33[m[E] -> Entrar\n[S] -> Sair')

#entrar ou sair
escolha = ' '
while escolha not in 'ES':
    escolha = str(input('Qual a sua escolha [E/S]? ')).strip().upper()[0]
    if escolha == 'S':
        print('Saindo do programa...')
        exit()
        
        
#LOGIN
print()
print('\33[35m--' * 7)
print('ENTRAR (LOGIN):')
print('--' * 7)

#verificar nome e senha
contador = 0
while True:
    verificarNome = str(input('\33[mNome de usuário: ')).strip()
    verificarSenha = str(input('Senha: ')).strip()
    time.sleep(0.3)
    
    #nome e senha estão corretos?
    if verificarNome == nome_usuario and verificarSenha == senha:
        print('\33[32mLogin realizado com sucesso!\33[m')
        time.sleep(0.8)
        break
    else:
        print('\33[33mNome de usuário ou senha incorreto(s)!\33[m')
        time.sleep(0.3)
        contador += 1
        
    #já tentou 3 vezes e n entrou ainda?
    if contador == 3:
        print('\33[31mVocê excedeu o limite de 3 tentativas. Tente novamente mais tarde.\33[m')
        exit()
        

#MENU OPÇÕES
print()
print('\33[32m--' * 6)
print('MENU OPÇÕES:')
print('--' * 6)
    
saldo = 50
while True:
    print('\33[m[1] -> Sacar\n[2] -> Depositar\n[3] -> Ver saldo\n[4] -> Comprar algo\n[5] -> Sair')
    
    #usuario escolhe a opção
    opcao_menu = int(input('Qual opção você deseja escolher? '))
    
    #se escolher 1 (sacar)
    if opcao_menu == 1:
        print()
        print('\33[33mSACAR DINHEIRO\33[m')
        quanto_sacar = float(input(f'Quanto você quer sacar? Você tem R${saldo:.2f}: '))
        if quanto_sacar > saldo:
            print('\33[31mVocê não pode sacar mais do que tem!\33[m')
            print()
            
        elif quanto_sacar <= 0:
            print('\33[31mValor inválido! Digite um valor positivo maior que zero.\33[m')
            print()
            
        else:
            saldo -= quanto_sacar
            print(f'\33[33mVocê sacou R${quanto_sacar:.2f} e seu saldo agora é de R${saldo:.2f}\33[m')
            print()
    
    #se escolher 2 (depositar)
    if opcao_menu == 2:
        print()
        print('\33[33mDEPOSITAR DINHEIRO\33[m')
        quanto_depositar = float(input(f'Quanto você quer depositar? Seu saldo atual é de R${saldo:.2f}: '))
        
        if quanto_depositar <= 0:
            print('\33[31mValor inválido! Digite um valor positivo maior que zero.\33[m')
            print()
        else:
            saldo += quanto_depositar
            print(f'\33[33mVocê depositou R${quanto_depositar:.2f} e seu saldo agora é de R${saldo:.2f}\33[m')
            print()
            
    #se escolher 3 (ver saldo)
    if opcao_menu == 3:
        print()
        print('\33[33mSALDO\33[m')
        print(f'\33[34mSeu saldo: R${saldo:.2f}\33[m')
        print()
    
    #se escolher 4 (comprar algo)
    if opcao_menu == 4:
        print()
        print('\33[33mCOMPRAR ALGO\33[m')
        print(f'\33[34mSeu saldo: {saldo:.2f}\33[m')
        
        nome_produto = str(input('Nome do produto: ')).strip()
        valor_unitario = float(input('Valor produto (1 unidade): '))
        valor_quantidade = int(input('Quantidade do produto: '))
        
        if valor_unitario <= 0 or valor_quantidade <= 0:
            print('\33[33mValor inválido. A quantidade ou o preço do produto devem ser maior que zero.\33[m')
            print()
            continue
        
        valor_total = valor_unitario * valor_quantidade
        
        if saldo < valor_total:
            print('\33[31mVocê não tem dinheiro suficiente para efetuar essa compra.\33[m')
            
            
            resposta = ' '
            while resposta not in 'SN':
                resposta = str(input('Quer diminuir uma certa quantidade de produtos? [S/N]: ')).strip().upper()[0]
                
                if resposta ==  'S':
                    novo_valor_quantidade = int(input('Nova quantidade do(s) produto(s): '))
                    if novo_valor_quantidade <= 0:
                        print('\33[33mValor inválido. A quantidade ou o preço do produto deve ser maior que zero.\33[m')
                        continue
                    elif novo_valor_quantidade >= valor_quantidade:
                        print('\33[31mValor inválido. A quantidade informada não pode ser maior ou igual à quantidade original.\33[m')
                        print()
                        continue
                    
                    novo_valor_total = valor_unitario * novo_valor_quantidade
                    if saldo < novo_valor_total:
                        print('\33[31mInfelizmente você não pode efetuar essa compra.\33[m')
                        print()
                        break
                    else:
                        saldo -= novo_valor_total
                        print(f'\33[32mCompra realizada com sucesso! Sua compra foi de R${novo_valor_total:.2f} e seu saldo agora é de R${saldo:.2f}\33[m')
                        print()
                        break 
                
                else:
                    print('\33[33mCompra cancelada.\33[m')
                    print()
                    break
                        
        
        else:
            saldo -= valor_total
            print(f'\33[32mCompra realizada com sucesso! Sua compra foi de R${valor_total:.2f} e seu saldo agora é de R${saldo:.2f}\33[m')
            print()
    
    #se escolher 5 (sair)
    if opcao_menu == 5:
        print('\33[34mSaindo da conta...\33[m')
        break