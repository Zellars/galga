my_sprite2 = sprites.create(img("""
    . . . . c c c b b b b b . . . .
    . . c c b 4 4 4 4 4 4 b b b . .
    . c c 4 4 4 4 4 5 4 4 4 4 b c .
    . e 4 4 4 4 4 4 4 4 4 5 4 4 e .
    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c
    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e
    e b b 4 4 4 4 4 4 4 4 4 4 4 b e
    . e b 4 4 4 4 4 5 4 4 4 4 b e .
    8 7 e e b 4 4 4 4 4 4 b e e 6 8
    8 7 2 e e e e e e e e e e 2 7 8
    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e
    e c 6 7 6 6 7 7 7 6 6 7 6 c c e
    e b e 8 8 c c 8 8 c c c 8 e b e
    e e b e c c e e e e e c e b e e
    . e e b b 4 4 4 4 4 4 4 4 e e .
    . . . c c c c c e e e e e . . .
"""), SpriteKind.player)
my_sprite2.set_stay_in_screen(True)
info.set_life(3)
controller.move_sprite(my_sprite2, 200, 200)
def on_a_pressed():
 dart = sprites.create_projectile_from_sprite(img("""
     . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . .
     . . . . . . . c c c . . . . . .
     . . . . . . a b a a . . . . . .
     . . . . . c b a f c a c . . . .
     . . . . c b b b f f a c c . . .
     . . . . b b f a b b a a c . . .
     . . . . c b f f b a f c a . . .
     . . . . . c a a c b b a . . . .
     . . . . . . c c c c . . . . . .
     . . . . . . . c . . . . . . . .
     . . . . . . . . . . . . . . . .
     . . . . . . . . . . . . . . . .
 """), my_sprite2, 200, 0)
 controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)
 
 def on_update_interval():
     bogey = sprites.creates(img("""...
     """), SpriteKind.scroll, 0)
     bogey.set_velocity(-100, 0)
     bogey.left = scene.screen_width() #makes it travel the entire screen
     bogey.y = randit(0, scene.screen_height())
     bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
     game.on_update_interval(500, on_update_interval)

     def on_on_overlap(sprite, otherSprite): #Fuction to destoroy sprite and remove
         otherSprite.destroy()
         info.change_life_by(-1)
         sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

def on_projectile_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_projectile_overlap)