import xlrd
import re
from sqlalchemy import Unicode, Integer, ForeignKey, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, backref

Base = declarative_base()

class Switch(Base):
    __tablename__ = "switch"
    id = Column(Integer, primary_key=True)
    hostname = Column(Unicode, index=True)
    ip = Column(Unicode)
    model = Column(Unicode)
    #switchports = relationship('SwitchPort', back_populates='switch')
    switchports = relationship('SwitchPort', backref='switch')


class SwitchPort(Base):
    __tablename__ = "switchport"
    id = Column(Integer, primary_key=True)
    port = Column(Unicode)
    ip = Column(Unicode)
    duplex = Column(Unicode)
    speed = Column(Integer)
    switch_hostname = Column(Unicode,
                         ForeignKey('switch.hostname'),
                         index=True,
                       nullable=False)
    # switch = relationship(Switch,
    #                       backref='switch_name',
    #                       uselist=True)
    #switch = relationship(Switch, back_populates='switchports')




wb = xlrd.open_workbook('switch.xlsx')
sheet = wb.sheet_by_index(0)
info_line = re.compile('Host')
switchport_line = re.compile(r'\d/\d+|\d/\d/\d+')
switch_hostname = re.compile(r'Host: (?P<hostname>\w+)'
                             ' ip: (?P<ip>\d+\.\d+\.\d+\.\d+)'
                             ' type: (?P<model>\w+)')

engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
s = Session()

for row in sheet.get_rows():
    if info_line.search(str(row)):
        print(row)
        result = switch_hostname.match(str(row[1].value))
        new_machine = Switch(hostname = result.group('hostname'),
                             ip = result.group('ip'),
                             model = result.group('model'))
        s.add(new_machine)
    elif switchport_line.search(str(row)):
        print(row)
        new_switchport = SwitchPort(port = row[1].value,
                                    ip = row[2].value,
                                    duplex = row[3].value,
                                    speed = row[4].value,
                                    switch_hostname = new_machine.hostname
                                    )
        s.add(new_switchport)
    s.commit()
        #s.refresh(new_machine)

print('Querying Switch table')
s.query(Switch).all()
print('Querying SwitchPort table')
s.query(SwitchPort).all()


