from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define the ORM model for your table
class PalabraSlang(Base):
    __tablename__ = 'palabras_slang'

    palabra = Column(String, primary_key=True)
    significado = Column(String)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)
def agregar_palabra():
    palabra = input("Ingrese la nueva palabra: ")
    significado = input("Ingrese el significado de la palabra: ")
    
    # Create a new PalabraSlang object
    nueva_palabra = PalabraSlang(palabra=palabra, significado=significado)
    
    # Add the new word to the session
    session.add(nueva_palabra)
    
    # Commit the changes to the database
    session.commit()
    
    print("Palabra agregada correctamente.")

def editar_palabra():
    palabra = input("Ingrese la palabra que desea editar: ")
    nuevo_significado = input("Ingrese el nuevo significado de la palabra: ")
    
    palabra_a_editar = session.query(PalabraSlang).filter_by(palabra=palabra).first()
    
    if palabra_a_editar:
        # Update the meaning
        palabra_a_editar.significado = nuevo_significado
        session.commit()
        print("Palabra editada correctamente.")
    else:
        print("Palabra no encontrada en el diccionario.")
