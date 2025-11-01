def get_rag_response(message: str, file_content: str):

    if not file_content:
        return f"Respuesta generada solo con el mensaje: '{message}'."
    else:
        resumen = file_content[:200].replace("\n", " ")
        return (
            f"Mensaje: '{message}'. He analizado el archivo, que contiene este extracto: "
            f"'{resumen}...'"
        )
