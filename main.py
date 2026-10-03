from app.models.ticket import Ticket


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
    print(ticket.status.value)
    ticket.resolve()
    print(ticket.status.value)

    
if __name__ == "__main__":
    main()
    
