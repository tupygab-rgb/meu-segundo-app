import streamlit as st

# ----------------------------
# Cabeçalho
# ----------------------------
st.title("Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

st.markdown("""
🌿 **Alimentação Natural e Consciente**  
Lembre-se: o que você ingere influencia seu bem-estar completo.  
Procure priorizar alimentos naturais, frescos e equilibrados, criando uma rotina alimentar que respeite seu corpo e traga vitalidade para todas as áreas da sua vida.
""")

st.divider()

# ----------------------------
# Inputs do usuário
# ----------------------------
nome = st.text_input("Nome: ")
idade = st.number_input("Idade: ", min_value=10, max_value=150, step=1)
peso = st.number_input("Peso (kg): ", min_value=30.0, max_value=400.0, step=0.1)
altura = st.number_input("Altura (cm): ", min_value=100, max_value=300, step=1)
sexo = st.selectbox("Sexo Biológico: ", ["Selecione...", "Masculino", "Feminino"])

tmb = None
gcd = None
resultado = None

# ----------------------------
# Função TMB
# ----------------------------
def calcular_tmb(idade, peso, altura, sexo):
    if sexo == "Masculino":
        return 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    else:
        return 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)

# ----------------------------
# Calcular TMB
# ----------------------------
if sexo != "Selecione...":
    tmb = calcular_tmb(idade, peso, altura, sexo)
    st.subheader(f"Sua Gasto Calórico Base é 💥 {tmb:.0f} Kcal")
else:
    st.warning("Preencha todos campos acima para continuar.")

st.divider()

# ----------------------------
# Atividade física
# ----------------------------
if tmb is not None:
    st.write("Agora, vamos calcular seu gasto calórico de acordo com seu nível de atividade 💪:")
    atividade = st.selectbox(
        "Nível de atividade física:", 
        ["Selecione...", "Sedentário", "Levemente ativo", "Moderadamente ativo", "Muito ativo", "Extremamente ativo"]
    )

    fator = {
        "Sedentário": 1.2,
        "Levemente ativo": 1.375,
        "Moderadamente ativo": 1.55,
        "Muito ativo": 1.725,
        "Extremamente ativo": 1.9
    }

    if atividade != "Selecione...":
        gcd = tmb * fator[atividade]
        st.subheader(f"Seu Gasto Calórico Diário estimado é 🔥 {gcd:.0f} Kcal")
        
        # ----------------------------
        # Objetivo
        # ----------------------------
        objetivo = st.selectbox("Qual seu Objetivo?", ["Selecione...", "Perder Peso", "Manter o Peso", "Ganhar Peso"])
        if objetivo != "Selecione...":
            if objetivo == "Perder Peso":
                resultado = gcd - 500
                fat_prot, fat_gord = 2.0, 0.75
            elif objetivo == "Manter o Peso":
                resultado = gcd
                fat_prot, fat_gord = 1.8, 0.75
            elif objetivo == "Ganhar Peso":
                resultado = gcd + 500
                fat_prot, fat_gord = 1.8, 1.0

            st.success(f"**{nome}**, você deve consumir {resultado:.0f} Kcal por dia 🥗")

            # ----------------------------
            # Macros
            # ----------------------------
            prot_g = peso * fat_prot
            gord_g = peso * fat_gord
            kcal_prot = prot_g * 4
            kcal_gord = gord_g * 9
            kcal_carb = resultado - (kcal_prot + kcal_gord)
            carb_g = kcal_carb / 4

            st.divider()
            st.subheader("Distribuição de Macros 🥩🥑🍚")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Proteínas (g)", f"{prot_g:.1f}")
            col2.metric("Gorduras (g)", f"{gord_g:.1f}")
            col3.metric("Carboidratos (g)", f"{carb_g:.1f}")

            # ----------------------------
            # Aviso / explicação
            # ----------------------------
            with st.expander("⚠️ Aviso Importante"):
                st.warning("""
Esta calculadora serve apenas como **referência** e não substitui orientação profissional.  

Uma alimentação extremamente regrada, baseada apenas em proteínas, carboidratos e gorduras, pode não ser a melhor para sua saúde e vitalidade.  
Priorize sempre alimentos naturais e ouça seu corpo.  
                """)

