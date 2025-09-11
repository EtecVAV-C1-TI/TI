import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo=LinearRegression()

x=df[["diametro"]]
y=df[["preco"]]

modelo.fit(x, y)

st.divider()
st.title("Prevendo o valor da pizza")
st.divider()

diametro=st.number_input("Digite o tamanho do diâmetro da pizza em centímetros: ")

if diametro:
    preco_previsto=modelo.predict([[diametro]])[0] [0]
    st.write(f"O valor da pizza com o diâmetro de {diametro:.2f} é de R${preco_previsto:.2f}")