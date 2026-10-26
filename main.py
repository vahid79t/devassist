from app.models.ticket import Ticket
from app.enums.ticket_priority import TicketPriority


def main() -> None:
    print("DevAssist is starting...")

    title = "Kubernetes pod is restarting"
    description = "The pod enters CrashLoopBackOff after deployment."

    ticket1 = Ticket(title, description)

    print("Ticket 1:")
    print(ticket1.get_summary())
    print(ticket1.priority)
    print(ticket1.priority.name)
    print(ticket1.priority.value)

    print()

    ticket2 = Ticket(
        "Production is down",
        "All users are affected.",
        priority=TicketPriority.HIGH,
    )

    print("Ticket 2:")
    print(ticket2.get_summary())
    print(ticket2.priority)
    print(ticket2.priority.name)
    print(ticket2.priority.value)


    ticket3 = Ticket(
        "Production is down ",
        "All users are affected.",
        priority=TicketPriority.Urgent,
    )

    print("Ticket 3:")
    print(ticket3.get_summary())
    print(ticket3.priority)
    print(ticket3.priority.name)
    print(ticket3.priority.value)

if __name__ == "__main__":
    main()