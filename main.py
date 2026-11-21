from app.models.ticket import Ticket
from app.enums.ticket_priority import TicketPriority


def main() -> None:
    print("DevAssist is starting...")

    title = "Kubernetes pod is restarting"
    description = "The pod enters CrashLoopBackOff after deployment."

    ticket1 = Ticket(title, description, priority=TicketPriority.LOW)

    print("Ticket 1:")
    print(ticket1.priority.value)

    ticket2 = Ticket(
        "Production is down",
        "All users are affected.",
    )

    print("Ticket 2:")
    print(ticket2.priority.value)

    ticket3 = Ticket(
        "Production is not available ",
        "All users are affected.",
        priority=TicketPriority.HIGH,
    )

    print("Ticket 3:")
    print(ticket3.priority.value)

    ticket4 = Ticket(
        "Production is inprogress ",
        "All users are affected.",
        priority=TicketPriority.CRITICAL,
    )

    print("Ticket 4:")
    print(ticket4.priority.value)
    print(ticket4.category,ticket4.id,ticket4.created_at)
    print(ticket4.created_at.year)
    print(ticket4.created_at.month)
    print(ticket4.created_at.day)
    print(ticket4.created_at.hour)
    print(ticket4.created_at.minute)
    print(ticket4.created_at.second)

if __name__ == "__main__":
    main()