def open_txt_file(file_path: str) -> str:
    """
    Opens and reads a file.

    :param file_path: path to the file
    :return: content of the file as a string
    :raises FileNotFoundError: if the file is not found
    :raises Exception: if an error occurs while reading the file
    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as fne:
        raise FileNotFoundError(f"File not found: {fne}")
    except Exception as e:
        raise Exception(f"Error with reading file: {e}")


def save_txt_file(file_path: str, text: str) -> None:
    """
    The function opens/creates a text file and writes data to it.

    :param file_path: file directory
    :param text: data that will be written to the file
    :return: None
    :raises Exception: if an error occurs while saving the file
    """
    try:
        with open(file_path, mode="w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        raise Exception(f"Error with saving file: {e}")
