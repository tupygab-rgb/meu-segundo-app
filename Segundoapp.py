import streamlit as st

# ===============================
# TÍTULO E INTRODUÇÃO
# ===============================
st.title("🥗 Calculadora de Calorias e Macros do TUPY")
st.header("Preencha seus dados abaixo para começar!")

st.markdown("""
🌿 **Alimentação Natural e Consciente**  
Lembre-se: o que você ingere influencia seu bem-estar completo.  
Procure priorizar alimentos naturais, frescos e equilibrados, criando uma rotina alimentar que respeite seu corpo e traga vitalidade para todas as áreas da sua vida.
Esta calculadora serve apenas como referência. O mais importante é escolher alimentos naturais e frescos, escutando seu corpo e cultivando vitalidade física e espiritual, respeitando a harmonia do seu ser.
""")

st.divider()

# ===============================
# DADOS PESSOAIS
# ===============================
st.subheader("👤 Dados Pessoais")

col_nome, col_sexo = st.columns([2, 1])

with col_nome:
    nome = st.text_input("Nome")

with col_sexo:
    sexo = st.selectbox("Sexo Biológico", ["Selecione...", "Masculino", "Feminino"])

# ===============================
# DADOS CORPORAIS
# ===============================
st.subheader("📏 Dados Corporais")

col1, col2, col3 = st.columns(3)

with col1:
    idade = st.number_input("Idade", min_value=10, max_value=150, step=1, value = None)

with col2:
    peso = st.number_input("Peso (kg)", min_value=30.0, max_value=400.0, step=0.1, value = None)

with col3:
    altura = st.number_input("Altura (cm)", min_value=100, max_value=300, step=1, value = None)

# ===============================
# CÁLCULO DA TMB
# ===============================
def calcular_tmb(idade, peso, altura, sexo):
    if sexo == "Masculino":
        return 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        return 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

tmb = None
gcd = None
resultado = None

if sexo != "Selecione..." and idade and peso and altura:
    tmb = calcular_tmb(idade, peso, altura, sexo)
    st.divider()
    st.subheader("🔥 Gasto Calórico Base (TMB)")
    st.success(f"{tmb:.0f} Kcal por dia")
else:
    st.warning("Preencha corretamente todos os dados acima para continuar.")

# ===============================
# ATIVIDADE FÍSICA
# ===============================
if tmb is not None:
    st.divider()
    st.subheader("🏃‍♂️ Nível de Atividade Física")

    atividade = st.selectbox(
        "Selecione seu nível de atividade:",
        ["Selecione...", "Sedentário", "Levemente ativo", "Moderadamente ativo", "Muito ativo", "Extremamente ativo"]
    )

    fatores = {
        "Sedentário": 1.2,
        "Levemente ativo": 1.375,
        "Moderadamente ativo": 1.55,
        "Muito ativo": 1.725,
        "Extremamente ativo": 1.9
    }

    if atividade != "Selecione...":
        gcd = tmb * fatores[atividade]
        st.success(f"Gasto Calórico Diário estimado: **{gcd:.0f} Kcal**")

# ===============================
# OBJETIVO
# ===============================
if gcd is not None:
    st.divider()
    st.subheader("🎯 Objetivo")

    objetivo = st.selectbox(
        "Qual seu objetivo?",
        ["Selecione...", "Perder Peso", "Manter o Peso", "Ganhar Peso"]
    )

    if objetivo != "Selecione...":
        if objetivo == "Perder Peso":
            resultado = gcd - 500
        elif objetivo == "Manter o Peso":
            resultado = gcd
        elif objetivo == "Ganhar Peso":
            resultado = gcd + 500

        st.success(f"👉 Consumo recomendado: **{resultado:.0f} Kcal por dia**")

# ===============================
# MACROS
# ===============================
if resultado is not None:
    st.divider()
    st.subheader("🥩🥑🍚 Distribuição de Macros")

    if objetivo == "Perder Peso":
        fat_prot, fat_gord = 2.0, 0.75
    elif objetivo == "Manter o Peso":
        fat_prot, fat_gord = 1.8, 0.75
    elif objetivo == "Ganhar Peso":
        fat_prot, fat_gord = 1.8, 1.0

    prot_g = peso * fat_prot
    gord_g = peso * fat_gord

    kcal_prot = prot_g * 4
    kcal_gord = gord_g * 9
    kcal_carb = resultado - (kcal_prot + kcal_gord)
    carb_g = kcal_carb / 4

    colp, colg, colc = st.columns(3)

    with colp:
        st.metric("Proteínas", f"{prot_g:.1f} g")

    with colg:
        st.metric("Gorduras", f"{gord_g:.1f} g")

    with colc:
        st.metric("Carboidratos", f"{carb_g:.1f} g")

# ===============================
# AVISO FINAL
# ===============================
if resultado is not None:
    st.divider()

    st.markdown(f"**{nome}**, espero que de alguma forma eu possa ter te ajudado com essa calculadora! 👊")

with st.expander("⚠️ Aviso Importante"):
            st.warning("""
        ⚠️ **Importante**  
        Deixo claro que uma alimentação extremamente regrada, baseada apenas em proteínas, carboidratos e gorduras, provavelmente não será a melhor para sua saúde e vitalidade!

Ela pode ajudar esteticamente, mas para que realmente seja completa, procure manter uma alimentação equilibrada e natural todos os dias.

Além disso, essa calculadora foi feita de forma amadora, sem qualquer formação envolvida do autor. Objetivo é apenas te ajudar, entretanto, não use-a como verdade absoluta.
        """)
        
            st.markdown("""
        **Opinião do autor**: "Acredito que uma dieta assim, vai te trazer mudanças estéticas muito boas sim, mas quando se fala de saúde e vitalidade,
        o mais importante é o consumo de alimentos naturais, e reconhecer a importância do carboidratos (cereais, legumes, frutas), mais que isso,
        seu corpo é uma excelente máquina para produzir o que você precisa, deixe-o trabalhar, evite alimentos muito processados."
        Fortaleça corpo💪, mente🧠 e espírito🙏
        """)
if resultado is not None:
        st.write("Com os macros na palma da sua mão🤌, agora é só ficar atento a tabela nutricional do alimentos, anotar o que ingeriu e pronto!")
        st.info("Observação: existem vários aplicativos que facilitam essa anotação...")
        











