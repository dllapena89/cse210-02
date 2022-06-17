from game.card import Card

class Director:
    """A person who directs the game
    
    The responsability of the Director is to control the sequence of play
    
    Attributes:
        Card (Card): One instance of the Card class
        second_card (Card): One instanceof the Card class
        is_playing (boolean): Wheter or not the game is being played.
        overall_score (int): The score for the entire game.
        guess (string): PLayer input guessing if it is higher or lower the next cards value
        """

    def __init__(self):
         """Constructs a new Director.
         Args:
            self (Director): an instance of Director.
         """
         self.card = Card()
         self.second_card = Card()
         self.is_playing = True
         self.overall_score = 300
         self.guess = ""

         

        

    def start_game(self):
         """Starts the game by running the main game loop.
        
         Args:
            self (Director): an instance of Director.
         """
         while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
         """Ask the user if to guess teh value of the next card.

         Args:
            self (Director): An instance of Director.
         """
         if (self.card.value == 0):
            self.card.draw()

         print(f"The card is: {self.card.value}")
         self.guess = (input(f"Higher or lower? [h/l]: "))
         self.second_card.draw()
         print(f"The card is: {self.second_card.value}")

    def do_updates(self):
        """Check the input, then updates teh overall score

        Args:
            self (Director): An instance of Director.
        """
        if ( self.guess == "h"):
            if self.card.value < self.second_card.value:
                self.overall_score += 100
            else:
                self.overall_score -= 75

        elif (self.guess == "l"):
            if self.card.value > self.second_card.value:
                self.overall_score += 100
            else:
                self.overall_score -= 75

        self.card.value = self.second_card.value

        if self.overall_score <= 0:
            self.is_playing = False 
            print ("You lose, Game Over")

    def do_outputs(self):
         """Displays the score. Also asks the player if they want play again. 

         Args:
            self (Director): An instance of Director.
        
         """
         if not self.is_playing:
            return
        
         print(f"Your score is: {self.overall_score}")
         again = input("Do you want to play again?(y/n): ")
         if again == "n":
            print("Ok, see you next time.")
            self.is_playing = False

