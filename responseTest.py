# # data = [ {'Questions': '¿Cómo se accede a Yammer en Yammer Web 2020?', 'A': 'a) Usando una cuenta de correo electrónico personal y accediendo a través de la página web de Yammer', 'B': 'b) Usando una dirección de correo electrónico de la empresa y accediendo a través de la página web de Yammer', 'C': 'c) Usando una cuenta de correo electrónico personal y accediendo a través de la página web de la empresa', 'D': 'd) Usando una dirección de correo electrónico de la empresa y accediendo a través de la página web de la empresa', 'Correct Answers': 'b) Usando una dirección de correo electrónico de la empresa y accediendo a través de la página web de Yammer'}, {'Questions': '¿Qué se puede personalizar en tu perfil de Yammer?', 'A': 'a) Nombre y foto de perfil', 'B': 'b) Intereses, experiencia, historial laboral, foto de perfil y portada', 'C': 'c) Solo la foto de perfil', 'D': 'd) Solo la portada', 'Correct Answers': 'b) Intereses, experiencia, historial laboral, foto de perfil y portada'}, {'Questions': '¿Cómo se navega entre diferentes versiones de Yammer?', 'A': 'a) Usando un menú desplegable en la página principal', 'B': 'b) Usando un interruptor de palanca entre la nueva y la clásica versión', 'C': 'c) Usando un botón de cambio en la barra de herramientas', 'D': 'd) Usando un enlace en el pie de página', 'Correct Answers': 'b) Usando un interruptor de palanca entre la nueva y la clásica versión'}, {'Questions': '¿Cuál es el propósito del buzón de entrada de Yammer?', 'A': 'a) Organizar, leer y responder a los mensajes', 'B': 'b) Enviar mensajes privados a otros usuarios', 'C': 'c) Crear y administrar grupos', 'D': 'd) Configurar la cuenta de usuario', 'Correct Answers': 'a) Organizar, leer y responder a los mensajes'}, {'Questions': '¿Cómo se envía un mensaje privado en Yammer?', 'A': 'a) Usando el botón de Mensaje Nuevo en la página principal', 'B': 'b) Usando el botón de Nuevo Mensaje Privado', 'C': 'c) Usando el botón de Compartir en la página principal', 'D': 'd) Usando el botón de Compartir en un grupo', 'Correct Answers': 'b) Usando el botón de Nuevo Mensaje Privado'}, {'Questions': '¿Qué función se utiliza para administrar y organizar los mensajes en el buzón de entrada de Yammer?', 'A': 'a) La función de búsqueda', 'B': 'b) Las herramientas de administración del buzón de entrada', 'C': 'c) La función de filtrado', 'D': 'd) La función de etiquetado', 'Correct Answers': 'b) Las herramientas de administración del buzón de entrada'}, {'Questions': '¿Cómo se pueden responder a los mensajes en Yammer?', 'A': 'a) Usando el botón de Mensaje Nuevo en la página principal', 'B': 'b) Usando el botón de Comentario debajo de un mensaje', 'C': 'c) Usando el botón de Compartir en la página principal', 'D': 'd) Usando el botón de Compartir en un grupo', 'Correct Answers': 'b) Usando el botón de Comentario debajo de un mensaje'}, {'Questions': '¿Cuál es un método para marcar los mensajes como leídos en el buzón de entrada de Yammer?', 'A': 'a) Usando un botón de Marcar como Leído en la página principal', 'B': 'b) Usando un icono de marca de verificación en el buzón de entrada', 'C': 'c) Usando un botón de Marcar como Leído en un mensaje', 'D': 'd) Usando un icono de marca de verificación en un mensaje', 'Correct Answers': 'b) Usando un icono de marca de verificación en el buzón de entrada'}, {'Questions': '¿Cómo se actualiza tu perfil de Yammer?', 'A': 'a) Usando el botón de Actualizar en la página principal', 'B': 'b) Usando el enlace de Editar configuración en la página de Configuración', 'C': 'c) Usando el botón de Cambiar foto de perfil en la página principal', 'D': 'd) Usando el botón de Cambiar portada en la página principal', 'Correct Answers': 'b) Usando el enlace de Editar configuración en la página de Configuración'}, {'Questions': '¿Cuál es la función del iniciador de aplicaciones en Yammer?', 'A': 'a) Crear y administrar grupos', 'B': 'b) Navegar a otras aplicaciones de Office', 'C': 'c) Buscar mensajes y conversaciones', 'D': 'd) Configurar la cuenta de usuario', 'Correct Answers': 'b) Navegar a otras aplicaciones de Office'} ]

