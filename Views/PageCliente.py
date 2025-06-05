import streamlit as st
import pandas as pd
import Controllers.ClienteController as clienteController
from Models.Cliente import Cliente

def show_cliente_page():
    st.title('📋Cadastro de Clientes')

    # Menu de operações para Cliente
    Page_Cliente = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    # Incluir cliente
    if Page_Cliente == "Incluir":
        st.subheader("➕ Incluir Novo Cliente")
        cliente = Cliente(0, "", "", "", "")

        cliente.set_cpf(st.text_input("CPF: "))
        cliente.set_nome(st.text_input("Nome: "))
        cliente.set_data_nascimento(st.date_input("Data de Nascimento: "))
        cliente.set_cidade(st.text_input("Cidade: "))
        cliente.set_telefone(st.text_input("Telefone: "))
        #Botão para inserir os dados
        if st.button("Inserir"):
            clienteController.incluirCliente(cliente)
            st.success("Cliente cadastrado com sucesso!")

    # Consultar cliente
    elif Page_Cliente == "Consultar":
        st.subheader("📋 Lista de Clientes")
        if st.button("Consultar"):
            dados = clienteController.consultarCliente()
            if dados:
                dado = pd.DataFrame(dados, columns=["CPF", "Nome", "DataNascimento", "Cidade", "Telefone"])
                st.dataframe(dado)
            else:
                st.info("Nenhum cliente cadastrado")

    # Excluir cliente
    elif Page_Cliente == "Excluir":
        st.subheader("❌ Excluir Cliente")
        dados = clienteController.consultarCliente()
        if dados:
            # st.table(pd.DataFrame(dados))
            codigo_cpf = st.text_input("CPF do cliente para excluir")
            
            if st.button("Excluir"):
                clienteController.excluirCliente(codigo_cpf)
                st.success("Cliente excluído com sucesso!")
        else:
            st.info("Nenhum cliente cadastrado")
    
    # Alterar cliente
    elif Page_Cliente == "Alterar":
        st.subheader("✏️ Alterar Cliente")
        dados = clienteController.consultarCliente()

        if dados:
            codigo_cpf = st.text_input("CPF do cliente para alterar")
            if st.button("Buscar"):
                cliente_data = next((c for c in dados if c["CPF"] == codigo_cpf), None)

                if cliente_data:
                    # Armazena o cliente selecionado para manter os dados após o clique no botão "Buscar"
                    st.session_state.cliente_selecionado = cliente_data
                else:
                    st.error("Cliente não encontrado")
                    st.session_state.cliente_selecionado = None
            # Busca o cliente selecionado no session_state, se existir
            cliente_data = st.session_state.get("cliente_selecionado", None)
        # Referente a alteração de dados
        if cliente_data:
            cliente = Cliente(
                cliente_data["CPF"],
                cliente_data["Nome"],
                cliente_data["DataNascimento"],
                cliente_data["Cidade"],
                cliente_data["Telefone"]
            )

            with st.form(key="alteraCliente"):
                cliente.set_cpf(st.text_input("CPF", value=cliente.get_cpf()))
                cliente.set_nome(st.text_input("Nome", value=cliente.get_nome()))
                cliente.set_data_nascimento(
                    st.date_input("Data de Nascimento", value=cliente.get_data_nascimento())
                )
                cliente.set_cidade(st.text_input("Cidade", value=cliente.get_cidade()))
                cliente.set_telefone(st.text_input("Telefone", value=cliente.get_telefone()))

                if st.form_submit_button("Confirmar Alterações"):
                    clienteController.alterarCliente({
                        "CPF": cliente.get_cpf(),
                        "Nome": cliente.get_nome(),
                        "DataNascimento": cliente.get_data_nascimento(),
                        "Cidade": cliente.get_cidade(),
                        "Telefone": cliente.get_telefone()
                    })
                    st.success("Cliente alterado com sucesso!")

                    # Limpa o estado após alteração
                    del st.session_state["cliente_selecionado"]

    else:
        st.info("Nenhum cliente cadastrado")

        