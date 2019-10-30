from project.apps.database.database import Database
from project.apps.table.table import Table
from project.apps.table.customtypes.image import Image
from project.apps.table.customtypes.segment import Segment

# TODO: add type validation in the whole code (except table because it's already there)

# db = Database.create('newDB')
# db.addTable('keys', ['s', 'i'], ['segment', 'image'])
# db.tables['keys'].insert([
#     Segment(0, 1),
#     Image.create('C:\\Projects\\information-technologies-dbms-project\\tests\\table\\customtypes\\image.jpg')
# ])
# db.saveOnStorage()

db = Database.restore('C:\\Projects\\database\\newDB\\newDB.dbconfig')
db.tables['keys'].update(0, 's', Segment(-1, -2))
# db.tables['keys'].update(0, 'i', Image.create('C:\\Projects\\information-technologies-dbms-project\\testim.png'))
# newIm = Image.restore(db.tables['keys'].records[0][1].data)
# newIm.saveOnStorage('C:\\Projects\\information-technologies-dbms-project\\tests\\table\\customtypes', 'newIm', 'png')
db.saveOnStorage()