# # import json
# # llmResponseJSON = json.loads(data)
# # print()

# # import pandas as pd
# # dataFrame = pd.DataFrame(data)
# # print(f"DataFrame: {dataFrame}")


# data = """{
#     "Questions": [
#         "Problem records"
#     ],

#     "OptionsA": [
#         "HelloA"
#     ],

#     "OptionsB": [
#         "HelloB"
#     ],

#     "OptionsC": [
#         "HelloC"
#     ]
# }
# """
# # data_start_index = data.find('{')
# # data_end_index = data.find('}') + 1
# # json_data_string = data[data_start_index:data_end_index]  # Extract the JSON data string
# # print(f"EXTRACTED RESPONSE: {json_data_string}")

# # import json
# # llmResponseJSON = json.loads(json_data_string)
# # print(f"\n\nDF-INPUT-DATA-JSON: {llmResponseJSON}")

# # import pandas as pd
# # dataFrame = pd.DataFrame([llmResponseJSON])
# # print(f"DataFrame: {dataFrame}")




# # data = [['Questions', 'A', 'B', 'C', 'D', 'Correct Answers'], ['How do you access Yammer in Yammer Web 2020?', 'Through the Yammer desktop application', 'Using a company email address and accessing via Office 365', 'By downloading the Yammer app on a mobile device', 'Via a direct link in an email', 'b) Using a company email address and accessing via Office 365'], ['What can be customized in your Yammer profile?', 'Your network and group memberships', 'Interests, expertise, work history, profile picture, and birthday', 'The layout of the Yammer feed', 'The design of the Yammer interface', 'b) Interests, expertise, work history, profile picture, and birthday'], ['How do you navigate between different versions of Yammer?', 'By changing settings in the Profile menu', 'Using a toggle switch between the new and classic versions', 'By installing different versions of the application', 'The version cannot be changed', 'b) Using a toggle switch between the new and classic versions'], ['What is the purpose of the Yammer inbox?', 'To organize, read, and reply to messages', 'To store files and documents', 'To customize user settings', 'To manage group memberships', 'a) To organize, read, and reply to messages'], ['How do you send a private message in Yammer?', 'Through the main feed', 'Using the New Private Message button', 'By tagging a user in a public post', 'Via the Files tab', 'b) Using the New Private Message button'], ['What feature is used to manage and organize messages in Yammer?', 'The Communities tab', 'The Files directory', 'The inbox management tools', 'The profile settings', 'c) The inbox management tools'], ['How can you reply to messages in Yammer?', 'By creating a new post in the feed', 'Using the Comment button beneath a message', 'Through the Yammer desktop application only', 'By sending an email', 'b) Using the Comment button beneath a message'], ['What is a method for marking messages as read or unread in Yammer?', 'Through the Office 365 settings', 'Using a checkmark icon in the inbox', 'By opening each message individually', 'This feature is not available in Yammer', 'b) Using a checkmark icon in the inbox'], ['How do you update your Yammer profile?', 'By emailing the Yammer support team', 'Using the Edit settings link in the Settings panel', 'Through the Communities tab', 'Profile updates are not permitted', 'b) Using the Edit settings link in the Settings panel'], ['What is the function of the app launcher in Yammer Web 2020?', 'To close the Yammer application', 'To navigate to other Office applications', 'To change language settings', 'For editing user profiles', 'b) To navigate to other Office applications']]
# # data = [['Preguntas', 'A', 'B', 'C', 'D', 'Respuestas Correctas'], ['¿Cómo se accede a Yammer en Yammer Web 2020?', 'A través de la aplicación de escritorio de Yammer', 'Usando una dirección de correo electrónico de la empresa y accediendo a través de Office 365', 'Descargando la aplicación de Yammer en un dispositivo móvil', 'A través de un enlace directo en un correo electrónico', 'b) Usando una dirección de correo electrónico de la empresa y accediendo a través de Office 365'], ['¿Qué se puede personalizar en tu perfil de Yammer?', 'Tu red y membresías de grupo', 'Intereses, experiencia, historial laboral, foto de perfil y cumpleaños', 'El diseño del feed de Yammer', 'El diseño de la interfaz de Yammer', 'b) Intereses, experiencia, historial laboral, foto de perfil y cumpleaños'], ['¿Cómo se navega entre diferentes versiones de Yammer?', 'Cambiando la configuración en el menú de perfil', 'Usando un interruptor para alternar entre las versiones nueva y clásica', 'Instalando diferentes versiones de la aplicación', 'La versión no se puede cambiar', 'b) Usando un interruptor para alternar entre las versiones nueva y clásica'], ['¿Cuál es el propósito de la bandeja de entrada de Yammer?', 'Organizar, leer y responder mensajes', 'Almacenar archivos y documentos', 'Personalizar la configuración del usuario', 'Administrar membresías de grupo', 'a) Organizar, leer y responder mensajes'], ['¿Cómo se envía un mensaje privado en Yammer?', 'A través del feed principal', 'Usando el botón Nuevo mensaje privado', 'Etiquetando a un usuario en una publicación pública', 'A través de la pestaña Archivos', 'b) Usando el botón Nuevo mensaje privado'], ['¿Qué función se utiliza para administrar y organizar mensajes en Yammer?', 'La pestaña Comunidades', 'El directorio de archivos', 'Las herramientas de administración de bandeja de entrada', 'La configuración del perfil', 'c) Las herramientas de administración de bandeja de entrada'], ['¿Cómo se puede responder a mensajes en Yammer?', 'Creando una nueva publicación en el feed', 'Usando el botón Comentar debajo de un mensaje', 'A través de la aplicación de escritorio de Yammer solamente', 'Enviando un correo electrónico', 'b) Usando el botón Comentar debajo de un mensaje'], ['¿Cuál es un método para marcar mensajes como leídos o no leídos en Yammer?', 'A través de la configuración de Office 365', 'Usando un icono de marca de verificación en la bandeja de entrada', 'Abriendo cada mensaje individualmente', 'Esta función no está disponible en Yammer', 'b) Usando un icono de marca de verificación en la bandeja de entrada'], ['¿Cómo se actualiza tu perfil de Yammer?', 'Enviando un correo electrónico al equipo de soporte de Yammer', 'Usando el enlace Editar configuración en el panel de configuración', 'A través de la pestaña Comunidades', 'No se permiten actualizaciones de perfil', 'b) Usando el enlace Editar configuración en el panel de configuración'], ['¿Cuál es la función del lanzador de aplicaciones en Yammer Web 2020?', 'Cerrar la aplicación Yammer', 'Navegar a otras aplicaciones de Office', 'Cambiar la configuración del idioma', 'Editar perfiles de usuario', 'b) Navegar a otras aplicaciones de Office']]
# # print(type(data))

