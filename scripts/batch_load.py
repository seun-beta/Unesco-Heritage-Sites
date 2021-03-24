import csv 

from unesco.models import Site, Category, Region, Iso, State

def run():
    fhand = open('unesco/unesco.csv')
    reader = csv.reader(fhand)
    next(reader)

    Site.objects.all().delete()
    Category.objects.all().delete()
    Region.objects.all().delete() 
    Iso.objects.all().delete()
    State.objects.all().delete()

    for row in reader:

        category, created = Category.objects.get_or_create(name=row[7])
        state, created = State.objects.get_or_create(name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])
        iso, created = Iso.objects.get_or_create(name=row[10])

        
        try:
            n = str(row[0])
        except:
            n = None
        
        try:
            d = str(row[1])
        except:
            d = None
        
        try:
            j = str(row[2])
        except:
            j = None
        
        try:
            y = int(row[3])
        except:
            y = None

        try:
            lon = float(row[4])
        except:
            lon = None  

        try:
            lat = float(row[5])
        except:
            lat = None  

        if row[6]=="":
            a=None
        else:
            a = float(row[6])
      




        site= Site(name=n, description=d, justification=j, year=y, longitude=lon, latitude=lat, area_hectares=a, category=category, region=region, state=state, iso=iso)
        site.save()

        print('Done')