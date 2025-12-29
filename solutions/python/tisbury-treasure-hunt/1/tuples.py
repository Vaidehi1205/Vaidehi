"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    co = record[1]
    return co

def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    tr = tuple(coordinate)
    return tr

def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    co = tuple(azara_record[1])
    if co in rui_record:
        return True
    else:
        return False

    pass


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    co = tuple(azara_record[1])
    if co in rui_record:
        cm = azara_record + rui_record
        return cm
    else:
        return "not a match"    



def clean_up(combined_record_group):
    cleaned = []
    for rec in combined_record_group:
        # remove the second element
        new_rec = (rec[0], rec[2], rec[3], rec[4])
        cleaned.append(str(new_rec))
        
    # Join with a SINGLE newline, and add ONE newline at the end
    return "\n".join(cleaned) + "\n"
