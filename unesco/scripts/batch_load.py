import csv
 
from unesco.models import Site, Category, Region, Iso, State

def run():
    fhand = open('unesco/unesco.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete() 
    Iso.objects.all().delete()
    State.objects.all().delete()

    for row in reader:
        print('-------------GOing--------------------')
        try:
            y = int(row[3])
        except:
            y = None

        category, created = Category.objects.get_or_create(name=row[7])


        state, created = State.objects.get_or_create(name=row[8])


        region, created = Region.objects.get_or_create(name=row[9])


        iso, created = Iso.objects.get_or_create(name=row[10])

        site= Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=row[4], latitude=row[5], area_hectares=row[6], category=category, region=region, state=state, iso=iso)
        site.save()
        print('Done')
