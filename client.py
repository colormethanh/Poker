from network import Network
import pygame
import sys
pygame.font.init()

pygame.init()

width = 1280
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_num = 0


def redrawWindow(window, game):
    window.fill((255, 255, 255))
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Hello!", 1, (255, 0, 0), True)
    window.blit(text, (0, 0))
    btn.draw(window)
    if len(game.action_log) > 3:
        ct = 0
        for item in game.action_log[:3]:
            font = pygame.font.SysFont("comicsans", 20)
            text = font.render(item, True, (0, 0, 0))
            text_rect = text.get_rect()

            pos = (text.get_height() * ct)
            text_rect.center = (window.get_width()//2, window.get_height()//2 - pos)
            window.blit(text, text_rect)

            if ct == 3:
                ct = 0
            else:
                ct += 1

    pygame.display.update()


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2),
                           self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]

        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False


btn = Button("click me!", 500, 500, (0, 0, 255))


def main():

    clock = pygame.time.Clock()
    run = True

    n = Network()
    p_num = n.get_player()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos):
                    print("clicked")
                    n.send_data("clicked")

        game = n.send_data("get")
        redrawWindow(window, game)


main()
