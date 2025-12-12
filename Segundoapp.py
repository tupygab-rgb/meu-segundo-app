import streamlit as st

st.title("Cadastro rápido")
st.write("Seja muito bem-vindo! Para que possamos te conhecer melhor, preencha os dados abaixo.")

# --- Inputs ---
nome = st.text_input("Nome:")
idade = st.number_input("Idade:", min_value=0, max_value=150, step=1)
genero = st.text_input("Gênero: ")


# --- Função que processa os dados ---
def confirmar_dados(nome, idade, genero):
    # normaliza: tira espaços e passa pra minusculo
    g = genero.strip().lower()
    if g in ["masculino", "m", "masc"]:
        if int(idade) < 18:
            st.success(f"Perfeito! Então você é o mano {nome} e você tem {int(idade)} anos. É uma criança ainda kkkkk")
        else:
            st.success(f"Perfeito! Então você é o mano {nome} e você tem {int(idade)} anos. Hum já é um adultinho ein")
    elif g in ["feminino", "f", "fem"]:
        if int(idade) < 18:
            st.success(f"Perfeito! Então você é a mana {nome} e você tem {int(idade)} anos. É uma princesinha ainda kkkkk")
        else:
            st.success(f"Perfeito! Então você é a mana {nome} e você tem {int(idade)} anos. Hum já é uma garota adulta ein")
    else:
        st.warning("Escreve direito, bobão🥱")

# --- Botão para enviar ---
if st.button("Enviar"):
    if not nome:
        st.error("Por favor, preencha o nome.")
    else:
        confirmar_dados(nome, idade, genero)

