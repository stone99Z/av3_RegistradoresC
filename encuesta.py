import streamlit as st
from PIL import Image

image = Image.open('logo_reniec.jpg')
st.image(image, caption='', use_column_width=True)

st.title("Encuesta de Evaluación de Registradores Civiles Capacitados")

html_temp = """
<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
<h2 style="color:white;text-align:left;">Datos personales: </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

st.write('**¿Cuál es tu edad?**')
edad = st.slider(label="", min_value=1, max_value=100, value=18, step=1)

st.write('**¿Cuál es tu género?**')
genero = st.selectbox(label="", options=['Masculino', 'Femenino'], index=0)

st.write('**¿En qué región vives?**')
region = st.selectbox(label="", options=['Región 1', 'Región 2', 'Región 3'], index=0)

st.write('**¿En qué distrito vives?**')
distrito = st.selectbox(label="",
                        options=['Distrito 1', 'Distrito 2', 'Distrito 3'],
                        index=0)

html_temp = """
<div style="background-color:#26c5de;padding:0.2 px">
<h2 style="color:white;text-align:left;">Evaluación de Registradores Civiles Capacitados: </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)
st.title("Encuesta de Evaluación de Registradores Civiles Capacitados [Registro Nacional de Identificación y Estado Civil]")

st.write('**¿El registrador civil recibió capacitación sobre los procedimientos del Registro Nacional de Identificación y Estado Civil?**')
pregunta1 = st.selectbox(label="Pregunta 1", options=['Sí', 'No'], index=0, key="pregunta1")

st.write('**¿El registrador civil conoce los requisitos y trámites para la inscripción de nacimientos, matrimonios y defunciones?**')
pregunta2 = st.selectbox(label="Pregunta 2", options=['Sí', 'No'], index=0, key="pregunta2")

st.write('**¿El registrador civil aplica correctamente los procedimientos establecidos por el Registro Nacional de Identificación y Estado Civil?**')
pregunta3 = st.selectbox(label="Pregunta 3", options=['Sí', 'No'], index=0, key="pregunta3")

st.write('**¿El registrador civil proporciona un servicio eficiente y de calidad a los usuarios del Registro Nacional de Identificación y Estado Civil?**')
pregunta4 = st.selectbox(label="Pregunta 4", options=['Sí', 'No'], index=0, key="pregunta4")

st.write('**¿El registrador civil brinda información clara y precisa a los usuarios sobre los trámites y requisitos del Registro Nacional de Identificación y Estado Civil?**')
pregunta5 = st.selectbox(label="Pregunta 5", options=['Sí', 'No'], index=0, key="pregunta5")

st.write('**¿El registrador civil maneja correctamente la documentación y los registros del Registro Nacional de Identificación y Estado Civil?**')
pregunta6 = st.selectbox(label="Pregunta 6", options=['Sí', 'No'], index=0, key="pregunta6")

st.write('**¿El registrador civil actualiza de manera oportuna y precisa los datos en el Registro Nacional de Identificación y Estado Civil?**')
pregunta7 = st.selectbox(label="Pregunta 7", options=['Sí', 'No'], index=0, key="pregunta7")

st.write('**¿El registrador civil cumple con los plazos establecidos para la inscripción de los actos civiles?**')
pregunta8 = st.selectbox(label="Pregunta 8", options=['Sí', 'No'], index=0, key="pregunta8")

st.write('**¿El registrador civil garantiza la confidencialidad y seguridad de la información personal registrada en el Registro Nacional de Identificación y Estado Civil?**')
pregunta9 = st.selectbox(label="Pregunta 9", options=['Sí', 'No'], index=0, key="pregunta9")

st.write('**¿El registrador civil participa en programas de actualización y capacitación continua sobre el Registro Nacional de Identificación y Estado Civil?**')
pregunta10 = st.selectbox(label="Pregunta 10", options=['Sí', 'No'], index=0, key="pregunta10")

def main():
    if st.button("**EJECUTAR**"):
        resultado = ''
        if (pregunta1 == 'Sí' and pregunta2 == 'Sí' and pregunta3 == 'Sí' and 
            pregunta4 == 'Sí' and pregunta5 == 'Sí' and pregunta6 == 'Sí' and 
            pregunta7 == 'Sí' and pregunta8 == 'Sí' and pregunta9 == 'Sí' and 
            pregunta10 == 'Sí'):
            resultado = 'El registrador civil demuestra un alto nivel de conocimiento y eficiencia en los procedimientos del Registro Nacional de Identificación y Estado Civil.'
        else:
            resultado = 'Es recomendable brindar capacitación adicional al registrador civil para mejorar su desempeño y conocimiento en los procedimientos del Registro Nacional de Identificación y Estado Civil.'
        
        st.write(resultado)

if __name__ == '__main__':
    main()
