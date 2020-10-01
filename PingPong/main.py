# step 1 - Create the App
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget): #Step 2
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    # moving the ball by calling the move function and other stuff
    # on_touch_down() - when our fingers / mouse touch the screen
    # on_touch_up() - when we lift our finger off the screen after touching it
    # on_touch_move() - when we drag our finger on the screen
    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))
    def update(self, dt):
        self.ball.move()
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        #bounce ball off of top and bottom of screen
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1
        #bounce off left and increase score
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player1.score += 1
        #bounce off right and increase score
        if self.ball.x > self.width -50:
            self.ball.velocity_x *= -1
            self.player2.score += 1
    def on_touch_move(self, touch):
        if touch.x < self.width * 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y

class PongApp(App): #Step 1
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update, 1.0/60.0)#60 fps
        game.serve_ball()
        return game

PongApp().run()