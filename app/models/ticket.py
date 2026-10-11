from app.enums.ticket_status import TicketStatus
from app.exceptions.ticket_exceptions import InvalidTicketStatusTransitionError


class Ticket:
    def __init__(self, title: str, description: str) -> None:
        self.title = title
        self.description = description
        self.status = TicketStatus.OPEN

    def get_summary(self) -> str:
        return f"{self.title} - {self.description}"

    def start_progress(self) -> None:
        if self.status != TicketStatus.OPEN:
            raise InvalidTicketStatusTransitionError(f"Cannot start progress from status '{self.status.value}'. "
            "Ticket must be 'open'.")
        self.status = TicketStatus.IN_PROGRESS

    def resolve(self) -> None:
        if self.status != TicketStatus.IN_PROGRESS:
            raise InvalidTicketStatusTransitionError(f"Cannot resolve ticket from status '{self.status.value}'. "
            "Ticket must be 'in_progress'.")
        self.status = TicketStatus.RESOLVED