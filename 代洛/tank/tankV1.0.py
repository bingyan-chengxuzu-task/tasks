import pygame
import random

class enemy_tank_ai(pygame.sprite.Sprite):
    def __init__( self, image, position,direction, speed = 100 ):
        pygame.sprite.Sprite.__init__( self )
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.direction = direction
        self.speed = speed
    def draw_self( self, surface ):
        surface.blit( self.image, self.rect.topleft )
    def move( self, current_time, map_object_list,imageU ):
        ( x, y ) = self.rect.topleft
        if self.direction == 'up':
            enemy_test_up = enemy_tank_ai( imageU,(x,y-1),'up')
            if pygame.sprite.spritecollideany( enemy_test_up, map_object_list) != None:
                if pygame.sprite.spritecollideany( enemy_test_up, map_object_list).is_destroyable == 1:
                    return
            self.rect.topleft = ( x, y - self.speed * current_time)
        if self.direction == 'down':
            enemy_test_up = enemy_tank_ai( imageU,(x,y+1),'up')
            if pygame.sprite.spritecollideany( enemy_test_up, map_object_list) != None:
                if pygame.sprite.spritecollideany( enemy_test_up, map_object_list).is_destroyable == 1:
                    return
            self.rect.topleft = ( x, y + self.speed * current_time )
        if self.direction == 'left':
            enemy_test_up = enemy_tank_ai( imageU,(x-1,y),'up')
            if pygame.sprite.spritecollideany( enemy_test_up, map_object_list) != None:
                if pygame.sprite.spritecollideany( enemy_test_up, map_object_list).is_destroyable == 1:
                    return
            self.rect.topleft = ( x - self.speed *current_time, y )
        if self.direction == 'right':
            enemy_test_up = enemy_tank_ai( imageU,(x+1,y),'up')
            if pygame.sprite.spritecollideany( enemy_test_up, map_object_list) != None:
                if pygame.sprite.spritecollideany( enemy_test_up, map_object_list).is_destroyable == 1:
                    return
            self.rect.topleft = ( x + self.speed *current_time, y )

    def firing( self, moving_object_list, image_enemy_missile ):
        ( a, b ) = self.rect.topleft
        if self.direction == 'right':
            ( a, b ) = ( a + 64 , b + 24 )
        if self.direction == 'left':
            ( a, b ) = ( a - 16 , b + 24 )
        if self.direction == 'up':
            ( a, b ) = ( a + 24 , b - 16 )
        if self.direction == 'down':
            ( a, b ) = ( a + 24 , b + 64 )
        enemy_missile = moving_object(image_enemy_missile, ( a, b ),self.direction, 250 )
        moving_object_list.append(enemy_missile)

    def exploring( self, map_object_list, current_time,imageU,imageD,imageL,imageR, target_position):
        ( a, b ) = self.rect.topleft
        ( m, n ) = target_position
        r_o = random.Random()

        result_list = [self.direction_can_go(map_object_list,'up',imageU),self.direction_can_go(map_object_list,'down',imageU),
                        self.direction_can_go(map_object_list,'left',imageU),self.direction_can_go(map_object_list,'right',imageU)]

        direction_list = ['up','down','left','right']
        image_list = [imageU,imageD,imageL,imageR]
        i = direction_list.index(self.direction)

        if result_list[i] != 0 :
            self.move( current_time, map_object_list, imageU)
            return
        else:
            number_direction = r_o.randrange(0,4)
            self.direction = direction_list[number_direction]
            self.image = image_list[number_direction]
            return

    def direction_can_go( self, map_object_list, direction, imageU ):
        ( a, b ) = self.rect.topleft
        enemy_test_up = enemy_tank_ai( imageU,(a,b-1),'up')
        enemy_test_down = enemy_tank_ai( imageU,(a,b+1),'up')
        enemy_test_left = enemy_tank_ai( imageU,(a-1,b),'up')
        enemy_test_right = enemy_tank_ai( imageU,(a+1,b),'up')

        if direction == 'up':
            if b - 1 >= 0:
                if pygame.sprite.spritecollideany( enemy_test_up, map_object_list) == None:
                    return 1
                if  pygame.sprite.spritecollideany( enemy_test_up, map_object_list) != None:
                    if  pygame.sprite.spritecollideany( enemy_test_up, map_object_list).is_destroyable == 0:
                        return 0
                    else:
                        return 2
            else:
                return 0

        if direction == 'down':
            if b + 1 <= 640-64:
                if pygame.sprite.spritecollideany( enemy_test_down, map_object_list) == None:
                    return 1
                if  pygame.sprite.spritecollideany( enemy_test_down, map_object_list) != None:
                    if  pygame.sprite.spritecollideany( enemy_test_down, map_object_list).is_destroyable == 0:
                        return 0
                    else:
                        return 2
            else:
                return 0

        if direction == 'left':
            if a - 1 >= 0:
                if pygame.sprite.spritecollideany( enemy_test_left, map_object_list) == None:
                    return 1
                if  pygame.sprite.spritecollideany( enemy_test_left, map_object_list) != None:
                    if  pygame.sprite.spritecollideany( enemy_test_left, map_object_list).is_destroyable == 0:
                        return 0
                    else:
                        return 2
            else:
                return 0

        if direction == 'right':
            if a + 1 <= 1280-64:
                if pygame.sprite.spritecollideany( enemy_test_right, map_object_list) == None:
                    return 1
                if  pygame.sprite.spritecollideany( enemy_test_right, map_object_list) != None:
                    if  pygame.sprite.spritecollideany( enemy_test_right, map_object_list).is_destroyable == 0:
                        return 0
                    else:
                        return 2
            else:
                return 0



