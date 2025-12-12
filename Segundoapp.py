import streamlit as st
import unicodedata

# Normalização do texto (remove acentos, espaços etc.)
def normalizar(texto):
    texto = texto.strip().lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto


st.title("Cálculo de Metabolismo Basal e Macronutrientes")
st.write("Preencha seus dados abaixo para receber seu plano nutricional básico.")

# Inputs
nome = st.text_input("Nome:")
idade = st.number_input("Idade:", min_value=0, max_value=150, step=1)
peso = st.number_input("Peso (kg):", min_value=20.0, max_value=300.0, step=0.1)
altura = st.number_input("Altura (cm):", min_value=100.0, max_value=230.0, step=0.1)
genero = st.text_input("Gênero (Masculino/Feminino):")
objetivo = st.selectbox("Qual seu objetivo?",
                        ["Emagrecer", "Ganhar massa muscular", "Manter peso"])


def calcular_tmb(peso, altura, idade, genero):
    g = normalizar(genero)

    if g in ["masculino", "m", "masc"]:
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif g in ["feminino", "f", "fem"]:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    else:
        return None
    
    return tmb


def calcular_macro(calorias, peso, objetivo):
    if objetivo == "Emagrecer":
        proteina_g = 2.0 * peso
        gordura_g = 0.8 * peso
    elif objetivo == "Ganhar massa muscular":
        proteina_g = 2.2 * peso
        gordura_g = 1.0 * peso
    else:
        proteina_g = 1.8 * peso
        gordura_g = 0.8 * peso

    # calorias dos macros
    kcal_proteina = proteina_g * 4
    kcal_gordura = gordura_g * 9

    # carboidrato = calorias restantes
    kcal_carbo = calorias - (kcal_proteina + kcal_gordura)
    carbo_g = kcal_carbo / 4

    return proteina_g, carbo_g, gordura_g



if st.button("Calcular"):
    if not nome:
        st.error("Por favor, preencha o nome.")
    else:
        tmb = calcular_tmb(peso, altura, idade, genero)

        if tmb is None:
            st.warning("Gênero inválido. Digite Masculino ou Feminino.")
        else:
            # Ajuste calórico conforme objetivo
            if objetivo == "Emagrecer":
                calorias = tmb - 400
            elif objetivo == "Ganhar massa muscular":
                calorias = tmb + 300
            else:
                calorias = tmb

            proteina_g, carbo_g, gordura_g = calcular_macro(calorias, peso, objetivo)

            st.success(f"**{nome}**, sua TMB é de **{tmb:.0f} kcal/dia**.")
            st.info(f"Para **{objetivo.lower()}**, você deve consumir aproximadamente **{calorias:.0f} kcal/dia**.")

            st.write("### Distribuição de Macronutrientes")
            st.write(f"- **Proteínas:** {proteina_g:.0f} g")
            st.write(f"- **Carboidratos:** {carbo_g:.0f} g")
            st.write(f"- **Gorduras:** {gordura_g:.0f} g")




