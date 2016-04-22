from django.test import TestCase
from content.models import OurStory,OurTeam,OurStoryTitle
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class OurStoryTestCase(TestCase):
    def setUp(self):

        story1 = OurStory.objects.create(text="title 1", color="#ff0000",order=5)
        story2 = OurStory.objects.create(text="title 2",order=7)


    def test_story_have_text(self):
        """OurStory Test
            Fields tested : text,color
        """
        story1 = OurStory.objects.get(text="title 1")
        story2 = OurStory.objects.get(order=7)
        self.assertEqual(story1.text, 'title 1')
        # self.assertEqual(story2,None)

class OurTeamTestCase(TestCase):
    def setUp(self):

        team1 = OurTeam.objects.create(text="team 1", us_team="us_team_us_team_us_team_us_team",peru_team="peru_teamperu_team_peru_team",board_team="board_team")
        team2 = OurTeam.objects.create(text="team 2", us_team="team_us",peru_team="team_peru",board_team="team_board")


    def test_team_have_text(self):
        """OurStory Test
            Fields tested : text,color
        """
        team1 = OurTeam.objects.get(text="team 1")
        team2 = OurTeam.objects.get(text="team 2")
        self.assertEqual(team1.text, 'team 1')
        self.assertEqual(team2.us_team,'team_us')

class OurStoryTitleTestCase(TestCase):
    def setUp(self):

        storyTitle1 = OurStoryTitle.objects.create(title="LightandLeadership")

    def test_team_have_text(self):
        """OurStoryTitle Test
            Fields tested : title
        """
        storyTitle1 = OurStoryTitle.objects.get(title="LightandLeadership")
        self.assertNotEqual(storyTitle1.title, 'team 1')


class OurStoryViewTests(TestCase):
    def test_ourstory_index_page(self):
        response = self.client.get(reverse('content:our_story'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'No Story available')

class OurTeamViewTests(TestCase):
    def test_ourstory_index_page(self):
        response = self.client.get(reverse('content:our_team'))
        self.assertEqual(response.status_code, 200)
