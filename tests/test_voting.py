from django.http.response import HttpResponse
from django.test import TestCase, Client
from django.utils import timezone
from voting.models import Project, Voting, VotingType, Group
from datetime import datetime, timedelta

from users.models import CustomUser

SOME_DATE = datetime.now(tz=timezone.utc)

class VT:
    MAJORITY = 'majority'
    APPROVAL = 'approval'
    BORDA = 'borda'
class VotingTest(TestCase):
    def __init__(self, *args, n_projects_each=5, n_users=5, **kwargs):
        super().__init__(*args, **kwargs)
        self.n_projects_each = n_projects_each
        self.n_users = n_users

    def create_voting(self, type, n_projects=None):
        if n_projects is None:
            n_projects = self.n_projects_each
        vt = VotingType.objects.create(name=type)
        start = SOME_DATE
        end = start + timedelta(days=30)
        g = Group.objects.create(name=f'{type}_group', description='...')
        v = Voting.objects.create(name=type, voting_type=vt, start_date=start, end_date=end, group=g)

        for i in range(n_projects):
            Project.objects.create(name=f'{type}_p{i}', description='...', budget=0, stage='?', finish_date=SOME_DATE, group=g, voting=v)


    def setUp(self):
        self.create_voting(VT.MAJORITY)
        self.create_voting(VT.APPROVAL)
        self.create_voting(VT.BORDA)
        self.users = [CustomUser.objects.create(username=f'u{i}') for i in range(self.n_users)]

    def user_vote(self, i, voting, choices) -> HttpResponse:
        u = self.users[i]
        c = Client()
        c.force_login(u)

        projects = Project.objects.filter(voting=voting)

        data = {
            'voting': voting.id,
            'choice': [{'project': p.id, 'points': c} for (p, c) in zip(projects, choices)]
        }
        res = c.post('/api/vote/', data=data, content_type='application/json')
        return res

    def _majority_for(self, k):
        return [1 if i == k else 0 for i in range(self.n_projects_each)]

    def _test_votes_legal(self, type, choices_data, expected_results):
        name = type
        v = Voting.objects.filter(name=name).first()
        assert v, f'Voting "{name}" does not exist'

        for i, ch in enumerate(choices_data):
            res = self.user_vote(i, v, ch)
            assert res.status_code == 200, f'Vote {ch} error code {res.status_code}: {res.content}'

        projects = Project.objects.filter(voting=v)

        for i, expected in enumerate(expected_results):
            pv = projects[i].votes
            assert pv == expected, f"Votes for project {i}: {pv} != {expected}"

    def _test_votes_illegal(self, type, choices_data):
        name = type
        v = Voting.objects.filter(name=name).first()
        assert v, f'Voting "{name}" does not exist'

        for i, ch in enumerate(choices_data):
            res = self.user_vote(i, v, ch)
            assert res.status_code != 200, f'Vote {ch} succeded, but shouldn\'t'

        results = [p.votes for p in Project.objects.filter(voting=v)]

        assert all(x == 0 for x in results), f'Results not all zero: {results}'

    def test_majority_ok(self):
        choices = [0, 4, 3, 1, 0]
        expected_results = [2, 1, 0, 1, 1]

        choices_data = [self._majority_for(x) for x in choices]
        self._test_votes_legal(VT.MAJORITY, choices_data, expected_results)

    def test_approval_ok(self):
        choices_data = [
            [1, 0, 1, 1, 1],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0],
        ]
        expected_results = [3, 0, 4, 2, 3]
        self._test_votes_legal(VT.APPROVAL, choices_data, expected_results)

    def test_borda_ok(self):
        choices_data = [
            [4, 3, 2, 1, 0],
            [0, 1, 2, 3, 4],
            [0, 3, 1, 4, 2],
            [4, 0, 1, 2, 3],
            [3, 1, 2, 4, 0],
        ]
        expected_results = [11, 8, 8, 14, 9]
        self._test_votes_legal(VT.BORDA, choices_data, expected_results)

    def test_majority_wrong(self):
        choices_data = [
            [ 0, 0, 0, 0, 0],
            [ 0, 1, 1, 0, 0],
            [ 2, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0]
        ]
        self._test_votes_illegal(VT.MAJORITY, choices_data)

    def test_approval_wrong(self):
        choices_data = [
            [ 0, 0, 0, 0, 0],
            [ 2, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0],
            [ 1, 1, 1, 1, 2]
        ]
        self._test_votes_illegal(VT.APPROVAL, choices_data)

    def test_borda_wrong(self):
        choices_data = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 2, 3],
            [1, 2, 3, 4, 5],
            [4, 3, 2, -1, 0],
            [4, 4, 4, 4, 4],
        ]
        self._test_votes_illegal(VT.BORDA, choices_data)