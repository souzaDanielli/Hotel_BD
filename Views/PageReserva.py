import streamlit as st
import pandas as pd
from datetime import datetime

import Controllers.ReservaController as reservaController
from Models.Reserva import Reserva

import Controllers.ClienteController as clienteController
import Controllers.QuartoController as quartoController

def show_reserva_page():
    st.title('📋 Cadastro de Reservas')

    # Menu de operações para Reserva
    Page_Reserva = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    # Incluir Reserva
    if Page_Reserva == "Incluir":
        st.subheader("➕ Incluir Nova Reserva")
        reserva = Reserva(0, "", "", "", "")

        reserva.set_data_entrada(st.date_input("Data de Entrada: "))
        reserva.set_data_saida(st.date_input("Data de Saída: "))
        reserva.set_cpf_cliente(st.text_input("CPF do Cliente: "))
        reserva.set_num_quarto(st.text_input("Número do Quarto: "))
        #Botão para inserir os dados
        if st.button("Inserir"):
            #Verificação se existe o cliente/quarto antes de inserir a reserva
            existe_cliente = clienteController.buscarClienteCpf(reserva.get_cpf_cliente())
            existe_quarto = quartoController.buscarQuartoNum(reserva.get_num_quarto())
            if not existe_cliente:
                st.error("Cliente não existe. Cadastre o cliente antes!")
            if not existe_quarto:
                st.error("Quarto não existe. Cadastre o quarto antes!")
            else:
                reservaController.incluirReserva(reserva)
                st.success("Reserva cadastrada com sucesso!")   
    
    # Consultar Reserva
    elif Page_Reserva == "Consultar":
        st.subheader("📋 Lista de Reservas")
        opcao_consulta = st.sidebar.selectbox("Escolha o tipo de consulta:", ["Listagem Simples","Reservas por Cliente","Reservas Detalhadas"])
        # Consulta com SELECT
        if opcao_consulta == "Listagem Simples":
            dados = reservaController.consultarReserva()
            if dados:
                dado = pd.DataFrame(dados)
                st.dataframe(dado)
            else:
                st.info("Nenhuma Reserva cadastrado")
        # Consulta com WHERE - Procura todas as reservas do Cliente com CPF
        elif opcao_consulta == "Reservas por Cliente":
            cpf = st.text_input("Digite o CPF do Cliente")
            if st.button("Inserir"):
                dados = reservaController.consultarReservaPorCliente(cpf)
                if dados:
                    st.table(pd.DataFrame(dados))
                else:
                    st.warning(f"Nenhuma Reserva encontrada nesse CPF {cpf}")
        # Consulta com INNERJOIN - Junta todos os dados de cliente + quarto com as reservas
        # elif opcao_consulta == "Reservas Detalhadas":
        #     dados = 

    # Excluir Reserva
    elif Page_Reserva == "Excluir":
        st.subheader("❌ Excluir Reserva")
        dados = reservaController.consultarReserva()
        if dados:
            id_para_excluir = st.text_input("ID da reserva para excluir")
            if st.button("Excluir"):
                reservaController.excluirReserva(id_para_excluir)
                st.success("Reserva excluída com sucesso!")
        else:
            st.info("Nenhuma reserva cadastrada")

    # Alterar reserva
    elif Page_Reserva == "Alterar":
        st.subheader("✏️ Alterar Reserva")
        dados = reservaController.consultarReserva()
        if dados:
            st.table(pd.DataFrame(dados))
            id = st.text_input("ID da Reserva para alterar")
            reserva_data = next((c for c in dados if str(c["ID"]).strip() == str(id).strip()), None)
            
            if reserva_data:
                data_entrada = datetime.strptime(reserva_data["Data_Entrada"], "%Y-%m-%d").date()
                data_saida = datetime.strptime(reserva_data["Data_Saida"], "%Y-%m-%d").date()

                reserva = Reserva(
                    reserva_data["ID"],
                    data_entrada,
                    data_saida,
                    reserva_data["CPF_Cliente"],
                    reserva_data["Num_Quarto"]
                    
                )
                #Alterando a reserva
                with st.form(key="alteraReserva"):
                    reserva.set_cpf_cliente(st.text_input("cpf_cliente", value=reserva.get_cpf_cliente()))
                    reserva.set_data_entrada(st.date_input("data_entrada", value=reserva.get_data_entrada()))
                    reserva.set_data_saida(st.date_input("data_saida", value=reserva.get_data_saida()))
                    reserva.set_num_quarto(st.text_input("num_quarto", value=reserva.get_num_quarto()))
                #Confirmando alterações (mostrando o que foi inserido anteriormente)
                    if st.form_submit_button("Confirmar Alterações"):
                        #Verificação se existe o cliente/quarto antes de inserir a reserva
                        existe_cliente = clienteController.buscarClienteCpf(reserva.get_cpf_cliente())
                        existe_quarto = quartoController.buscarQuartoNum(reserva.get_num_quarto())

                        if not existe_cliente and not existe_quarto:
                            st.error("Cliente e Quarto não existem. Cadastre antes!")
                            return
                        if not existe_cliente:
                            st.error("Cliente não existe. Cadastre o cliente antes!")
                            return
                        if not existe_quarto:
                            st.error("Quarto não existe. Cadastre o quarto antes!")
                            return
                        else:
                            reservaController.alterarReserva({
                                "id": reserva.get_id(),
                                "cpf_cliente": reserva.get_cpf_cliente(),
                                "data_entrada": reserva.get_data_entrada(),
                                "data_saida": reserva.get_data_saida(),
                                "num_quarto": reserva.get_num_quarto()
                            })
                            st.success("Reserva alterada com sucesso!")
            else:
                st.error("Reserva não encontrada")
        else:
            st.info("Nenhuma reserva cadastrada")