import streamlit as st
import pandas as pd
import Controllers.QuartoController as quartoController
from Models.Quarto import Quarto

def show_quarto_page():
    st.title('Cadastro de Quartos')

    # Menu de operações para Quarto
    Page_Quarto = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    # Incluir Quarto
    if Page_Quarto == "Incluir":
        quarto = Quarto(0, "", "", "", "")

        quarto.set_num_quarto(st.number_input("Número do Quarto: "))
        quarto.set_descricao(st.text_input("Descrição: "))
        quarto.set_id_reserva(st.number_input(""))