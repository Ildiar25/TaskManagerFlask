from sqlalchemy import Column, Integer, String, Boolean, Date
from datetime import date
import db


class Task(db.Base):

    # Table settings
    __tablename__ = "todos"
    __table_args__ = {"sqlite_autoincrement": True}

    # Adding columns
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    complete = Column(Boolean, default=False)
    category = Column(String(50))
    created = Column(Date)

    # Starting the initializer
    def __init__(self, content: str, complete: bool, category: str, created: date) -> None:
        self.content = content
        self.complete = complete
        self.category = category
        self.created = created

    def __str__(self) -> str:
        # Is necessary to give a format to our date when is printed through the terminal because python will
        # print a memory object. That's why we need to use the method 'strftime()'.
        return (f"\nTarea #{self.id:03}:\n · Contenido: {self.content}\n · Terminada: {self.complete}\n"
                f" · Categoría: {self.category}\n · Creada: {self.created.strftime("%d/%m/%Y")}")
