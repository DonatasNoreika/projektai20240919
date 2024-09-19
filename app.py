from models import engine, Projektas
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()

while True:
    veiksmas = int(input("1 - atvaizduoti\n2 - įvesti\n3 - pakeisti\n4 - ištrinti\n0 - išeiti\n"))
    match veiksmas:
        case 1:
            for projektas in session.query(Projektas).all():
                print(projektas)
        case 2:
            pavadinimas = input("Pavadinimas: ")
            kaina = float(input("Kaina: "))
            projektas = Projektas(pavadinimas, kaina)
            session.add(projektas)
            session.commit()
        case 3:
            for projektas in session.query(Projektas).all():
                print(projektas)
            projekto_id = int(input("Įveskite norimo pakeisti projekto ID: "))
            projektas_upd = session.get(Projektas, projekto_id)
            pavadinimas = input("Pavadinimas: ")
            kaina = float(input("Kaina: "))
            projektas_upd.name = pavadinimas
            projektas_upd.price = kaina
            session.commit()
        case 4:
            for projektas in session.query(Projektas).all():
                print(projektas)
            projekto_id = int(input("Įveskite norimo ištrinti projekto ID: "))
            projektas_del = session.get(Projektas, projekto_id)
            session.delete(projektas_del)
            session.commit()
        case 0:
            break