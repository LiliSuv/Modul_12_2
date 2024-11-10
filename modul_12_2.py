from unittest import TestCase
import pprint
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
    def run(self):
        self.distance += self.speed * 2
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if isinstance (other, str):
            return self.name == other
        elif isinstance (other, Runner):
            return self.name == other.name
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list (participants)
    def start(self):
        finishers = {}
        finisher = {}
        while self.participants:
            for participant in self.participants:
                participant.run ()
                if participant.distance >= self.full_distance:
                    finisher[1 / participant.speed] = participant
                    finishers = dict (sorted (finisher.items ()))
                    m = []
                    for key in finishers.keys ():
                        m.append (finishers[key])
                    finishers = {i: k for i, k in enumerate (m, 1)}
                    self.participants.remove (participant)
        return finishers


class TournamentTest (TestCase):
    def setUp(self):
        self.rur_1 = Runner ('Усэйн', 10)
        self.rur_2 = Runner ('Андрей', 15)
        self.rur_3 = Runner ('Ник', 8)
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items ():
            pprint.pprint (f' {test_key}')
            for key, value in test_value.items ():
                pprint.pprint (f'{key}: {value.name}')

    def test_tur_1(self):
        tur_1 = Tournament (90, self.rur_1, self.rur_3)
        m={}
        for par in tur_1.participants:
            m.update ({par.name: par.speed})
            a=min(m,key=m.get)
        result = tur_1.start ()
        self.assertTrue (result[max (result)] == a)
        self.all_results['Первый забег'] = result

    def test_tur_2(self):
        tur_2 = Tournament (90, self.rur_2, self.rur_3)
        m = {}
        for par in tur_2.participants:
            m.update ({par.name: par.speed})
            a = min (m, key=m.get)
        result = tur_2.start ()
        self.assertTrue (result[max (result)] == a)
        self.all_results['Второй забег'] = result

    def test_tur_3(self):
        tur_3 = Tournament (40, self.rur_1, self.rur_2, self.rur_3)
        m = {}
        for par in tur_3.participants:
            m.update ({par.name: par.speed})
            a = min (m, key=m.get)
        result = tur_3.start ()
        self.assertTrue (result[max (result)] == a)
        self.all_results['Третий забег'] = result

    def test_tur_4(self):
        tur_1 = Tournament (90, self.rur_1, self.rur_3)
        m = {}
        for par in tur_1.participants:
            m.update ({par.name: par.speed})
            a = max (m, key=m.get)
        result = tur_1.start ()
        self.assertTrue (result[min (result)] == 'Усэйн')

    def test_tur_5(self):
        tur_2 = Tournament (90, self.rur_2, self.rur_3)
        m = {}
        for par in tur_2.participants:
            m.update ({par.name: par.speed})
            a = max (m, key=m.get)
        result = tur_2.start ()
        self.assertTrue (result[min (result)] == a)

    def test_tur_6(self):
        tur_3 = Tournament (30, self.rur_1, self.rur_2, self.rur_3)
        m = {}
        for par in tur_3.participants:
            m.update ({par.name: par.speed})
            a = max (m, key=m.get)
        result = tur_3.start ()
        self.assertTrue (result[min (result)] == a)
