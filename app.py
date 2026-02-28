import streamlit as st

# Configuração da página
st.set_page_config(page_title="Meu Currículo", page_icon="📊")

# Cabeçalho
st.title("João Silva") # Troque pelo seu nome
st.subheader("Aspirante a Cientista de Dados | Aluno Indicium Academy")

# Contatos
st.write("📍 Cidade/Estado | [LinkedIn](seu-link) | [GitHub](seu-link)")

st.divider()

# Sobre Mim
st.header("Sobre Mim")
st.write("""
Estou em transição de carreira para a área de dados, focado em lógica de programação e Python.
Atualmente estudo na Indicium Academy para dominar ferramentas como SQL, dbt e Engenharia de Dados.
""")

# Habilidades Técnicas
st.header("Habilidades")
st.code("Python, Pandas, SQL, Streamlit, Git, Debian Linux")

st.info("Dica: Use 'st.write()' para textos e 'st.header()' para títulos!")
