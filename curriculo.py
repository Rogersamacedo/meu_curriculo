import streamlit as st

# Configuração da página
st.set_page_config(page_title="Currículo - Rogério Sá de Macedo", page_icon="📄")

# --- CABEÇALHO ---
st.title("Rogério Sá de Macedo")
col1, col2 = st.columns(2)

with col1:
    st.markdown("📍 Ribeirão Preto - SP")
    st.markdown("📞 +55 (16) 9 9786-3346")
with col2:
    st.markdown("📧 [rogersamacedo@hotmail.com](mailto:rogersamacedo@hotmail.com)")
    st.markdown("🔗 [LinkedIn](https://linkedin.com)")

st.divider()

# --- OBJETIVO ---
st.subheader("🎯 Objetivo")
st.write("**Cientista de Dados | Inteligência Artificial | Visão Computacional**")

# --- RESUMO PROFISSIONAL ---
st.subheader("👤 Resumo Profissional")
st.write("""
Profissional com sólida experiência em tecnologia e implantação de sistemas, especializado em Ciência de Dados, 
Inteligência Artificial e **Visão Computacional**. Certificado em IA Generativa (Google Gemini AI), **Modelos de 
Detecção de Objetos (YOLO)** e Cloud Computing. **Desenvolvedor de 04 projetos práticos em Visão Computacional** 
envolvendo processamento de imagens com OpenCV e Deep Learning (CNNs). Participante do programa Oracle Next Education 
com formação em Ciência de Dados e participação em Hackathon oficial. Combina visão de negócio com capacidade técnica 
aplicada a dados, IA profunda e arquiteturas de nuvem.
""")

# --- COMPETÊNCIAS TÉCNICAS ---
st.subheader("🛠️ Competências Técnicas")
st.write("""
- **Linguagens:** Python, SQL, MySQL.
- **Visão Computacional & IA:** OpenCV, Algoritmos YOLO, Redes Neurais Convencionais (CNNs), Machine Learning, Deep Learning.
- **Dados & BI:** Modelagem, Tratamento e Visualização de Dados, Power BI.
- **Tecnologias:** Cloud Computing (OCI), Linux, Processamento e Filtragem de Imagens.
""")

# --- EXPERIÊNCIA PROFISSIONAL ---
st.subheader("💼 Experiência Profissional")

# --- PUC-Rio ---
st.markdown("### **Instituto ECOA – PUC-Rio**")
st.caption("Técnico Residente em Análise de Dados | 2025 – Atual")
st.write("""
- Tratamento e análise de dados para geração de insights operacionais e estratégicos.
- Desenvolvimento de dashboards, pipelines de dados e visualizações dinâmicas.
- Aplicação de técnicas analíticas e algoritmos de IA para solução de problemas complexos.
""")

# --- SIMUS TECNOLOGIA ---
st.markdown("### **Simus Tecnologia Ltda**")
st.caption("Analista Fiscal SR | Janeiro de 2021 a Maio de 2023")
st.write("""
- Suporte especializado ao cliente em software fiscal (Windows/Visual Basic).
- Responsável pela instalação, configuração e parametrização do sistema.
- Condução de treinamentos técnicos das funcionalidades do software para clientes finais.
""")

# --- SOCIN ---
st.markdown("### **SOCIN – Soluções Comerciais Integradas**")
st.caption("Analista de Service Desk")
st.write("""
- Suporte técnico em ambiente Linux e Java.
- Implantação e parametrização de sistemas.
- Participação estratégica na migração fiscal nacional (ECF → NFC-e).
""")

# --- FORMAÇÃO ACADÊMICA ---
st.subheader("🎓 Formação Acadêmica")
st.write("- **MBA Data Science & Analytics** – USP/ESALQ (em andamento)")
st.write("- **MBA Big Data e Inteligência Competitiva** – Concluído")
st.write("- **Pós-graduação em Análise de Dados** – Concluído")
st.write("- **Graduação em Administração** – Concluído")

# --- CERTIFICAÇÕES E CURSOS ---
st.subheader("📜 Certificações e Cursos Extensão")
st.write("""
- **Formação em Visão Computacional (60h)** – NextVisual
- **TIC em Trilhas: Visão Computacional com YOLO (24h)** – MCTI
- Oracle Cloud Infrastructure Foundations Associate
- Google Education – Gemini AI for Students (válido até 2029)
- Artificial Intelligence Fundamentals – IBM
- Cloud Aplicada – Venturus
- Residência em Análise de Dados – PUC-Rio
- Oracle Next Education (ONE) – Ciência de Dados (em andamento)
""")
