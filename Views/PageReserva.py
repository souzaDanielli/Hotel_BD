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
                st.info("Nenhuma Reserva cadastrada")
        # Consulta com WHERE - Procura todas as reservas do Cliente com CPF
        elif opcao_consulta == "Reservas por Cliente":
            cpf = st.text_input("Digite o CPF do Cliente")

            if st.button("Inserir"):
                dados = reservaController.buscarReservasPorCpf(cpf)
                if dados:
                    st.table(pd.DataFrame(dados))
                else:
                    st.warning(f"Nenhuma Reserva encontrada nesse CPF {cpf}")
        # Consulta com INNERJOIN - Junta todos os dados de cliente + quarto com as reservas
        elif opcao_consulta == "Reservas Detalhadas":
            dados =  reservaController.buscarReservasCompletas()
            if dados:
                dado = pd.DataFrame(dados)
                st.dataframe(dado)
            else:
                st.info("Nenhuma Reserva cadastrada")

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

    elif Page_Reserva == "Alterar":
        st.subheader("✏️ Alterar Reserva")

        dados = reservaController.consultarReserva()
        reserva_dados = None

        if dados:
            id = st.text_input("ID da Reserva para alterar")

            if st.button("Buscar"):
                # Procura a reserva pelo ID informado
                reserva_dados = next((c for c in dados if str(c["ID"]).strip() == str(id).strip()),None)

                if reserva_dados:
                    st.session_state.reserva_selecionada = reserva_dados
                else:
                    st.error("Reserva não encontrada")
                    st.session_state.reserva_selecionada = None
            # Recupera os dados armazenados no session_state, se houver
            reserva_dados = st.session_state.get("reserva_selecionada", None)
            # Se encontrou a reserva, exibe o formulário de alteração
            if reserva_dados:
                data_entrada = datetime.strptime(reserva_dados["Data_Entrada"], "%Y-%m-%d").date()
                data_saida = datetime.strptime(reserva_dados["Data_Saida"], "%Y-%m-%d").date()

                reserva = Reserva(
                    reserva_dados["ID"],
                    data_entrada,
                    data_saida,
                    reserva_dados["CPF_Cliente"],
                    reserva_dados["Num_Quarto"]
                )
                # Formulário para alterar os dados da reserva
                with st.form(key="alteraReserva"):
                    reserva.set_cpf_cliente(st.text_input("CPF do Cliente", value=reserva.get_cpf_cliente()))
                    reserva.set_data_entrada(st.date_input("Data de Entrada", value=reserva.get_data_entrada()))
                    reserva.set_data_saida(st.date_input("Data de Saída", value=reserva.get_data_saida()))
                    reserva.set_num_quarto(st.text_input("Número do Quarto", value=reserva.get_num_quarto()))

                    if st.form_submit_button("Confirmar Alterações"):
                        # Verifica se cliente e quarto existem
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

                        # Faz a alteração
                        reservaController.alterarReserva({
                            "id": reserva.get_id(),
                            "cpf_cliente": reserva.get_cpf_cliente(),
                            "data_entrada": reserva.get_data_entrada(),
                            "data_saida": reserva.get_data_saida(),
                            "num_quarto": reserva.get_num_quarto()
                        })
                        st.success("Reserva alterada com sucesso!")

                        # Limpa o session_state após a alteração
                        del st.session_state.reserva_selecionada
        else:
            st.info("Nenhuma reserva cadastrada")