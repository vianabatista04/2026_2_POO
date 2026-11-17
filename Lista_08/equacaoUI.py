import streamlit as st
import pandas as pd
from equacao import Equacao

class EquacaoUI:
    def main():
        st.header("Equação do II Grau: y = ax**2 + bx+c")
        a=st.text_input("a")
        b=st.text_input("b")
        c=st.text_input("c")
        if st.button("Calcular"):
            try:
                if a and b and c:
                    e=Equacao(int(a),int(b),int(c))
                    st.write(f"Delta = {e.Delta()}")
                    st.write(f"X1 = {e.X1()}")
                    st.write(f"X2 = {e.X2()}")
                    st.write(e)

                    if e.Delta()>=0:
                        st.title("Gráfico de uma função do segundo grau")
                        x=list(range(-10,11))
                        y = [e.Y(val) for val in x]

                        dados = pd.DataFrame({
                            "x": x,
                            "y": y
                        })
                        st.line_chart(
                            data=dados,
                            x="x",
                            y="y",
                            x_label="Valores de X",
                            y_label="Valores de Y"
                        )
                    else:
                        st.info("Gráfico não gerado pois a equação não tem raízes reais, ou seja, o delta é negativo")
                else:
                    st.warning("Preencha todos os coeficientes(a, b e c)")
            except ValueError as erro:
                st.error(f"Erro nos valores informados: {erro}")        
