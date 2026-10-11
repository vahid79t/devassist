from app.models.ticket import Ticket
from app.exceptions.ticket_exceptions import InvalidTicketStatusTransitionError


def main() -> None:
    print("DevAssist is starting...")

    title = "Kubernetes pod is restarting"

    description = "The pod enters CrashLoopBackOff after deployment."
    ticket = Ticket(title, description)
    print(ticket.get_summary())
    print(ticket.status)
    print(ticket.status.name)
    print(ticket.status.value)
    ticket.start_progress()
# Previous test:
# Calling start_progress() twice raises InvalidTicketStatusTransitionError.
#
# try:
#     ticket.start_progress()
# except InvalidTicketStatusTransitionError as error:
#     print(error)
    print("Program continues...")
    print(ticket.status.value)
    ticket.resolve()
    print(ticket.status.value)
    ticket2 = Ticket("test2", "for testing")
    try:
        ticket2.resolve()
    except InvalidTicketStatusTransitionError as error:
        print(error)


if __name__ == "__main__":
    main()
    
