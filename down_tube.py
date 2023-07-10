import pytube

while True:
    try:
        formato = input("Seleccione formato mp3/mp4 o salir: ")
        
        if formato == "salir":
            break

        URL_STRING = input("Ingrese la url: ")

        LIST_OF_URL = URL_STRING.split()

        LIST_OF_URL = [url for url in LIST_OF_URL if url.strip()]  # Eliminar elementos vacios
    
        for url in LIST_OF_URL:
            video = pytube.YouTube(url)

            if formato == "mp4":
                video.streams.filter(file_extension="mp4").first().download()
                print("Su video se está descargando")

            elif formato == "mp3":
                audio = video.streams.filter(only_audio=True).first()
                audio.download()
                print("Su audio se está descargando")
                
            else:
                print("Ingrese un formato válido (mp3 o mp4)")
        
    except Exception as e:
        print("Hubo un problema con el link/links pasado:", str(e))