class moving_object(pygame.sprite.Sprite):
    '''moving things like tanks,bombs,missiles'''
    def __init__( self, image, position = (0,0),direction = 'up', speed = 0,is_enemy = -1 ):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.direction = direction
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.is_enemy = is_enemy

    def move( self ):
        ( x, y ) = self.rect.topleft

        if self.direction == 'up':
            self.rect.topleft = ( x, y - 32 )
        if self.direction == 'down':
            self.rect.topleft = ( x, y + 32 )
        if self.direction == 'left':
            self.rect.topleft = ( x - 32, y )
        if self.direction == 'right':
            self.rect.topleft = ( x + 32, y )

    def move_at_certain_speed ( self, current_time ):
        ( x, y ) = self.rect.topleft

        if self.direction == 'up':
            self.rect.topleft = ( x, y - self.speed * current_time  )
        if self.direction == 'down':
            self.rect.topleft = ( x, y + self.speed * current_time  )
        if self.direction == 'left':
            self.rect.topleft = ( x - self.speed * current_time , y )
        if self.direction == 'right':
            self.rect.topleft = ( x + self.speed * current_time , y )


class map_object(pygame.sprite.Sprite):
    #is_destroyable = 1,can be destroyed
    #is_destroyable = 0,can't be destroyed

    #is_collide = 1, collide!
    def __init__( self, image, position = ( 0, 0 ), is_destroyable = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.is_destroyable = is_destroyable

def main():
    pygame.init()
    pygame.mixer.init()
    surface_size = 640

    #load wav
    blast_wav=pygame.mixer.Sound("blast.wav")
    start_wav = pygame.mixer.Sound('start.wav')
    fire_wav = pygame.mixer.Sound('fire.wav')
    start_wav.play()

    #load image

    image_tank_p1_up = pygame.image.load('p1tankU.gif')
    image_tank_p1_down = pygame.image.load('p1tankD.gif')
    image_tank_p1_left = pygame.image.load('p1tankL.gif')
    image_tank_p1_right = pygame.image.load('p1tankR.gif')
    image_tank_missile = pygame.image.load('tankmissile.gif')
    image_enemy1_up = pygame.image.load('enemy1U.gif')
    image_enemy1_down = pygame.image.load('enemy1D.gif')
    image_enemy1_left = pygame.image.load('enemy1L.gif')
    image_enemy1_right = pygame.image.load('enemy1R.gif')
    image_enemy2_up = pygame.image.load('enemy2U.gif')
    image_enemy2_down = pygame.image.load('enemy2D.gif')
    image_enemy2_left = pygame.image.load('enemy2L.gif')
    image_enemy2_right = pygame.image.load('enemy2R.gif')
    image_enemy3_up = pygame.image.load('enemy3U.gif')
    image_enemy3_down = pygame.image.load('enemy3D.gif')
    image_enemy3_left = pygame.image.load('enemy3L.gif')
    image_enemy3_right = pygame.image.load('enemy3R.gif')
    image_enemy_missile = pygame.image.load('enemymissile.gif')
    image_walls = pygame.image.load('walls.gif')
    image_wall = pygame.image.load('wall.gif')
    image_steels = pygame.image.load('steels.gif')
    image_steel = pygame.image.load('steel.gif')
    image_home = pygame.image.load('home.gif')
    image_water = pygame.image.load('water.gif')
    image_grass = pygame.image.load('grass.gif')
    image_blast_1 = pygame.image.load('blast1.gif')
    image_blast_2 = pygame.image.load('blast2.gif')
    image_blast_3 = pygame.image.load('blast3.gif')
    image_blast_4 = pygame.image.load('blast4.gif')
    image_blast_5 = pygame.image.load('blast5.gif')
    image_blast_6 = pygame.image.load('blast6.gif')
    image_blast_7 = pygame.image.load('blast7.gif')

    #list of blast images
    blast_image_list = [image_blast_1,image_blast_2,image_blast_3,image_blast_4,
                        image_blast_5,image_blast_6,image_blast_7]

    #text
    my_font = pygame.font.SysFont('Courier',30)
    #game over text
    game_over_text = pygame.font.SysFont('Courier', 50)

    #creating moving objects like tanks and missiles
    tank_p1 = moving_object(image_tank_p1_up,(8*64,9*64),'up')
    moving_object_list = [tank_p1]

    #creating enermy tanks
    enemy_tank_list = []
    for i in range(3):
        enemy1 = enemy_tank_ai( image_enemy1_down,((i)*64,0),'down')
        enemy_tank_list.append(enemy1)
    for i in range(1):
        enemy1 = enemy_tank_ai( image_enemy1_down,((i+5)*64,0),'down')
        enemy_tank_list.append(enemy1)
    for i in range(4):
        enemy1 = enemy_tank_ai( image_enemy1_down,((i+8)*64,0),'down')
        enemy_tank_list.append(enemy1)
    for i in range(1):
        enemy1 = enemy_tank_ai( image_enemy1_down,((i+14)*64,0),'down')
        enemy_tank_list.append(enemy1)

    #creating map objects
    home = map_object( image_home, (608,592))
    map_object_list = [home]

    #the location of the map objects
    #wall is used to protect home
    location_of_map_wall = [(608-32,640-32),(608-32,640-32*2),(608-32,640-32*3),(608,640-32*3),
                            (608+32,640-32*3),(608+32*2,640-32*3),(608+32*2,640-32*2),(608+32*2,640-32)]
    for location in location_of_map_wall:
        wall = map_object(image_wall,location)
        map_object_list.append(wall)

    #the location of walls
    location_of_map_walls = [(64,4*64),(64*2,4*64),(64*3,4*64),(64*3,5*64),(64*4,5*64),
                            (64*5,5*64),(64*6,5*64),(64*7,5*64),(64*6,4*64),(64*7,4*64),(64*8,4*64),
                            (64+10*64,4*64),(64*2+10*64,4*64),(64*3+10*64,4*64),(64*2+10*64,5*64),(64*3+10*64,5*64),(64*4+10*64,5*64),
                            (64*5+10*64,5*64),(64*6+10*64,5*64),(64*6+10*64,4*64),(64*7+10*64,4*64),(64*8+10*64,4*64),
                            (4*64,8*64),(5*64,8*64),(4*64,9*64),(5*64,9*64),(14*64,8*64),(15*64,8*64),(14*64,9*64),(15*64,9*64)]

    for i in range(16):
        location_of_map_walls.append(((i+2)*64,6*64))
    for i in range(16):
        location_of_map_walls.append(((i+2)*64,3*64))
    for location in location_of_map_walls:
        walls = map_object( image_walls, location )
        map_object_list.append( walls )

    #location of grass
    location_of_grass = [(0,0),(0,64),(0,64*2),(0,64*3),(64,0),(64,64),(64,64*2),(64,64*3),(0,6*64),(0,7*64),(0,64*8),(0,64*9),
                        (64,6*64),(64,7*64),(64,64*8),(64,64*9),(18*64,0),(18*64,64),(18*64,64*2),(18*64,64*3),
                        (19*64,0),(19*64,64),(19*64,64*2),(19*64,64*3),(18*64,6*64),(18*64,64*7),(18*64,64*8),(18*64,64*9),
                        (19*64,6*64),(19*64,7*64),(19*64,64*8),(19*64,64*9)]

    #loacation of water
    location_of_map_water = [(0,4*64),(0,5*64),(1280-64,4*64),(1280-64,5*64),(608-32,4*64),(608-32,5*64),(640,4*64),(640,5*64)]
    for location in location_of_map_water:
        water = map_object( image_water, location, 0 )
        map_object_list.append( water )

    #location of steels
    location_of_map_steels = [(4*64,4*64),(5*64,4*64),(15*64,4*64),(14*64,4*64),(64,5*64),(64*2,5*64),(8*64,5*64),(11*64,5*64),(64*7+10*64,5*64),(18*64,5*64),
                                (4*64,7*64),(5*64,7*64),(14*64,7*64),(15*64,7*64),(4*64,0),(4*64,64),(7*64,0),(7*64,64),(12*64,0),
                                (12*64,64),(15*64,0),(15*64,64)]
    for location in location_of_map_steels:
        steels = map_object( image_steels,location,0 )
        map_object_list.append( steels )

    main_surface = pygame.display.set_mode((1366,768),pygame.FULLSCREEN,32)
    #main_surface = pygame.display.set_mode((surface_size * 2,surface_size))

    clock = pygame.time.Clock()

    is_blast = None
    is_blast_p = None
    i = None
    j = None
    score = 0


    count = 0
    while True:
        count += 1
        ev = pygame.event.poll()

        if ev.type == pygame.QUIT:
            pygame.quit()
            return 1
        if ev.type == pygame.MOUSEBUTTONDOWN:
            (o,l) = pygame.mouse.get_pos()
            if o >= 1000 and o <= 1200 and l >= 640+64 and l <= 640+64 +50:
                break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict['key']
            ( a, b ) = tank_p1.rect.topleft
            if key == 27:
                pygame.quit()
                return 1
            if key == 32:
                #blank
                fire_wav.play()
                if tank_p1.direction == 'right':
                    ( a, b ) = ( a + 64 , b + 24 )
                if tank_p1.direction == 'left':
                    ( a, b ) = ( a - 16 , b + 24 )
                if tank_p1.direction == 'up':
                    ( a, b ) = ( a + 24 , b - 16 )
                if tank_p1.direction == 'down':
                    ( a, b ) = ( a + 24 , b + 64 )
                tank_missile = moving_object(image_tank_missile, ( a, b ),tank_p1.direction, 200,0 )
                tank_missile.direction = tank_p1.direction

                moving_object_list.append(tank_missile)


            if key == 273:
                #up
                if tank_p1.direction == 'up' :
                    if b - 32 < 0:
                        continue
                    tank_test = moving_object(image_tank_p1_up,(a,b-32),'up',0)
                    #the tank can't go into the wall
                    if pygame.sprite.spritecollideany( tank_test, map_object_list ) != None :
                        continue
                    tank_p1.move()
                tank_p1.image = image_tank_p1_up
                tank_p1.direction = 'up'
            if key == 274:
                #down
                if tank_p1.direction == 'down' :
                    if b + 32 > 640 - 64:
                        continue
                    tank_test = moving_object(image_tank_p1_up,(a,b+32),'up',0)
                    if pygame.sprite.spritecollideany( tank_test, map_object_list ) != None:
                        continue
                    tank_p1.move()
                tank_p1.image = image_tank_p1_down
                tank_p1.direction = 'down'
            if key == 276:
                #left
                if tank_p1.direction == 'left' :
                    if a - 32 < 0:
                        continue
                    tank_test = moving_object(image_tank_p1_up,(a-32,b),'up',0)
                    if pygame.sprite.spritecollideany( tank_test, map_object_list ) != None:
                        continue
                    tank_p1.move()
                tank_p1.image = image_tank_p1_left
                tank_p1.direction = 'left'
            if key == 275:
                #right
                if tank_p1.direction == 'right' :
                    if a + 32 > 1280 - 64:
                        continue
                    tank_test = moving_object(image_tank_p1_up,(a+32,b),'up',0)
                    if pygame.sprite.spritecollideany( tank_test, map_object_list ) != None:
                        continue
                    tank_p1.move()
                tank_p1.image = image_tank_p1_right
                tank_p1.direction = 'right'



        main_surface.fill((0,0,0))


        current_time = clock.tick(100)

        #enemy tank auto moving
        for one_enemy_tank in enemy_tank_list:
            one_enemy_tank.exploring( map_object_list, current_time/1000,image_enemy1_up,image_enemy1_down,image_enemy1_left,image_enemy1_right, (608,592))
        #enemy tanks fire
        if count % 100 == 0:
            for one_enemy_tank in enemy_tank_list:
                one_enemy_tank.firing(moving_object_list, image_enemy_missile )


        for location in location_of_grass:
            main_surface.blit( image_grass, location )

        if is_blast_p == None:


            for one_object in moving_object_list:
                if one_object.speed != 0:
                    #missiles move automatically
                    one_object.move_at_certain_speed( current_time / 1000 )
                    ( a, b ) = one_object.rect.topleft
                main_surface.blit( one_object.image, one_object.rect.topleft )
        else:
            for one_object in moving_object_list[1:]:
                if one_object.speed != 0:
                    #missiles move automatically
                    one_object.move_at_certain_speed( current_time / 1000 )
                    ( a, b ) = one_object.rect.topleft
                main_surface.blit( one_object.image, one_object.rect.topleft )

        for one_object in moving_object_list:
            #delete the objects which are out of the area
            ( a, b ) = one_object.rect.topleft
            if one_object.speed != 0:
                if a < 0  or b < 0 or b > 640 or a > 1280:
                    delete_object = one_object
                    moving_object_list.remove( delete_object )

        #if the missile and wall collide ,they both disappear
        for one_object in moving_object_list:
            for one_map_object in map_object_list:
                if pygame.sprite.collide_rect(one_object,one_map_object) == True and one_object.speed != 0 and one_map_object.is_destroyable == 1 :
                    moving_object_list.remove( one_object )
                    map_object_list.remove( one_map_object )
                    #if this break is not added, mistake!
                    break
                if pygame.sprite.collide_rect(one_object,one_map_object) == True and one_object.speed != 0 and one_map_object.is_destroyable == 0 :
                    moving_object_list.remove( one_object )
                    break


        for one_object in moving_object_list:
            for one_enemy_tank in enemy_tank_list:
                if pygame.sprite.collide_rect( one_object, one_enemy_tank ) == True and one_object.speed != 0:
                    if one_object.is_enemy == -1:
                        continue

                    moving_object_list.remove( one_object )
                    enemy_tank_list.remove( one_enemy_tank )
                    one_enemy_tank.speed = 0
                    is_blast = 1
                    i = 1
                    enemy1 = one_enemy_tank
                    blast_wav.play()
                    score += 100

        for one_object in moving_object_list[1:]:
            if  pygame.sprite.collide_rect( one_object, moving_object_list[0] ) == True and one_object.speed != 0 and one_object.is_enemy != 0:
                j = 1
                is_blast_p = 1
                blast_wav.play()

        #enemy1.draw_self(main_surface)
        for one_enemy_tank in enemy_tank_list:
            one_enemy_tank.draw_self( main_surface )


        for one_map_object in map_object_list:
            main_surface.blit(one_map_object.image,one_map_object.rect.topleft)


        the_text = my_font.render('fps {0}'.format( clock.get_fps()),True,(255,0,0))
        main_surface.blit( the_text,(0,0))

        if i == 7:
            i = None
            is_blast = None

        if j == 7:
            the_game_over_text = game_over_text.render('GAME OVER',True,(255,255,255))
            main_surface.blit(the_game_over_text,(500,200))
            pygame.display.update()

            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.KEYDOWN:
                    pygame.quit()
                    return 1

        if is_blast == 1:
            main_surface.blit(blast_image_list[i],enemy1.rect.topleft)
            pygame.display.update()
            pygame.time.delay(50)
            i += 1
            continue

        if is_blast_p == 1:
            main_surface.blit(blast_image_list[j],moving_object_list[0].rect.topleft)
            pygame.display.update()
            pygame.time.delay(50)
            j += 1
            continue

        if map_object_list[0] != home:
            the_game_over_text = game_over_text.render('GAME OVER',True,(255,255,255))
            main_surface.blit(the_game_over_text,(500,200))
            pygame.display.update()

            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.KEYDOWN or ev.type == pygame.QUIT:
                    pygame.quit()
                    return 1
        if len(enemy_tank_list) == 0:
            victory_text = pygame.font.SysFont('Courier', 50)
            the_victory_text = victory_text.render('VICTORY!',True,(255,0,0))
            main_surface.blit( the_victory_text,(500,200))
            pygame.display.update()
            while True:
                ev = pygame.event.poll()
                if ev.type == pygame.KEYDOWN or ev.type == pygame.QUIT:
                    pygame.quit()
                    return

        score_text = pygame.font.SysFont('Courier', 20)
        the_score_text = score_text.render('score: {0}'.format(score),True,(255,255,255))
        main_surface.blit( the_score_text,(64,640+64))

        pygame.draw.rect( main_surface,(255,255,255),pygame.Rect(1000,640+64,200,50),0)

        restart_text = pygame.font.SysFont('Courier', 20)
        restart_text = score_text.render('restart',True,(255,0,0))
        main_surface.blit( restart_text,(1000,640+64))

        pygame.display.update()


    pygame.quit()

while True:
    if main() == 1:
        break
