import streamlit as st
import pandas as pd
import Controllers.ServicoController as servicoController
from Models.Servico import Servico

def show_servico_page():
    st.title('🧾 Cadastro de Serviços')

    operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if operacao == "Incluir":
        st.subheader("➕ Incluir Novo Serviço")
        col1, col2 = st.columns(2)
        with col1:
            id = st.number_input("ID do Serviço:", min_value=0, step=1)
            id_funcionario = st.number_input("ID do Funcionário (CPF):", min_value=0)
            id_cliente = st.number_input("ID do Cliente (CPF):", min_value=0)
            id_quarto = st.number_input("ID do Quarto (Nº):", min_value=0)
        with col2:
            descricao = st.text_area("Descrição do Serviço:")

        if st.button("Salvar"):
            if descricao.strip() == "":
                st.warning("A descrição não pode estar vazia.")
            else:
                servico = Servico(id, id_funcionario, descricao, id_cliente, id_quarto)
                servicoController.incluirServico(servico)
                st.success("Serviço cadastrado com sucesso!")

    elif operacao == "Consultar":
        st.subheader("📋 Lista de Serviços")
        servicos = servicoController.consultarServicos()
        if servicos:
            data = [{
                "ID": s.get_id(),
                "ID Funcionário": s.get_id_funcionario(),
                "Descrição": s.get_descricao(),
                "ID Cliente": s.get_id_cliente(),
                "ID Quarto": s.get_id_quarto()
            } for s in servicos]
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("Nenhum serviço cadastrado.")

    elif operacao == "Excluir":
        st.subheader("❌ Excluir Serviço")
        id_excluir = st.number_input("ID do serviço a excluir:", min_value=0, step=1)
        if st.button("Excluir"):
            servicoController.excluirServico(id_excluir)
            st.success(f"Serviço com ID {id_excluir} excluído com sucesso!")

    elif operacao == "Alterar":
        st.subheader("✏️ Alterar Serviço")
        servicos = servicoController.consultarServicos()
        if servicos:
            opcoes = {s.get_id(): f"Funcionário: {s.get_id_funcionario()} - Quarto: {s.get_id_quarto()}" for s in servicos}
            id_alterar = st.selectbox("Selecione o serviço para alterar:", options=list(opcoes.keys()),
                                      format_func=lambda x: f"ID {x} - {opcoes[x]}")
            servico_selecionado = next((s for s in servicos if s.get_id() == id_alterar), None)

            if servico_selecionado:
                novo_id_funcionario = st.number_input("Novo ID Funcionário (CPF):", value=servico_selecionado.get_id_funcionario())
                nova_descricao = st.text_area("Nova Descrição:", value=servico_selecionado.get_descricao())
                novo_id_cliente = st.number_input("Novo ID Cliente (CPF):", value=servico_selecionado.get_id_cliente())
                novo_id_quarto = st.number_input("Novo ID Quarto (Nº):", value=servico_selecionado.get_id_quarto())

                if st.button("Atualizar"):
                    servico_atualizado = Servico(
                        servico_selecionado.get_id(),
                        novo_id_funcionario,
                        nova_descricao,
                        novo_id_cliente,
                        novo_id_quarto
                    )
                    servicoController.alterarServico(servico_atualizado)
                    st.success(f"Serviço com ID {servico_selecionado.get_id()} atualizado com sucesso!")
        else:
            st.info("Nenhum serviço cadastrado para alterar.")
