import json

from loguru import logger as log

from ..settings import Settings


class _Utility:
    def __init__(self):
        self.SETTINGS = Settings()

    def _motd(self):
        return "YEET"

    def _json_dump_file(self, data: dict, filename: str):
        """
        _json_dump_file dump json dict directly to a json file

        Args:
            data (dict): json data to dump to file
            filename (str): name of the file before .json
        """
        with open(f"{filename}.json", "w") as fp:
            log.debug(f"Dumping json data to {filename}.json")
            json.dump(data, filename, indent=4)
