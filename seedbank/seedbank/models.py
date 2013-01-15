from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    LargeBinary,
    String,
    Text,
    Unicode
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    relationship,
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension
from passlib.hash import pbkdf2_sha512 as pwhash
from datetime import datetime

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()
Base.id = Column(Integer, primary_key=True)


def setup_db(engine):
    Base.metadata.create_all(engine)


class Collection(Base):
    __tablename__ = "collections"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.id"))
    voucher_number = Column(Integer)
    species_id = Column(Integer, ForeignKey("species.id"))
    date_collected = Column(Date, nullable=False)
    location = Column(Unicode(255, collation="utf8"))
    longitude = Column(Float(precision=64))
    latitude = Column(Float(precision=64))
    altitude = Column(Float(precision=64))
    comments = Column(Text(convert_unicode=True))

    # Relationships
    images = relationship("Image")

    def __init__(self, user_id, trip_id, species_id, date_collected, location,
            longitude, latitude, altitude, comments):
        self.user_id = user_id
        self.trip_id = trip_id
        self.species_id = species_id
        self.date_collected = date_collected
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altiude
        self.comments = comments


class Species(Base):
    __tablename__ = "species"
    genus = Column(Unicode(255, collation="utf8"), nullable=False)
    species = Column(Unicode(255, collation="utf8"), nullable=False) 
    family = Column(Unicode(255, collation="utf8"), nullable=False)
    higher_taxonomy = Column(Unicode(255, collation="utf8"))

    # Relationships
    collections = relationship("Collection")
    
    def __init__(self, genus, species, family, higher_taxonomy):
        self.genus = genus
        self.species = species
        self.family = family
        self.higher_taxonomy = higher_taxonomy


class User(Base):
    __tablename__ = "users"
    username = Column(Unicode(255, collation="utf8"), nullable=False)
    given_name = Column(Unicode(255, collation="utf8"), nullable=False)
    family_name = Column(Unicode(255, collation="utf8"), nullable=False)
    email = Column(Unicode(255, collation="utf8"), nullable=False)
    initials = Column(Unicode(3, collation="utf8"), nullable=False) 
    create_date = Column(DateTime, nullable=False)
    hashed_password = Column(String(130), nullable=False)

    def check_password(self, raw_password):
        return pwhash.verify(raw_password, self.hashed_password)

    # Relationships
    collections = relationship("Collection")
    trips = relationship("Trip")
    images = relationship("Image")

    def __init__(self, username, given_name, family_name, email, password):
        self.username = username
        self.given_name = given_name
        self.family_name = family_name
        self.email = email
        self.create_datetime = datetime.now()
        self.hashed_password = pwhash.encrypt(password)  #Store Hashed password


class Trip(Base):
    __tablename__ = "trips"
    location = Column(Unicode(255, collation="utf8"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    log_data = Column(LargeBinary)
    collections = relationship("Collection")

    def __init__(self, location, start_date, end_date, log_data):
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.log_data = log_data


class Image(Base):
    __tablename__ = "images"
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False) 
    collection_id = Column(Integer, ForeignKey("collections.id"),
            nullable=False)
    file_name = Column(Unicode(255, collation="utf8"), nullable=False)
    image_content = Column(LargeBinary, nullable=False)

    def __init__(self, collection_id, file_name, image_content):
        self.collection_id = collection_id
        self.file_name = file_name
        self.image_content = image_content
