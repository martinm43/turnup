# coding: utf-8
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()
    class Meta:
        database=db
        
from peewee import *
db = SqliteDatabase('people.db')
class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()
    class Meta:
        database=db
        
        
class Pet(Model):
    owner=ForeignKeyField(Person, related_name='pets')
    name=CharField()
    animal_type=CharField()
    class Meta:
        database=db
        
db.create_tables([Person,Pet])
get_ipython().magic(u'ls')
from datetime import date
uncle_bob=Person(name='Bob',birthday=date(1960,1,15),is_relative=True)
uncle_bob.save()
grandma=Person.create(name='Grandma',birthday=date(1935,3,1),is_relative=True)
herb=Person.create(name='Herb',birthday=(1950,5,5),is_relative=False)
herb=Person.create(name='Herb',birthday=(1950,5,5),is_relative=False)
herb=Person.create(name='Herb', birthday=(1950,5,5), is_relative=False)
herb=Person.create(name='Herb',birthday=date(1950,5,5),is_relative=False)
grandma.name = 'Grandma L.'
grandma.save()
bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
bob_kitty.save()
herb_fido.save()
herb_mittens.save()
herb_mittens_jr.save()
her_mittens.delete_instance()
herb_mittens.delete_instance()
herb_fido.owner=uncle_bob
herb_fido.save()
bob_fido=herb_fido
grandma=Person.select().where(Person.name=='Grandma L.').get()
grandma
grandma=Person.get(Person.name=='Grandma L.')
grandma
for person in Person.select():
    print person.name, person.is_relative
    