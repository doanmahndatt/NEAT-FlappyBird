
import pygame
import random
import os
import time
import neat
import visualize
import pickle
pygame.font.init()  # init font

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)
DRAW_LINES = False

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())

gen = 0

class Bird:
    MAX_ROTATION = 25
    IMGS = bird_images
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # cho gia tốc đi xuống
        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # tính vận tốc

        # vận tốc cuối
        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # góc nghiêng giảm dần
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        # Tạo hiệu ứng khi bay
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe():
    GAP = 200
    VEL = 5

    def __init__(self, x):
        self.x = x
        self.height = 0

        # Tạo vị trí pipe
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        # Vẽ top
        win.blit(self.PIPE_TOP, (self.x, self.top))
        # Vẽ bottom
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird, win):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False

class Base:
    VEL = 5
    WIDTH = base_img.get_width()
    IMG = base_img

    def __init__(self, y):

        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):

        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

def draw_window(win, birds, pipes, base, score, gen, pipe_ind):

    if gen == 0:
        gen = 1
    win.blit(bg_img, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    for bird in birds:
        # Vẽ lines từ bird đến pipe
        if DRAW_LINES:
            try:
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_TOP.get_width()/2, pipes[pipe_ind].height), 5)
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_BOTTOM.get_width()/2, pipes[pipe_ind].bottom), 5)
            except:
                pass
        # draw bird
        # bird.draw(win)

    if len(birds) != 0:
        # draw bird
        birds[0].draw(win)

    # score
    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    # # generations
    # score_label = STAT_FONT.render("Gens: " + str(gen-1), 1, (255, 255, 255))
    # win.blit(score_label, (10, 10))
    #
    # # alive
    # score_label = STAT_FONT.render("Alive: " + str(len(birds)), 1, (255,255,255))
    # win.blit(score_label, (10, 50))

    pygame.display.update()


def eval_genomes(genomes, config):

    global WIN, gen
    win = WIN
    gen += 1

    # Cụ thể hơn, nó khởi tạo các đối tượng lưu trữ thông tin về các genome,
    #   neural network và chim (bird) được tạo ra bởi các genome.
    # Đoạn mã này tạo ra một danh sách các neural network được tạo ra bằng cách truyền genome và
    #   config vào hàm create của lớp FeedForwardNetwork trong NEAT.
    # Sau đó, nó khởi tạo một danh sách các chim và genome tương ứng cho mỗi neural network.
    nets = []
    birds = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0  # Bắt đầu với fitness bằng 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230,350))
        ge.append(genome)

    base = Base(FLOOR)
    pipes = [Pipe(700)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():  # determine whether to use the first or second
                pipe_ind = 1       # Ống dẫn trên màn hình được sử dụng như một đầu vào cho mạng nơ-ron.

        for x, bird in enumerate(birds):
            ge[x].fitness += 0.1
            bird.move()

            # truyền vị trí chim, vị trí ống trên và vị trí ống dưới vào mạng neural để quyết định liệu có nhảy hay không
            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:  # Chúng ta sử dụng hàm kích hoạt tanh để kết quả nằm giữa -1 và 1. Nếu kết quả lớn hơn 0.5,
                bird.jump()      #  chim sẽ nhảy.

        base.move()

        rem = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()
            # check for collision
            for bird in birds:
                if pipe.collide(bird, win):
                    ge[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            score += 1
            # thêm điểm khi qua một cột
            for genome in ge:
                genome.fitness += 5
            pipes.append(Pipe(WIN_WIDTH))

        for r in rem:
            pipes.remove(r)

        for bird in birds:
            if bird.y + bird.img.get_height() - 10 >= FLOOR or bird.y < -50:
                nets.pop(birds.index(bird))
                ge.pop(birds.index(bird))
                birds.pop(birds.index(bird))

        draw_window(WIN, birds, pipes, base, score, gen, pipe_ind)


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction
                                , neat.DefaultSpeciesSet, neat.DefaultStagnation
                                , config_file)

    # Tạo ra một Population object, đại diện cho tất cả các genome trong một thế hệ.
    p = neat.Population(config)

    # Thêm các reporter object, trong đó StdOutReporter object sẽ in ra tiến trình huấn luyện trên terminal
    # và StatisticsReporter object sẽ cung cấp các thống kê về tiến trình huấn luyện.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Chạy quá trình huấn luyện bằng cách gọi phương thức "run"
    winner = p.run(eval_genomes, 50)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)