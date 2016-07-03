import xlrd
import re
from sqlalchemy import Unicode, Integer, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Ip(Base):
    __tablename__ = "ip"
    id = Column(Integer, primary_key=True)
    hostname = Column(Unicode, index=True)
    ip = Column(Unicode)
    area = Column(Unicode)


wb = xlrd.open_workbook('ips.xlsx')
sheet = wb.sheet_by_index(0)

engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()

ip = re.compile('\d+\.\d+\.\d+\.\d+')

for row in sheet.get_rows():
    if ip.search(str(row[0].value)):
        print(row)
        new_ip = Ip(ip = row[0].value,
                    hostname = row[1].value,
                    area = row[2].value,
                    )
        s.add(new_ip)
    s.commit()
        #s.refresh(new_machine)

print('Querying Switch table')
s.query(Ip).all()


