import streamlit as st
import pandas as pd
import Controllers.ServicoController as servicoController
import Controllers.FuncionarioController as funcionarioController
import Controllers.ClienteController as clienteController
import Controllers.QuartoController as quartoController
from Models.Servico import Servico

def show_servico_page():
    st.title('🧾 Cadastro de Serviços')

    operacao = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if operacao == "Incluir":
        st.subheader("➕ Incluir Novo Serviço")
        col1, col2 = st.columns(2)
        with col1:
            id_funcionario = st.text_input("ID do Funcionário (CPF):")
            id_cliente = st.text_input("ID do Cliente (CPF):")
            id_quarto = st.text_input("ID do Quarto (Nº):")
        with col2:
            descricao = st.text_area("Descrição do Serviço:")

        if st.button("Salvar"):
            if not id_funcionario.strip():
                st.warning("O ID do funcionário é obrigatório.")
            elif not id_cliente.strip():
                st.warning("O ID do cliente é obrigatório.")
            elif not id_quarto.strip():
                st.warning("O ID do quarto é obrigatório.")
            elif descricao.strip() == "":
                st.warning("A descrição não pode estar vazia.")
            else:
                funcionario_existe = funcionarioController.buscarFuncionarioCpf(id_funcionario)
                cliente_existe = clienteController.buscarClienteCpf(id_cliente)
                quarto_existe = quartoController.buscarQuartoNum(id_quarto)

                if not funcionario_existe:
                    st.error("Funcionário não cadastrado no sistema.")
                elif not cliente_existe:
                    st.error("Cliente não cadastrado no sistema.")
                elif not quarto_existe:
                    st.error("Quarto não cadastrado no sistema.")
                else:
                    servico = Servico(None, id_funcionario, descricao, id_cliente, id_quarto)
                    servicoController.incluirServico(servico)
                    st.success("Serviço cadastrado com sucesso!")

    elif operacao == "Consultar":
        st.subheader("📋 Lista de Serviços")
        servicos = servicoController.consultarServicos()
        if servicos:
            data = [{
                "ID": s.get_id() or "",
                "ID Funcionário": s.get_id_funcionario() or "",
                "Descrição": s.get_descricao() or "",
                "ID Cliente": s.get_id_cliente() or "",
                "ID Quarto": s.get_id_quarto() or ""
            } for s in servicos]
            df = pd.DataFrame(data)
            st.dataframe(df)
        else:
            st.info("Nenhum serviço cadastrado.")

    elif operacao == "Excluir":
        st.subheader("❌ Excluir Serviço")
        servicos = servicoController.consultarServicos()
        if servicos:
            opcoes = {s.get_id(): f"Funcionário: {s.get_id_funcionario()} - Quarto: {s.get_id_quarto()}" for s in servicos}
            id_excluir = st.selectbox("Selecione o serviço a excluir:", options=list(opcoes.keys()),
                                      format_func=lambda x: f"ID {x} - {opcoes[x]}")
            if st.button("Excluir"):
                sucesso = servicoController.excluirServico(id_excluir)
                if sucesso:
                    st.success(f"Serviço com ID {id_excluir} excluído com sucesso!")
                else:
                    st.error("Erro ao excluir o serviço.")
        else:
            st.info("Nenhum serviço cadastrado para excluir.")

    elif operacao == "Alterar":
        st.subheader("✏ Alterar Serviço")
        servicos = servicoController.consultarServicos()
        if servicos:
            opcoes = {s.get_id(): f"Funcionário: {s.get_id_funcionario()} - Quarto: {s.get_id_quarto()}" for s in servicos}
            id_alterar = st.selectbox("Selecione o serviço para alterar:", options=list(opcoes.keys()),
                                      format_func=lambda x: f"ID {x} - {opcoes[x]}")
            servico_selecionado = next((s for s in servicos if s.get_id() == id_alterar), None)

            if servico_selecionado:
                novo_id_funcionario = st.text_input("Novo ID Funcionário (CPF):", value=servico_selecionado.get_id_funcionario())
                nova_descricao = st.text_area("Nova Descrição:", value=servico_selecionado.get_descricao())
                novo_id_cliente = st.text_input("Novo ID Cliente (CPF):", value=servico_selecionado.get_id_cliente())
                novo_id_quarto = st.text_input("Novo ID Quarto (Nº):", value=servico_selecionado.get_id_quarto())

                if st.button("Atualizar"):
                    if not novo_id_funcionario.strip():
                        st.warning("O ID do funcionário é obrigatório.")
                    elif not nova_descricao.strip():
                        st.warning("A descrição não pode estar vazia.")
                    elif not novo_id_cliente.strip():
                        st.warning("O ID do cliente é obrigatório.")
                    elif not novo_id_quarto.strip():
                        st.warning("O ID do quarto é obrigatório.")
                    else:
                        funcionario_existe = funcionarioController.buscarFuncionarioCpf(novo_id_funcionario)
                        cliente_existe = clienteController.buscarClienteCpf(novo_id_cliente)
                        quarto_existe = quartoController.buscarQuartoNum(novo_id_quarto)

                        if not funcionario_existe:
                            st.error("Funcionário não cadastrado.")
                        elif not cliente_existe:
                            st.error("Cliente não cadastrado.")
                        elif not quarto_existe:
                            st.error("Quarto não cadastrado.")
                        else:
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
