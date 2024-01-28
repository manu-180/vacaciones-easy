from altair import limit_rows
import streamlit as st 
from openai import OpenAI 
import dotenv
import os 

dotenv.load_dotenv()
OpenAiKey = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = OpenAiKey)

def generate_vacations(vacaciones, limit_vacaciones):
    
    prompt = f"Como experto en planificación de viajes, planifica las vacaciones de manera eficiente y personalizadaIndica. Teniendo en cuenta factores como: Elección del destino, clima, diferencias culturales, salud y seguridad. Segun donde el usuario quiera ir de vacaciones:\n{vacaciones}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user", 
                "content": prompt,
            }
        ], 
        max_tokens = limit_vacaciones * 5,
    )
    
    response = response.choices[0].message.content
    
    if response:
        response = response.split(".")
        response = ".".join(response[:-1]) + "."
        return response
    
def main():
    st.title("Organiza tus Vacaciones")
    st.text("Instrucciones de uso:")
    st.text("1. Ingresa las vacaciones que quieras organizar")
    st.text("2. Oprime el boton ""Generar Tareas""")
    st.text("3. Se genera las tareas a realizar")
    st.text("4. Se genera el reporte")
    
    st.text("---")
    
    st.text("Ingresa las vacaciones que quieras organizar:")
    vacaciones = st.text_input("Descripcion", max_chars=100)
    
    limit_vacaciones = st.slider("Limite de respuesta", 50, 100, 100)
    
    if st.button("Generar Tareas"):
        response = generate_vacations(vacaciones, limit_vacaciones)
        st.write(response)
    
if __name__ == "__main__":
    main()  