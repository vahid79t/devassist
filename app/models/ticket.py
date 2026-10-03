from app.enums.ticket_status import TicketStatus


class Ticket:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.status = TicketStatus.OPEN

    def get_summary(self) -> str:
        return f"{self.title} - {self.description}"

    def start_progress(self) -> None: 
        self.status = TicketStatus.IN_PROGRESS
    
    
    def resolve(self) -> None:
        self.status = TicketStatus.RESOLVED
  