import streamlit as st
import pandas as pd
import Controllers.QuartoController as quartoController
from Models.Quarto import Quarto

def show_quarto_page():
    st.title('📋Cadastro de Quartos')

    # Menu de operações para Quarto
    Page_Quarto = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    # Incluir Quarto
    if Page_Quarto == "Incluir":
        st.subheader("➕ Incluir Novo Quarto")
        quarto = Quarto(0, "")

        quarto.set_num_quarto(st.text_input("Número do Quarto: "))
        quarto.set_descricao(st.text_input("Descrição: "))
        #Botão para inserir os dados
        if st.button("Inserir"):
            quartoController.incluirQuarto(quarto)
            st.success("Quarto cadastrado com sucesso!")
    
    # Consultar Quarto
    elif Page_Quarto == "Consultar":
        st.subheader("📋 Lista de Quartos")

        dados = quartoController.consultarQuarto()
        if dados:
            dado = pd.DataFrame(dados, columns=["Num_Quarto", "Descricao"])
            st.dataframe(dado)
        else:
            st.info("Nenhum quarto cadastrado")

    # Excluir Quarto
    elif Page_Quarto == "Excluir":
        st.subheader("❌ Excluir Quartos")

        dados = quartoController.consultarQuarto()
        if dados:
            num_quarto = st.text_input("Número do Quarto para excluir")
            
            if st.button("Excluir"):
                quartoController.excluirQuarto(num_quarto)
                st.success("Quarto excluído com sucesso!")
        else:
            st.info("Nenhum Quarto cadastrado")
    
    # Alterar quarto
    elif Page_Quarto == "Alterar":
        st.subheader("✏️ Alterar Quarto")

        dados = quartoController.consultarQuarto()

        if dados:
            num_quarto = st.text_input("Número do quarto para alterar")

            if st.button("Buscar"):
                quarto_data = next((c for c in dados if str(c["Num_Quarto"]).strip() == str(num_quarto).strip()),None)

                if quarto_data:
                    # Armazena o quarto selecionado no session_state
                    st.session_state.quarto_selecionado = quarto_data
                else:
                    st.error("Quarto não encontrado")
                    st.session_state.quarto_selecionado = None

            # Recupera os dados do quarto selecionado armazenados no session_state.
            quarto_data = st.session_state.get("quarto_selecionado", None)
        # Se encontrou o quarto, exibe o formulário de alteração
        if quarto_data:
            quarto = Quarto(
                quarto_data["Num_Quarto"],
                quarto_data["Descricao"]
            )
            # Formulário para alterar os dados do quarto
            with st.form(key="alteraQuarto"):
                quarto.set_num_quarto(st.text_input("Num_Quarto", value=quarto.get_num_quarto()))
                quarto.set_descricao(st.text_input("Descricao", value=quarto.get_descricao()))

                if st.form_submit_button("Confirmar Alterações"):
                    quartoController.alterarQuarto({
                        "Num_Quarto": quarto.get_num_quarto(),
                        "Descricao": quarto.get_descricao(),
                    })
                    st.success("Quarto alterado com sucesso!")

                    # Limpa o session_state após alteração
                    del st.session_state.quarto_selecionado
    else:
        st.info("Nenhum quarto cadastrado")