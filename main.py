from app.models.ticket import Ticket

def main() -> None:
    print("DevAssist is starting...")

    title = "Kubernetes pod is restarting"

    description = "The pod enters CrashLoopBackOff after deployment."
    ticket = Ticket(title,description)
    print(ticket.title)
    print(ticket.description)


if __name__ == "__main__":
    main()

