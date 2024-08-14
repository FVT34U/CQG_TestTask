class FileLoader:
    def __init__(self, path:str) -> None:
        self.path = path

    def get_content(self) -> str:
        content = ""

        with open(self.path, "r") as file:
            content = file.read()

        return content