# # import json
# # llmResponseJSON = json.loads(data)
# # print(f"\nSTEP3: llmResponseJSON: {llmResponseJSON}")

# # import pandas as pd
# # dataFrame = pd.DataFrame(data)
# # print(f"\nDataFrame: {dataFrame}")



# import pandas as pd

# # String representation of the list
# data_str = "[['Fragen', 'A', 'B', 'C', 'D', 'Korrekte Antworten'], ['Wie greifen Sie in Yammer Web 2020 auf Yammer zu?', 'Über die Yammer-Desktop-Anwendung', 'Mit einer Firmen-E-Mail-Adresse und Zugriff über Office 365', 'Durch Herunterladen der Yammer-App auf einem Mobilgerät', 'Über einen direkten Link in einer E-Mail', 'b) Mit einer Firmen-E-Mail-Adresse und Zugriff über Office 365'], ['Was kann in Ihrem Yammer-Profil angepasst werden?', 'Ihr Netzwerk und Gruppenmitgliedschaften', 'Interessen, Fachkenntnisse, Berufserfahrung, Profilbild und Geburtstag', 'Das Layout des Yammer-Feeds', 'Das Design der Yammer-Oberfläche', 'b) Interessen, Fachkenntnisse, Berufserfahrung, Profilbild und Geburtstag'], ['Wie navigieren Sie zwischen verschiedenen Versionen von Yammer?', 'Durch Ändern der Einstellungen im Profilmenü', 'Mit einem Umschalter zwischen den neuen und klassischen Versionen', 'Durch Installieren verschiedener Versionen der Anwendung', 'Die Version kann nicht geändert werden', 'b) Mit einem Umschalter zwischen den neuen und klassischen Versionen'], ['Was ist der Zweck des Yammer-Posteingangs?', 'Nachrichten zu organisieren, lesen und beantworten', 'Dateien und Dokumente zu speichern', 'Benutzereinstellungen anzupassen', 'Gruppenmitgliedschaften zu verwalten', 'a) Nachrichten zu organisieren, lesen und beantworten'], ['Wie senden Sie eine private Nachricht in Yammer?', 'Über den Haupt-Feed', 'Mit der Schaltfläche Neue private Nachricht', 'Indem Sie einen Benutzer in einem öffentlichen Beitrag markieren', 'Über die Registerkarte Dateien', 'b) Mit der Schaltfläche Neue private Nachricht'], ['Welche Funktion wird verwendet, um Nachrichten in Yammer zu verwalten und zu organisieren?', 'Die Registerkarte Communities', 'Das Dateiverzeichnis', 'Die Posteingangsverwaltungstools', 'Die Profileinstellungen', 'c) Die Posteingangsverwaltungstools'], ['Wie können Sie auf Nachrichten in Yammer antworten?', 'Indem Sie einen neuen Beitrag im Feed erstellen', 'Mit der Schaltfläche Kommentar unter einer Nachricht', 'Nur über die Yammer-Desktop-Anwendung', 'Durch Senden einer E-Mail', 'b) Mit der Schaltfläche Kommentar unter einer Nachricht'], ['Wie markiert man Nachrichten als gelesen oder ungelesen in Yammer?', 'Über die Office 365-Einstellungen', 'Mit einem Häkchen-Symbol im Posteingang', 'Indem man jede Nachricht einzeln öffnet', 'Diese Funktion ist in Yammer nicht verfügbar', 'b) Mit einem Häkchen-Symbol im Posteingang'], ['Wie aktualisieren Sie Ihr Yammer-Profil?', 'Indem Sie das Yammer-Support-Team per E-Mail kontaktieren', 'Mit dem Link Einstellungen bearbeiten im Einstellungsbereich', 'Über die Registerkarte Communities', 'Profilaktualisierungen sind nicht zulässig', 'b) Mit dem Link Einstellungen bearbeiten im Einstellungsbereich'], ['Was ist die Funktion des App-Starters in Yammer Web 2020?', 'Um die Yammer-Anwendung zu schließen', 'Zur Navigation zu anderen Office-Anwendungen', 'Um Spracheinstellungen zu ändern', 'Zum Bearbeiten von Benutzerprofilen', 'b) Zur Navigation zu anderen Office-Anwendungen']]"

# # Convert the string to a list
# data_list = eval(data_str)

# # Extract column names (header) and data
# columns = data_list[0]
# data = data_list[1:]

# # Create a Pandas DataFrame
# df = pd.DataFrame(data, columns=columns)

# # Display the DataFrame
# print(df)




import streamlit as st
import pandas as pd
from docx import Document

# Title for the Streamlit app
st.title("File Upload Example")

# File uploader widget
uploaded_file = st.file_uploader("Upload a CSV or DOCX file", type=["csv", "xlsx", "docx"])

# Check if a file is uploaded
if uploaded_file is not None:
    # Display the uploaded file name
    st.write("Uploaded file:", uploaded_file.name)

    # Read the file and display its content
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(df.head())
        # Your further processing logic for CSV files here
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.write("Data Preview:")
        st.write(df.head())
        # Your further processing logic for Excel files here
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document = Document(uploaded_file)
        paragraphs = [paragraph.text for paragraph in document.paragraphs]
        st.write("Text Content:")
        for paragraph in paragraphs:
            st.write(paragraph)
        # Your further processing logic for Word files here
    else:
        st.warning("Unsupported file format. Please upload a CSV, Excel, or Word file.")
else:
    st.info("Please upload a file.")