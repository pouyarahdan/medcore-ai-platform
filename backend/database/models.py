from sqlalchemy import Column, String, Float, DateTime

from backend.database.database import Base


class Analysis(Base):
    __tablename__ = "analyses"

    job_id = Column(String, primary_key=True, index=True)
    filename = Column(String)
    prediction = Column(String)
    confidence = Column(Float)
    status = Column(String)
    timestamp = Column(DateTime)