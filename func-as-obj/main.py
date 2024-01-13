import os.path
import sys

from database import report_data
from report_builder import (
    generate_csv_report,
    generate_txt_report,
    generate_json_report,
    generate_yaml_report,
)


def generate_report(filepath: str):
    """
    Generates a report and saves it to the specified file path,
    with the format determined by the file extension.

    :param filepath: The file path where the report will be saved.
    """

    basename, ext = os.path.splitext(filepath)
    ext = ext.lower()

    # TODO: Implement other formats
    if ext == ".csv":
        generate_csv_report(
            filepath=filepath,
            data=report_data,
        )

    if ext == ".txt":
        generate_txt_report(
            filepath=filepath,
            data=report_data,
    )

    if ext == ".json":
        generate_json_report(filepath=filepath, data=report_data)


def main(*args):
    try:
        filepath = input("Report filename (path): ")
        generate_report(filepath)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        sys.stderr.write(f"{e}\n")
        sys.stderr.flush()
        return 255
    else:
        print(
            f"The file was successfully saved to\n"
            f"{os.path.abspath(filepath)}"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv))
