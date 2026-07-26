import re


def normalize_name_add_underscores(name: str):
    """
    Normalize a name by converting it to lowercase and adding underscores between words. Remove any non-alphanumeric characters.

    Args:
        name (str): The name to normalize.

    Returns:
        str: The normalized name.
    """
    # Convert to lowercase
    name = name.lower()

    # Replace non-alphanumeric characters with underscores
    normalized_name = "".join(char if char.isalnum() else "_" for char in name)

    # Remove leading and trailing underscores
    normalized_name = normalized_name.strip("_")

    # remove any multiple underscores found in same place
    normalized_name = re.sub(r"_+", "_", normalized_name)

    return normalized_name


def function_written_without_llms(name: str):
    """
    3_________2_9_1__import_related_attributes_on_module_objects

    to

    3_2_9_1_import_related_attributes_on_module_objects
    """
    new_str = ""

    underscore_added = False

    for idx, char in enumerate(name):
        # print(s, idx)
        if underscore_added and char == "_":
            continue

        new_str += char

        if char == "_":
            underscore_added = True
        else:
            underscore_added = False

    return new_str


if __name__ == "__main__":
    n = function_written_without_llms(
        "3_________2_9_1__import_related_attributes_on_module_objects"
    )
    print(n)

    a = normalize_name_add_underscores(
        "3_________2_9_1__import_related_attributes_on_module_objects"
    )
    print(a)
