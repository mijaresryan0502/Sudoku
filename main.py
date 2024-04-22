import pygame, sys
from constants import *
from board import Board

#Start screen and returns number of cells to be removed
def draw_game_start(screen):
    #Initialize Fonts
    start_title_font = pygame.font.Font(None, 100)
    subtitle_font = pygame.font.Font(None, 90)
    button_font = pygame.font.Font(None, 70)

    #Background color
    screen.fill(BG_COLOR)

    #Sets and draws title
    title_surface = start_title_font.render("Sudoku", 0, TEXT_COLOR)
    title_rect = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 200)
    )
    screen.blit(title_surface, title_rect)

    #Sets and draws subtitle
    subtitle_surface = subtitle_font.render("Select Difficulty", 0, TEXT_COLOR)
    subtitle_rect = subtitle_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2)
    )
    screen.blit(subtitle_surface, subtitle_rect)

    #Sets button and text
    easy_text = button_font.render("Easy", 0, TEXT_COLOR)
    medium_text = button_font.render("Medium", 0, TEXT_COLOR)
    hard_text = button_font.render("Hard", 0, TEXT_COLOR)

    #Sets button surface
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(BOX_COLOR)
    easy_surface.blit(easy_text, (10,10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(BOX_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(BOX_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    #Sets button rectangle
    easy_rectangle = easy_surface.get_rect(
        center = (WIDTH // 2 - 200, HEIGHT // 2 + 125)
    )
    medium_rectangle = medium_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 + 125)
    )
    hard_rectangle = hard_surface.get_rect(
        center = (WIDTH // 2 + 200, HEIGHT // 2 + 125)
    )

    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    #Depending on what the user clicks returns the level of difficulty
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    return 30
                elif medium_rectangle.collidepoint(event.pos):
                    return 40
                elif hard_rectangle.collidepoint(event.pos):
                    return 50
        pygame.display.update()

def game_end_win(screen):
    #Initialized Font
    win_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)

    #Background Color
    screen.fill(BG_COLOR)

    #Sets and Draws winning text
    win_surface = win_font.render("Congrats, You Won!", 0, TEXT_COLOR)
    win_rect = win_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 200)
    )
    screen.blit(win_surface, win_rect)

    #Sets button color and text
    quit_text = button_font.render("Quit", 0, TEXT_COLOR)

    #Sets button surface
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill(BOX_COLOR)
    quit_surface.blit(quit_text, (10, 10))

    #Sets button rectangle
    quit_rectangle = quit_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 + 125)
    )

    #Draws button
    screen.blit(quit_surface, quit_rectangle)

    #Depending on what the user clicks exits the program
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_rectangle.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()

