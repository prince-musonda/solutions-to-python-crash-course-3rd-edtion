favourite_places = {
    'john': ['new york city','paris','london'],
    'sizwayo':['lusaka','manchester','london','new york city'],
    'prince':['new york city','london','rome','silicon valley','delhi','tokyo'],
    'melvin':['bervery hills']
}


for person, places in favourite_places.items():
    if len(places) > 1:
        print(f"\n{person.title()}'s favourite places are:")
        for place in places:
            print('\t'+place.title())
    else:
        print(f"\n{person.title()}'s favourite place is {places[0].title()}")