# Usa la imagen oficial de Rasa
FROM rasa/rasa:latest

# Copia todo el contenido del proyecto al contenedor
COPY . /app

# Cambia el directorio de trabajo a /app
WORKDIR /app

# Entrena el modelo al construir la imagen
RUN rasa train

# Inicia el servidor de Rasa cuando el contenedor se ejecute
CMD ["run", "--enable-api", "--cors", "*", "-p", "5005"]
