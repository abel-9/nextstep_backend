# Interfaces
from src.core.interfaces import IDatabase, IVectorDB, IMediator, IMessageBroker


class AppContainer:
    def __init__(self):
        self.database: IDatabase | None = None
        self.vector_db: IVectorDB | None = None
        self.mediator: IMediator | None = None
        self.message_broker: IMessageBroker | None = None

    def set_database(self, database: IDatabase):
        if self.database is not None:
            raise Exception("Database is already set")
        self.database = database

    def set_vector_db(self, vector_db: IVectorDB):
        if self.vector_db is not None:
            raise Exception("VectorDB is already set")
        self.vector_db = vector_db

    def set_mediator(self, mediator: IMediator):
        if self.mediator is not None:
            raise Exception("Mediator is already set")
        self.mediator = mediator

    def set_message_broker(self, message_broker: IMessageBroker):
        if self.message_broker is not None:
            raise Exception("MessageBroker is already set")
        self.message_broker = message_broker
