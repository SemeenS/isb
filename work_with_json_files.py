import json


def read_json_file(file_path: str) -> dict:
    """
    Reads and parses a json file.

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
    Saves data to a JSON file.

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
