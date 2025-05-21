import streamlit as st
import pandas as pd
import Controllers.FuncionarioController as funcionarioController
from Models.Funcionario import Funcionario
from datetime import date

def show_funcionario_page():
    st.title('📋 Cadastro de Funcionários')

    operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if operacao == "Incluir":
        st.subheader("➕ Incluir Novo Funcionário")
        col1, col2 = st.columns(2)
        with col1:
            cpf = st.number_input("CPF:", min_value=0, step=1, format="%d")
            nome = st.text_input("Nome:")
            telefone = st.text_input("Telefone:")
        with col2:
            data_nascimento = st.date_input("Data de Nascimento:")
            data_cadastro = st.date_input("Data de Cadastro:", value=date.today())

        if st.button("Salvar"):
            if not nome.strip():
                st.warning("Nome não pode estar vazio.")
            else:
                funcionario = Funcionario(cpf, nome, telefone, str(data_nascimento), str(data_cadastro))
                funcionarioController.incluirFuncionario(funcionario)
                st.success("Funcionário cadastrado com sucesso!")

    elif operacao == "Consultar":
        st.subheader("📋 Lista de Funcionários")
        funcionarios = funcionarioController.consultarFuncionarios()
        if funcionarios:
            data = []
            for func in funcionarios:
                data.append({
                    "CPF": func.get_cpf(),
                    "Nome": func.get_nome(),
                    "Telefone": func.get_telefone(),  # Corrigido
                    "Data Nascimento": func.get_data_nascimento(),
                    "Data Cadastro": func.get_data_cadastro()
                })
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("Nenhum funcionário cadastrado.")

    elif operacao == "Excluir":
        st.subheader("❌ Excluir Funcionário")
        cpf_excluir = st.number_input("CPF do funcionário a excluir:", min_value=0, step=1, format="%d")
        if st.button("Excluir"):
            funcionarioController.excluirFuncionario(cpf_excluir)
            st.success(f"Funcionário com CPF {cpf_excluir} excluído!")

    elif operacao == "Alterar":
        st.subheader("✏️ Alterar Funcionário")
        funcionarios = funcionarioController.consultarFuncionarios()
        if funcionarios:
            opcoes = {func.get_cpf(): func.get_nome() for func in funcionarios}
            codigo_alterar = st.selectbox("Selecione o funcionário:", options=list(opcoes.keys()),
                                          format_func=lambda x: f"{x} - {opcoes[x]}")
            funcionario_selecionado = next((f for f in funcionarios if f.get_cpf() == codigo_alterar), None)

            if funcionario_selecionado:
                novo_nome = st.text_input("Novo Nome:", value=funcionario_selecionado.get_nome())
                novo_telefone = st.text_input("Novo Telefone:", value=funcionario_selecionado.get_telefone())
                nova_data_nascimento = st.date_input("Nova Data de Nascimento:", value=pd.to_datetime(funcionario_selecionado.get_data_nascimento()))
                nova_data_cadastro = st.date_input("Nova Data de Cadastro:", value=pd.to_datetime(funcionario_selecionado.get_data_cadastro()))

                if st.button("Atualizar"):
                    funcionario_atualizado = Funcionario(
                        codigo_alterar, novo_nome, novo_telefone,
                        str(nova_data_nascimento), str(nova_data_cadastro)
                    )
                    funcionarioController.alterarFuncionario(funcionario_atualizado)
                    st.success(f"Funcionário {novo_nome} atualizado com sucesso!")
        else:
            st.info("Nenhum funcionário cadastrado para alterar.")
