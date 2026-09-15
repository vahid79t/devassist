class Ticket:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description

    def get_summary(self) -> str:
        return f"{self.title} - {self.description}"