def game_end_loss(screen):
    #Initialized Font
    lose_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)

    #Background Color
    screen.fill(BG_COLOR)

    #Sets and Draws loss text
    lose_surface = lose_font.render("You Lost, Try Again!", 0, TEXT_COLOR)
    lose_rectangle = lose_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(lose_surface, lose_rectangle)

    #Sets button color and text
    restart_text = button_font.render("Retry", 0, TEXT_COLOR)

    #Sets button surface
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(BOX_COLOR)
    restart_surface.blit(restart_text, (10, 10))

    #Sets button rectangle
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 125)
    )

    # Draw button
    screen.blit(restart_surface, restart_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    main()
        pygame.display.update()

def main():
    while True:
        game_over = False

        #GUI creation, size, and caption
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")

        #Gives title screen and returns difficulty
        difficulty = draw_game_start(screen)

        #Title screen
        screen.fill(BG_COLOR)
        game = Board(WIDTH, HEIGHT, screen, difficulty)
        game.draw()
        pygame.display.update()

        #Sets buttons and text
        button_font = pygame.font.Font(None, 50)
        reset_text = button_font.render("Reset", 0, TEXT_COLOR)
        restart_text = button_font.render("Restart", 0, TEXT_COLOR)
        exit_text = button_font.render("Exit", 0, TEXT_COLOR)

        #Sets button color and text and draws them
        reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surface.fill(BOX_COLOR)
        reset_surface.blit(reset_text, (10, 10))
        restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surface.fill(BOX_COLOR)
        restart_surface.blit(restart_text, (10, 10))
        exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surface.fill(BOX_COLOR)
        exit_surface.blit(exit_text, (10, 10))

        #Sets button rectangles
        reset_rectangle = reset_surface.get_rect(
            center = (WIDTH / 2 - 200, HEIGHT - 50)
        )
        restart_rectangle = restart_surface.get_rect(
            center = (WIDTH // 2, HEIGHT - 50)
        )
        exit_rectangle = exit_surface.get_rect(
            center = (WIDTH / 2 + 200, HEIGHT - 50)
        )

        #Draws button
        screen.blit(reset_surface, reset_rectangle)
        screen.blit(restart_surface, restart_rectangle)
        screen.blit(exit_surface, exit_rectangle)

        #User clicks
        while game_over is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                #When the user clicks on the screen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    try:
                        if event.pos[0] <= 600 and event.pos[1] <= 600:
                            x, y = event.pos
                            col, row = game.click(x, y)
                            game.select(row, col)
                        #If user clicked reset
                        elif reset_rectangle.collidepoint(event.pos):
                            screen.fill(BG_COLOR)
                            game.reset_to_original()
                            #Redraws buttons if reset
                            screen.blit(reset_surface, reset_rectangle)
                            screen.blit(restart_surface, restart_rectangle)
                            screen.blit(exit_surface, exit_rectangle)
                        #If restart goes back to start of main
                        elif restart_rectangle.collidepoint(event.pos):
                            main()
                        #Closes the program
                        elif exit_rectangle.collidepoint(event.pos):
                            sys.exit()
                    except TypeError:
                        continue

                #If user uses arrow keys to move in the board
                if event.type == pygame.KEYDOWN:
                    try:
                        if event.key == pygame.K_DOWN and row < 8:
                            row += 1
                            game.select(row, col)
                        elif event.key == pygame.K_UP and row > 0:
                            row -= 1
                            game.select(row, col)
                        elif event.key == pygame.K_LEFT and col > 0:
                            col -= 1
                            game.select(row, col)
                        elif event.key == pygame.K_RIGHT and col < 8:
                            col += 1
                            game.select(row, col)
                    except UnboundLocalError:
                        col, row = 0, 0
                        game.select(col, row)

                #If user clicks any of the number keys or backspace
                if event.type == pygame.KEYDOWN and game.cell.value == 0:
                    #Deletes the cell
                    if event.key == pygame.K_BACKSPACE:
                        game.clear()
                    #Sketches the number when number key is pressed
                    elif event.key == pygame.K_1:
                        game.sketch(1)
                    elif event.key == pygame.K_2:
                        game.sketch(2)
                    elif event.key == pygame.K_3:
                        game.sketch(3)
                    elif event.key == pygame.K_4:
                        game.sketch(4)
                    elif event.key == pygame.K_5:
                        game.sketch(5)
                    elif event.key == pygame.K_6:
                        game.sketch(6)
                    elif event.key == pygame.K_7:
                        game.sketch(7)
                    elif event.key == pygame.K_8:
                        game.sketch(8)
                    elif event.key == pygame.K_9:
                        game.sketch(9)
                    #Places number when they press the enter key
                    elif event.key == pygame.K_RETURN:
                        game.place_number(game.cells[row][col].sketched_value)
                #Checks if board is full
                if game.is_full() is True:
                    game.update_board()
                    #Check if win
                    if game.check_board() is True:
                        game_over = True
                        game_end_win(screen)
                    #Check if loss
                    elif game.check_board is False:
                        game_over = True
                        game_end_loss(screen)
                    else:
                        game_over = True
                        game_end_loss(screen)

            #Update display after every event
            pygame.display.update()

if __name__ == "__main__":
    main()
