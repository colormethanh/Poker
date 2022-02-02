from network import Network
import pygame
import sys
import os
pygame.font.init()


def redrawWindow(window, game, player_obj, sel_btn_grp):
    """ a Function that redraws the screen of the game """

    window.fill((255, 255, 255))

    # initializing game sections
    poker_tbl_area.draw(window)
    player_info_area.draw(window)
    move_log_area.draw(window)
    selection_area.draw(window)
    otherP_info_area.draw(window)
    ready_btn.draw(window)

    # assigning button colors depending on if it's their turn or not
    if not player_obj.turn:
        for btn in sel_btn_grp:
            btn.color = (142, 142, 142)
            btn.draw(window)
    else:
        for btn in sel_btn_grp:
            if player_obj.choices[btn.text] == 'on':
                btn.color = (0, 255, 0)
            else:
                btn.color = (142, 142, 142)
            btn.draw(window)

    # Log system
    log_box = Box("",
                  40,
                  move_log_area.y,
                  (64, 189, 93),
                  move_log_area.width - 80,
                  move_log_area.height
                  )
    log_box.draw(window)

    if game.action_log:
        ct = 0

        for item in game.action_log[:10]:

            font = pygame.font.SysFont("comicsans", 20)
            text = font.render(item, True, (0, 0, 0))
            log_pos = (text.get_height() * ct)
            text_rect = text.get_rect(topleft=(log_box.x + (log_box.width * .1),
                                               log_box.y + 15 + (log_pos * 1.5)
                                               )
                                      )
            window.blit(text, text_rect)

            if ct == 10:
                ct = 0
            else:
                ct += 1

    # Prints player hand if hand has cards
    if player_obj.hand:
        ct = 0
        for c in player_obj.hand:
            card_code = f"{c[0]}_{c[1]}"
            image_path = os.path.join(dirname, f'pixel_cards\\{card_code}.png')
            card = pygame.image.load(image_path)
            window.blit(card, ((card.get_width()+2) * ct, 0))
            ct += 1

    # Printing community_cards
    if game.community_cards:
        pass

    pygame.display.update()


class Box:
    """ A class that creates a button that can be clicked """

    def __init__(self, text, x, y, color, width=150, height=40):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

    # Draws a the button box and text
    def draw(self, window):
        """ Draws the button retangle and text """
        # Creating and draws a retangle at certain x, y cords
        pygame.draw.rect(window,
                         self.color,
                         (self.x, self.y, self.width, self.height)
                         )

        # creates a text object
        font = pygame.font.SysFont("comicsans", 25)
        text = font.render(self.text, 1, (255, 255, 255))

        # draws the text object onto cords that are the center of the retangle
        window.blit(text,
                    (self.x + round(self.width/2) - round(text.get_width()/2),
                     self.y + round(self.height/2) - round(text.get_height()/2)
                     )
                    )

    # returns true or false if button was clicked
    def click(self, pos):
        """ This funtion returns true or false if the button was clicked """

        x1 = pos[0]
        y1 = pos[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


class Screen_div:
    """ A class that creates section seperators for the game UI """

    def __init__(self, text, x, y, width, height, color):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, window):
        """ Draws the rectangle that will be the section """
        pygame.draw.rect(window,
                         self.color,
                         (self.x, self.y, self.width, self.height)
                         )

        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                           self.y + round(self.height/2) - round(text.get_height()/2)))


poker_tbl_area = Screen_div("Poker Table Area", 768, 0, 512, 720, (0, 255, 0))
player_info_area = Screen_div("Player info area", 0, 0, 768, 240, (70, 130, 180))
move_log_area = Screen_div("Move log area", 0, 240, 384, 240, (135, 206, 235))
otherP_info_area = Screen_div("Other Player info", 384, 240, 384, 240, (123, 104, 238))
selection_area = Screen_div("Selection Area", 0, 480, 768, 240, (176, 224, 230))

# Creating the btns selection area buttons
ready_btn = Box("Deal Cards", 500, 500, (0, 0, 255))  # throw away button
sel_btn_grp = []
ready_btn = Box("Ready",
                (selection_area.width / 2) + (ready_btn.width / 2),
                500,
                (255, 0, 0)
                )

fold_btn = Box("Fold",
               (selection_area.width / 5) - (ready_btn.width / 2),
               500,
               (0, 0, 255)
               )
sel_btn_grp.append(fold_btn)
check_btn = Box("Check",
                (selection_area.width/5) - (ready_btn.width / 2),
                (fold_btn.y + (fold_btn.height * 1.25)),
                (0, 0, 255)
                )
sel_btn_grp.append(check_btn)
raise_btn = Box("Raise",
                (selection_area.width/5) - (ready_btn.width / 2),
                (check_btn.y + (check_btn.height * 1.25)),
                (0, 0, 255)
                )
sel_btn_grp.append(raise_btn)
call_btn = Box("Call",
               (selection_area.width/5) - (ready_btn.width / 2),
               (raise_btn.y + (raise_btn.height * 1.25)),
               (0, 0, 255)
               )
sel_btn_grp.append(call_btn)


# Defining the dirpath to the card assets
dirname = os.path.dirname(__file__)
card_code = "card_back_red"
image_path = os.path.join(dirname, f'pixel_cards\\{card_code}.png')

# Defining and creating the display
width = 1280
height = 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def main():

    clock = pygame.time.Clock()
    run = True

    n = Network()
    p_num = n.get_player()
    print(f"You are player {p_num}")
    game = n.send_data("get")
    game.players_mstr[int(p_num) - 1].active = True

    while run:
        clock.tick(60)
        player_obj = game.players_mstr[int(p_num) - 1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            # checking for mouse button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # checks to see if the ready button was clicked
                if ready_btn.click(pos):
                    if not game.players_mstr[int(p_num) - 1].ready:
                        print("Ready")
                        game = n.send_data(ready_btn.text)
                        ready_btn.color = (0, 255, 0)
                        # redrawWindow(window, game, player_obj, sel_btn_grp)
                    elif game.players_mstr[int(p_num) - 1].ready:
                        pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for btn in sel_btn_grp:
                    if btn.click(pos):
                        print(btn.text, " was clicked")

        game = n.send_data("get")
        redrawWindow(window, game, player_obj, sel_btn_grp)


main()
