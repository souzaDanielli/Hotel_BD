import streamlit as st
import sys
from pathlib import Path
import importlib

st.set_page_config(page_title= "Sistema de Hotel", layout="wide", initial_sidebar_state="auto")
sys.path.append(str(Path(__file__).parent))

PAGES = {
    "Cliente": "Views.PageCliente",
    "Quarto": "Views.PageQuarto",
    "Reserva": "Views.PageReserva",
    "Funcionário": "Views.PageFuncionario",
    "Serviço": "Views.PageServico"
}

def remove_acentos(text):
    replacements = {
        "á": "a",
        "à": "a",
        "ã": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ç": "c",
        " ": "_"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def load_page(page_name):
    try:
        module = importlib.import_module(PAGES[page_name])
        page_name_clean = remove_acentos(page_name.lower())
        return getattr(module, f"show_{page_name_clean}_page")
    except (ImportError, AttributeError, KeyError) as e:
        st.error(f"Erro ao carregar a página {page_name}: {e}")
        st.warning("Entre em contato com o administrador do sistema.")
        return None

def main():
    st.title('Sistema de Hotel')
    with st.sidebar:
        st.title("Menu")
        page_selection = st.selectbox("Selecione uma opção", list(PAGES.keys()))
    show_page = load_page(page_selection)
    if show_page:
        show_page()

if __name__ == "__main__":
    main()
