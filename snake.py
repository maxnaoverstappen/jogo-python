# importando bibliotecas
import pygame
import time
import random

snake_speed = 15

# tamanho da janela
window_x = 720
window_y = 480

# definindo cores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# inicializando pygame
pygame.init()

# inicializa a janela do jogo
pygame.display.set_caption('Snake == Game') # titulo da janela
game_window = pygame.display.set_mode((window_x, window_y))

# controlador de FPS (frames por segundo)
fps = pygame.time.Clock()

# definir a posição inicial da cobra
snake_position = [100, 50]

# definir os primeiros 4 blocos do corpo da cobra
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# posição aleatoria da fruta
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# adiciona direção inicial da cobra
# direito
direction = 'RIGHT'
change_to = direction

# pontuação inicial
score = 0

# função para mostrar a pontuação
def show_score(choice, color, font, size):
  
    # cria o objeto de fonte score_font
    score_font = pygame.font.SysFont(font, size)
    
    # cria o objeto de superfície de exibição
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # cria um objeto retangular para o texto
    # objeto de superfície
    score_rect = score_surface.get_rect()
    
    # exibindo texto
    game_window.blit(score_surface, score_rect)

# função de game over
def game_over():
  
    # cria o objeto de fonte my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # cria uma superfície de texto na qual o texto
    # será desenhado
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # cria um objeto retangular para o texto
    # objeto de superfície
    game_over_rect = game_over_surface.get_rect()
    
    # posição do texto
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit desenhará o texto na tela
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # depois de 2 segundos sai do programa
    time.sleep(2)
    
    # sai do pygame
    pygame.quit()
    
    # sai do programa
    quit()


# função principal
while True:
    
    # tratando eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # se duas teclas forem pressionadas simultaneamente
    # não queremos que a cobra se mova em duas
    # direções simultaneamente
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # mover a cobra
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # mecanismo de crescimento do corpo da cobra
    # se a fruta e a cobra colidirem, a pontuação
    # será incrementada em 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
        
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
        
    fruit_spawn = True
    game_window.fill(black)
    
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # condições de game over
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # tocando no corpo da cobra
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # exibindo a pontuação continuamente
    show_score(1, white, 'times new roman', 20)

    # atualiza a tela do jogo
    pygame.display.update()

    # taxa de quadros por segundo / taxa de atualização
    fps.tick(snake_speed)
