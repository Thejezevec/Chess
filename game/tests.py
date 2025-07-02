from django.test import TestCase

# Create your tests here.

class GameModelTest(TestCase):
    def setUp(self):
        # Set up initial data for the tests
        self.game = Game.objects.create(
            player_white='Whalter',
            player_black='Jack',
            board_state='initial_state'
        )

    def test_game_creation(self):
        # Test if the game is created correctly
        self.assertEqual(self.game.player_white, 'Walter')
        self.assertEqual(self.game.player_black, 'Jack')
        self.assertFalse(self.game.is_draw)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.game.board_state, 'initial_state')

    def test_str_representation(self):
        # Test the string representation of the game
        self.assertEqual(str(self.game), 'game Walter vs Jack')