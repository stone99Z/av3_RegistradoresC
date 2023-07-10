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
regiones_peru = ['Amazonas', 'Áncash', 'Apurímac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Callao',
                 'Cusco', 'Huancavelica', 'Huánuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque',
                 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 'Pasco', 'Piura', 'Puno', 'San Martín',
                 'Tacna', 'Tumbes', 'Ucayali']

region = st.selectbox(label="", options=regiones_peru, index=0)

provincias_peru = {
    'Amazonas': ['Chachapoyas', 'Bagua', 'Bongará', 'Condorcanqui', 'Luya', 'Rodríguez de Mendoza',
                 'Utcubamba'],
    'Áncash': ['Huaraz', 'Aija', 'Antonio Raymondi', 'Asunción', 'Bolognesi', 'Carhuaz', 'Carlos Fermín Fitzcarrald',
               'Casma', 'Corongo', 'Huari', 'Huarmey', 'Huaylas', 'Mariscal Luzuriaga', 'Ocros', 'Pallasca', 'Pomabamba',
               'Recuay', 'Santa', 'Sihuas', 'Yungay'],
    'Apurímac': ['Abancay', 'Andahuaylas', 'Antabamba', 'Aymaraes', 'Cotabambas', 'Grau'],
    'Arequipa': ['Arequipa', 'Camaná', 'Caravelí', 'Castilla', 'Caylloma', 'Condesuyos', 'Islay', 'La Unión'],
    'Ayacucho': ['Huamanga', 'Cangallo', 'Huanca Sancos', 'Huanta', 'La Mar', 'Lucanas', 'Parinacochas', 'Paucar del Sara Sara',
                 'Sucre', 'Víctor Fajardo', 'Vilcas Huamán'],
    'Cajamarca': ['Cajamarca', 'Cajabamba', 'Celendín', 'Chota', 'Contumazá', 'Cutervo', 'Hualgayoc', 'Jaén', 'San Ignacio',
                  'San Marcos', 'San Miguel', 'San Pablo', 'Santa Cruz'],
    'Callao': ['Callao'],
    'Cusco': ['Cusco', 'Acomayo', 'Anta', 'Calca', 'Canas', 'Canchis', 'Chumbivilcas', 'Espinar', 'La Convención', 'Paruro',
              'Paucartambo', 'Quispicanchi', 'Urubamba'],
    'Huancavelica': ['Huancavelica', 'Acobamba', 'Angaraes', 'Castrovirreyna', 'Churcampa', 'Huaytará', 'Tayacaja'],
    'Huánuco': ['Huánuco', 'Ambo', 'Dos de Mayo', 'Huacaybamba', 'Huamalíes', 'Leoncio Prado', 'Marañón', 'Pachitea',
                'Puerto Inca', 'Lauricocha', 'Yarowilca'],
    'Ica': ['Ica', 'Chincha', 'Nasca', 'Palpa', 'Pisco'],
    'Junín': ['Huancayo', 'Concepción', 'Chanchamayo', 'Jauja', 'Junín', 'Satipo', 'Tarma', 'Yauli'],
    'La Libertad': ['Trujillo', 'Ascope', 'Bolívar', 'Chepén', 'Julcán', 'Otuzco', 'Pacasmayo', 'Pataz', 'Sánchez Carrión',
                    'Santiago de Chuco', 'Gran Chimú', 'Virú'],
    'Lambayeque': ['Chiclayo', 'Ferreñafe', 'Lambayeque'],
    'Lima': ['Lima', 'Barranca', 'Cajatambo', 'Canta', 'Cañete', 'Huaral', 'Huarochirí', 'Huaura', 'Oyón', 'Yauyos'],
    'Loreto': ['Iquitos', 'Alto Amazonas', 'Loreto', 'Mariscal Ramón Castilla', 'Maynas', 'Requena', 'Ucayali', 'Datem del Marañón',
               'Putumayo', 'Tigre', 'Yaraví'],
    'Madre de Dios': ['Tambopata', 'Manu', 'Tahuamanu'],
    'Moquegua': ['Mariscal Nieto', 'General Sánchez Cerro', 'Ilo'],
    'Pasco': ['Pasco', 'Daniel Alcides Carrión', 'Oxapampa'],
    'Piura': ['Piura', 'Ayabaca', 'Huancabamba', 'Morropón', 'Paita', 'Sullana', 'Talara', 'Sechura'],
    'Puno': ['Puno', 'Azángaro', 'Carabaya', 'Chucuito', 'El Collao', 'Huancané', 'Lampa', 'Melgar', 'Moho', 'San Antonio de Putina',
             'San Román', 'Sandia', 'Yunguyo'],
    'San Martín': ['Moyobamba', 'Bellavista', 'El Dorado', 'Huallaga', 'Lamas', 'Mariscal Cáceres', 'Picota', 'Rioja', 'San Martín',
                   'Tocache']

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
