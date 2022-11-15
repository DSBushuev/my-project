import pygame.draw


class Ball:

    def __init__(self, sc, pos, color=(255,255,0), radius=20, speed=5):
        if type(speed) == int or type(speed) == float:
            speed = (int(speed), int(speed))
        self.pos = pos
        self.pos_x, self.pos_y = self.pos
        self.color = color
        self.colorR, self.colorG, self.colorB = color
        self.radius = radius
        self.speed = speed
        self.sc = sc
        self.speed_x, self.speed_y = self.speed
        self.speed = (self.speed_x, self.speed_y)
        self.abs_speed = (abs(self.speed_x)**2 + abs(self.speed_y)**2) ** 0.5


    def change_course(self, ball2):
        speed_x1, speed_y1 = self.speed_x, self.speed_y
        speed_x2, speed_y2 = ball2.speed_x, ball2.speed_y
        if speed_x1 >= 0 and speed_x2 <= 0 or speed_x1 <= 0 and speed_x2 >= 0:
            if speed_y1 >= 0 and speed_y2 >= 0 or speed_y1 <= 0 and speed_y2 <= 0:
                speed_x1 *= -1
                speed_x2 *= -1
            else:
                if speed_x1 + speed_x2 > speed_y1 + speed_y2:
                    speed_y1 *= -1
                    speed_y2 *= -1
                else:
                    speed_x1 *= -1
                    speed_x2 *= -1
        else:
            if speed_y1 >= 0 and speed_y2 >= 0 or speed_y1 <= 0 and speed_y2 <= 0:
                if speed_x1 + speed_x2 >= speed_y1 + speed_y2:
                    speed_y1 *= -1
                    speed_y2 *= -1
                else:
                    speed_x1 *= -1
                    speed_x2 *= -1
            else:
                speed_y1 *= -1
                speed_y2 *= -1
        self.speed_x = speed_x1
        self.speed_y = speed_y1
        ball2.change_speed(speed_x2,speed_y2)

    def clash(self, ball2):
        x2, y2 = ball2.pos
        if abs(self.pos_x - x2) <= (self.radius + ball2.radius)/2 and \
                abs(self.pos_y - y2) <= (self.radius + ball2.radius) / 2:
            self.speed_slow(5)
            return True
        return False

    def change_speed(self, x, y):
        self.speed_x = x
        self.speed_y = y

    def speed_up(self, boost):
        if type(boost) == int or type(boost) == float:
            boost = (boost, boost)
        x1, y1 = boost
        self.speed_x += x1 if self.speed_x >= 0 else -x1
        self.speed_y += y1 if self.speed_y >= 0 else -y1

    def speed_slow(self, slow):
        if type(slow) == int or type(slow) == float:
            slow = (slow, slow)
        x1, y1 = slow
        if abs(self.speed_x) - x1 < 0:
            self.speed_x = 0
        else:
            self.speed_x += -x1 if self.speed_x >= 0 else x1

        if abs(self.speed_y) - y1 < 0:
            self.speed_y = 0
        else:
            self.speed_y += -y1 if self.speed_y >= 0 else y1


    def color_of_speed(self):
        s = int(self.abs_speed)
        red,green,blue = 255, 255, 0

        if s < 6:
            blue = (5 - s) * 50
            self.color = (red, green, blue)
            return

        if s > 50:
            self.color = (255, 0, 0)
            return

        red = s * 5
        green = 255 - (s * 5)

        self.color = (red, green, blue)
        return


    def _move(self):
        if self.radius > self.pos_x + self.speed_x or\
                self.pos_x + self.speed_x > self.sc.get_size()[0] - self.radius:
            self.speed_y *= 1.1
            self.speed_x *= -1
        if self.radius > self.pos_y + self.speed_x or\
                self.pos_y + self.speed_y > self.sc.get_size()[1] - self.radius:
            self.speed_x *= 1.1
            self.speed_y *= -1
        if self.speed_x > 60:
            self.speed_x = 60
        if  self.speed_y > 60:
            self.speed_y = 60
        self.pos_x += int(self.speed_x)
        self.pos_y += int(self.speed_y)
        self.pos = (self.pos_x, self.pos_y)

    def ball_show(self):
        pygame.draw.ellipse(self.sc, self.color, (self.pos_x, self.pos_y, self.radius*2, self.radius*2))

    def ball_stretch(self):
        pass




