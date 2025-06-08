import json


def open_txt_file(file_path: str) -> str:
    """
    opens and reads a file

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
    function opens/creates a text file and writes data to it

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


import json


def open_json_file(file_path: str) -> dict:
    """
    reads and parses a json file

    :param file_path: path to the json file
    :return: parsed json data as a dictionary
    :raises FileNotFoundError: if the file is not found
    :raises json.JSONDecodeError: if the file contains invalid json
    :raises Exception: for any other errors
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError as fne:
        raise FileNotFoundError(f"File not found: {fne}")
    except json.JSONDecodeError as jde:
        raise json.JSONDecodeError(f"Invalid JSON in file: {jde}")
    except Exception as e:
        raise Exception(f"Error reading JSON file: {e}")


def save_json_file(file_path: str, data: dict) -> None:
    """
    saves data to a JSON file

    :param file_path: path to the JSON file including filename
    :param data: dictionary with data to be saved
    :raises TypeError: if data is not JSON serializable
    :raises PermissionError: if no write permissions
    :raises Exception: if an error occurred while saving the file
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except TypeError as te:
        raise TypeError(f"Data is not JSON serializable: {te}")
    except PermissionError:
        raise PermissionError(f"No write permissions for: {file_path}")
    except Exception as e:
        print(f"Error with saving file:{e}")


def bytes_file_save(path: str, text: bytes) -> None:
    """
    saves binary data to file

    :param path: path to file
    :param text: binary data
    :return: None

    """
    try:
        with open(path, "wb") as file:
            file.write(text)
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File not found: {not_found}")
    except Exception as e:
        raise Exception(f"Can't write bytes in file {e}")


def bytes_file_read(path: str) -> bytes:
    """
    reads binary data from file
    :param path: path to file
    :return: binary data
    """
    try:
        with open(path, "rb") as file:
            return file.read()
    except FileNotFoundError as not_found:
        raise FileNotFoundError(f"File not found: {not_found}")
    except Exception as e:
        raise Exception(f"Can't read bytes from file {e}")
