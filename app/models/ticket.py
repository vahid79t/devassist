from app.enums.ticket_status import TicketStatus
from app.exceptions.ticket_exceptions import InvalidTicketStatusTransitionError
from app.enums.ticket_priority import TicketPriority
from app.enums.ticket_category import TicketCategory
from uuid import UUID, uuid4 ###this for generating id 
from datetime import datetime


class Ticket:
    def __init__(self, title: str, description: str, creator: str, priority: TicketPriority = TicketPriority.MEDIUM ,category: TicketCategory = TicketCategory.GENERAL, assignee: str | None = None ) -> None:
        self.title = title
        self.description = description
        self.status = TicketStatus.OPEN
        self.id: UUID = uuid4()
        self.creator = creator
        self.category = category
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()
        self.assignee = assignee
        if not isinstance(priority, TicketPriority):
            raise TypeError("priority must be a TicketPriority")
        self.priority = priority
       
    def get_summary(self) -> str:
        return f"{self.title} - {self.description}"

    def start_progress(self) -> None:
        
        if self.status != TicketStatus.OPEN:
            raise InvalidTicketStatusTransitionError(f"Cannot start progress from status '{self.status.value}'. "
            "Ticket must be 'open'.")
        self.status = TicketStatus.IN_PROGRESS
        self.updated_at = datetime.now()
    def resolve(self) -> None:
       
        if self.status != TicketStatus.IN_PROGRESS:
            raise InvalidTicketStatusTransitionError(f"Cannot resolve ticket from status '{self.status.value}'. "
            "Ticket must be 'in_progress'.")
        self.status = TicketStatus.RESOLVED
        self.updated_at = datetime.now()