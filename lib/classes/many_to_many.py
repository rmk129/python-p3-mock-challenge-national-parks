import re
class NationalPark:

    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self._name == None:
            if isinstance(name, str) and len(name) >= 3:
                self._name = name

    def trips(self):
        all_trips = []
        for trips in Trip.all:
            if trips.national_park == self:
                all_trips.append(trips)
        return all_trips
    
    def visitors(self):
        all_visitors = set()
        for trips in Trip.all:
            if trips.national_park == self:
                all_visitors.add(trips.visitor)
        return list(all_visitors)
    
    def total_visits(self):
        visits = 0
        for trips in Trip.all:
            if trips.national_park == self:
                visits += 1
        return visits
    
    def best_visitor(self):
        all_trips = []
        for trips in Trip.all:
            if trips.national_park == self:
                all_trips.append(trips.visitor)
        return max(set(all_trips), key = all_trips.count)


class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7 and re.match(r"^\w+ \d+(st|nd|rd|th)$", start_date):
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7 and re.match(r"^\w+ \d+(st|nd|rd|th)$", end_date):
            self._end_date = end_date

class Visitor:

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) in range(1,16):
            self._name = name

    def trips(self):
        all_trips = []
        for trips in Trip.all:
            if trips.visitor == self:
                all_trips.append(trips)
        return all_trips
    
    def national_parks(self):
        all_parks = set()
        for trips in Trip.all:
            if trips.visitor == self:
                all_parks.add(trips.national_park)
        return list(all_parks)
    
    def total_visits_at_park(self, park):
        times = 0
        trips = []
        for trips in Trip.all:
            if trips.national_park == park:
                trips.append(trips)
        for trip in trips:
            if trip.visitor == self:
                times += 1
        return times