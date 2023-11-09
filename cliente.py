# Função para receber mensagens
def receber_mensagens():
    while executando:
        try:
            # Recebe os dados e o endereço do remetente
            dados, endereco = socket_server.recvfrom(tamanho_maximo)  # Tamanho do buffer é 1024 bytes

            mensagem = dados.decode('utf-8')
            if mensagem.startswith(".entrar "):
                nome = mensagem[8:]  # Extrai o nome da mensagem
                participantes.append((nome, endereco[0]))  # Adiciona o par (nome, IP) à lista
                print(nome + " adicionado na lista.")
                lista_contatos = "\n".join([f"{nome},{ip}" for nome, ip in participantes])
                print(lista_contatos)
            elif mensagem.startswith(".sair "):
                nome = mensagem[6:]  # Extrai o nome da mensagem
                remover_participante(nome)
            elif mensagem == ".contatos":
                responder_contatos(endereco)
            elif mensagem == ".parar":
                print("Encerrando o servidor...")
                # Notifica os clientes antes de encerrar
                for participante in participantes:
                    socket_server.sendto("O servidor está sendo encerrado. Adeus!".encode('utf-8'), (participante[1], porta))
                executando = False
            else:
                # Mensagem desconhecida
                print(f"Mensagem desconhecida recebida de {endereco[0]}:{endereco[1]}: {mensagem}")

        except UnicodeDecodeError:
            print(f"Recebido de {endereco[0]}:{endereco[1]}: Erro de decodificação (não UTF-8)")
        except Exception as e:
            print(f"Erro ao processar a mensagem: {str(e)}")

# ...
