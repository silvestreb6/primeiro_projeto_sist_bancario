menu = """

[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> """



saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
continuar = True

while continuar:
    
    opcao = input(menu)

    if opcao == "d":


        acao_deposito = True

        while acao_deposito == True:

            try:
                insira_valor_deposito = "Insira o valor do depósito: "
                valor_deposito = float(input(insira_valor_deposito))

                acao_inserir_valor = True

                while acao_inserir_valor == True:
                
                    if valor_deposito > 0:

                        menu_confirmar_deposito = f'''

                        ================= Confirmação =================

                        Deseja confirmar o depósito de R${valor_deposito:.2f}?

                        [Confirmar] = confirmar valor do depósito
                        [Alterar] = corrigir valor do depósito
                        [Menu Principal] = retornar ao Menu Principal
                        [Sair] = Encerrar sessão

                        ===============================================
                        '''

                        confirmacao_final_deposito = input(menu_confirmar_deposito)

                        if confirmacao_final_deposito == "Confirmar":

                            saldo += float(valor_deposito)

                            extrato += f'''

                            ===================================

                            Depósito de R${valor_deposito}

                            Saldo atualizado: R${saldo}

                            ===================================
                            '''

                            menu_deposito_realizado_com_sucesso = (f'''
                          
                            ====================================
                          
                            Depósito realizado com sucesso!
                            Seu saldo atualizado é de: R${saldo: .2f}

                            [Menu Principal]
                            [Encerrar Sessão]      

                            ====================================
                            ''')

                            opcao_menu_deposito_realizado_com_sucesso = input(menu_deposito_realizado_com_sucesso)

                            if opcao_menu_deposito_realizado_com_sucesso == 'Menu Principal':

                                acao_deposito = False
                                break
                    
                            else:
                                print("Sessão encerrada.")

                                continuar = False
                                acao_deposito = False
                                break
            
                        elif confirmacao_final_deposito == "Alterar":

                            break
                
                        elif confirmacao_final_deposito == "Menu Principal":
            
                            acao_deposito = False

                            break
            
                        else:
                            print("Sessão encerrada.")

                            continuar = False
                            acao_deposito = False
                            break



                    else:
                        menu_revisar_deposito = '''
                        ==============================================================

                        É necessário inserir um valor válido para realizar o depósito. 
                        Deseja inserir um novo valor?

                        [Sim] = Inserir novo valor
                        [Não] = Encerrar sessão
                        [Menu Principal] = Menu Principal

                        ==============================================================
                        '''
                
                        opcao_continuar_deposito = input(menu_revisar_deposito)

                        if opcao_continuar_deposito == "Sim":

                            acao_inserir_valor = False

                        elif opcao_continuar_deposito == "Menu Principal":

                            continuar_deposito = False

             
                        else:
                            print("Sessão encerrada.")

                            continuar = False
                            acao_deposito = False
                            break

            except ValueError:

                print("Por favor, insira um valor válido.")

       


    elif opcao == "s":

        acao_saque = True

        while acao_saque == True:
            
            if numero_saques <= LIMITE_SAQUES:
                
                try:

                    menu_solicitacao_valor_saque = f'''

                    =====================================

                    Seu saldo atual é de R${saldo: .2f}.

                    Qual valor deseja sacar?
                    R$ '''

                    valor_saque = float(input(menu_solicitacao_valor_saque)) > 0


                    if (valor_saque <= saldo) and (valor_saque <= limite):
                    

                        ########## Saque viável: saldo suficiente ##########


                        menu_confirmacao_valor_saque = f'''

                        =================================

                        Seu saldo após o saque será de R${saldo - float(valor_saque)}.

                        Confirma o saque de R${valor_saque}?

                        [Confirma]
                        [Alterar]
                        [Retornar ao Menu Principal]
                        [Encerrar Sessão]

                        =================================

                        '''
                        confirmacao_saque = input(menu_confirmacao_valor_saque)

                        if confirmacao_saque == 'Confirma':
                        
                            saldo -= valor_saque

                            numero_saques += 1

                            extrato += f'''

                            ===================================
                            
                            Depósito de R${valor_saque: .2f}

                            Saldo atualizado: R${saldo : .2f}                                  

                            ===================================

                            '''
                            
                            # Fatiamento se Strings f-string {saldo : .2f} garante que o saldo contenha, no máximo, 2 casas decimais.


                            menu_final_saque = ('''   
                                            
                            ============================= 
                                                           
                            Saque realizado com Sucesso!                                                       
                            
                            [Retornar ao Menu Principal]
                            [Encerrar Sessão]
                          
                            =============================
                                            
                            ''')
                        
                            decisao_final_usuario_saque = input(menu_final_saque)


                            ######### Saque realizado com Sucesso ###########


                            if decisao_final_usuario_saque == "Retornar ao Menu Principal":

                                acao_saque = False
                                break

                            else:
                                print('Sessão Encerrada.')
                                continuar = False
                                break

                        elif confirmacao_saque == 'Alterar':
                            print()

                        elif confirmacao_saque == 'Retornar ao Menu Principal':

                            acao_saque = False
                            break

                        else:
                            print('Sessão Encerrada.')

                            continuar = False
                            acao_saque = False
                            break




                    elif valor_saque > limite:

                        menu_valor_saque_excedido = '''
                        ================================

                        Valor máximo de saque excedido.

                        Deseja inserir um novo valor?

                        [Sim]
                        [Retornar ao Menu Principal]
                        [Encerrar Sessão]

                        ================================
                        '''

                        opcao_menu_saque_valor_excedido = input(menu_valor_saque_excedido)
                    
                        if opcao_menu_saque_valor_excedido == 'Sim':

                            print()

                        elif opcao_menu_saque_valor_excedido == 'Retornar ao Menu Principal':

                            break

                        else:
                            print('Sessão encerrada.')

                            continuar = False
                            break


                    else:                                                                                 #Saque mal sucedido: saldo insuficiente
                        menu_saque_saldo_insuficiente = '''
                    
                        ============================
                        Saldo Insuficiente        

                        Deseja inserir novo Valor?

                        [Sim]
                        [Retornar Menu Principal]
                        [Encerrar Sesssão]

                        ============================
                        '''
                        opcao_saldo_insuficiente = input(menu_saque_saldo_insuficiente)

                        if opcao_saldo_insuficiente == 'Sim':
                            print()

                        elif opcao_saldo_insuficiente == 'Menu Principal':
                            break

                        else:
                            print('Sessão Encerrada')

                            continuar = False
                            break

                except ValueError:
                    print('O valor do saque deve ser um valor maior que R$ 0.00. Insira um valor válido')

            

            else:
                menu_quantidade_saques_excedida = '''

                =====================================

                Quantidade semanal de saques excedida.

                [Menu Principal]
                [Encerrar Sessão]

                =====================================

                '''

                opcao_menu_quantidade_saques_excedida = input(menu_quantidade_saques_excedida)

                if opcao_menu_quantidade_saques_excedida == 'Menu Principal':
                    break

                else:
                    print("Sessão Encerrada.")

                    continuar = False
                    break



    elif opcao == "e":
        print('============== Extrato ===============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'''
        Saldo atualizado: R${saldo: .2f}

        =========== Fim do Extrato ===========
        ''')      
        
        # Strings vazias carregam valor booleano False

        #    a primeira parte > if not extrato > ele pergunta se o extrato está vazio. Se estiver vazio, esse primeiro extrato será entendido como False
        #       dessa forma, o not na frente agiria transformando esse False em um True. Essa mudança faria com que o if seja acionado e a mensagem 
        #       'Não foram realizadas movimentações.' apareça.

        # Caso contrário, se o extrato tiver informação, ele carregará um valor booleano True. 
        #    dessa forma, o not na frente agiria transformando esse True em um False. Essa mudança faria com que o if seja ignorado e o else acionado.
        #    o else imprimirá o valor de extrato e esconderá a mensagem 'Não foram realizadas movimentações.'.




    elif opcao == "q":
        print('''
              
              ========== Sessão encerrada ============

               Obrigada por utilizar nossos serviços!
              
              ========================================

              ''')

        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
