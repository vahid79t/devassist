from enum import Enum

class TicketCategory(Enum):

    GENERAL = "general"
    NETWORK = "network"
    SERVER = "server"
    KUBERNETES = "kubernetes"
    ACCESS = "access"