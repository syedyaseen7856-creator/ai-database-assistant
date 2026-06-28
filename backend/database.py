from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///database/company.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    salary = Column(Float)


def create_database():
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()

    if session.query(Employee).count() == 0:

        employees = [
            Employee(name="Rahul", department="IT", salary=65000),
            Employee(name="Priya", department="HR", salary=55000),
            Employee(name="Arjun", department="Finance", salary=70000),
            Employee(name="Sneha", department="IT", salary=72000),
            Employee(name="Kiran", department="Sales", salary=60000),
        ]

        session.add_all(employees)
        session.commit()

    session.close()


if __name__ == "__main__":
    create_database()
    print("Database Created Successfully")