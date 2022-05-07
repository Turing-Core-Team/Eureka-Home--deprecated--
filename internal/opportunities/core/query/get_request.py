class GetRequest:
    __description: str
    __tags: str

    def __init__(self, description: str, tags: str):
        self.__description = description
        self.__tags = tags

    def get_description(self) -> str:
        return self.__description

    def get_tags(self) -> str:
        return self.__tags
