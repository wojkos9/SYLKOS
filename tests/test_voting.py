from django.test import TestCase, Client
from django.utils import timezone
from voting.models import Project, Voting, VotingType, Group
from datetime import datetime, timedelta
import json

from users.models import CustomUser

SOME_DATE = datetime.now(tz=timezone.utc)

class VotingTest(TestCase):
    def setUp(self):
        vt = VotingType.objects.create(name='borda')
        start = SOME_DATE
        end = start + timedelta(days=30)
        g = Group.objects.create(name='group', description='...')
        v = Voting.objects.create(name='voting', voting_type=vt, start_date=start, end_date=end, group=g)

        for i in range(3):
            Project.objects.create(name=f'p{i}', description='...', budget=0, stage='?', finish_date=SOME_DATE, group=g, voting=v)

        self.users = [CustomUser.objects.create(username='u1')]

    def test_1(self):
        v = Voting.objects.filter(name='voting').first()
        assert v
        pp = Project.objects.filter(voting=v)
        assert pp.count() == 3
        choices = [2, 1, 0]
        data = {
            'voting': v.id,
            'choice': [{'project': p.id, 'points': c} for (p, c) in zip(pp, choices)]
        }
        c = Client()
        c.force_login(self.users[0])
        res = c.post('/api/vote/', data=data, content_type='application/json')
        print(res.content)