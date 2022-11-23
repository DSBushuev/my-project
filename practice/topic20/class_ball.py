from random import randint

import pygame.draw

EXAMPLES = []


class Ball:

    def __init__(self, sc, pos, color=(255, 255, 0), radius=20, speed=5):
        EXAMPLES.append(self)
        if type(speed) == int or type(speed) == float:
            speed = (int(speed), int(speed))
        self.pos = pos
        self.pos_x, self.pos_y = self.pos
        self.color = color
        self.radius = radius
        self.speed = speed
        self.sc = sc
        self.speed_x, self.speed_y = self.speed
        self.speed = (self.speed_x, self.speed_y)
        self.abs_speed = (abs(self.speed_x) ** 2 + abs(self.speed_y) ** 2) ** 0.5
        self.EXAMPLES = EXAMPLES

    def change_course(self, ball2):
        def stat(ball1, ball_2):
            _s1_x, _s2_x = int(ball1.speed_x), int(ball_2.speed_x)
            _s1_y, _s2_y = int(ball1.speed_y), int(ball_2.speed_y)
            if _s1_x == 0 and _s1_y == 0:
                if abs(_s2_x) > abs(_s2_y):
                    ball1.speed_x = _s2_x * 0.25
                    ball_2.speed_x = - _s2_x * 0.75

                elif abs(_s2_x) < abs(_s2_y):
                    ball1.speed_y = _s2_y * 0.25
                    ball_2.speed_y = - _s2_y * 0.75

                else:
                    ball1.speed_x = _s2_x * 0.75
                    ball1.speed_y = _s2_y * 0.75
                    ball_2.speed_x = - _s2_x * 0.25
                    ball_2.speed_y = - _s2_y * 0.25

        s1_x, s2_x = int(self.speed_x), int(ball2.speed_x)
        s1_y, s2_y = int(self.speed_y), int(ball2.speed_y)

        if s1_x == 0 and s1_y == 0:
            stat(self, ball2)
            return
        if s2_x == 0 and s2_y == 0:
            stat(ball2, self)
            return

        if s1_x < 0 < s2_x or s1_x > 0 > s2_x:
            if s1_y > 0 > s2_y or s1_y < 0 < s2_y:
                if int(s1_x / s1_y) == int(s2_x / s2_y):
                    self.speed_x *= -1
                    ball2.speed_x *= -1
                    self.speed_y *= -1
                    ball2.speed_y *= -1
                    return
                if abs(s1_x) > abs(s1_y):
                    if abs(s2_x) >= abs(s2_y):
                        self.speed_y *= -1
                        ball2.speed_y *= -1
                        return
                    if abs(s2_x) < abs(s2_y):
                        if abs(s2_y / s2_x) > abs(s1_x / s1_y):
                            self.speed_x *= -1
                            ball2.speed_x *= -1
                            return
                        self.speed_y *= -1
                        ball2.speed_y *= -1
                        return

        if abs(s1_x) > abs(s1_y):
            self.speed_y = - self.speed_y if int(self.speed_y) != 0 else ball2.speed_y * 0.3
            ball2.speed_y = - ball2.speed_y if int(ball2.speed_y) != 0 else - self.speed_y * 0.3
            return

        self.speed_x = - self.speed_x if int(self.speed_x) != 0 else ball2.speed_x * 0.3
        ball2.speed_x = - ball2.speed_x if int(ball2.speed_x) != 0 else - self.speed_x * 0.3
        return

    def clash(self, ball2):
        if self.speed_x != 0 or self.speed_y != 0 or ball2.speed_x != 0 or ball2.speed_y != 0:
            x = abs(self.pos_x - ball2.pos_x)
            y = abs(self.pos_y - ball2.pos_y)
            if (x ** 2 + y ** 2) ** 0.5 <= self.radius + ball2.radius:
                print("Clash")
                self.change_course(ball2)
                for i in range(2):
                    self._move()
                    ball2._move()
                return True
        return False

    def change_speed(self, x, y):
        self.speed_x = x
        self.speed_y = y

    def speed_up(self, boost):
        self.speed_x += self.speed_x / 100 * boost
        self.speed_y += self.speed_y / 100 * boost

    def speed_slow(self, nx_slow=1):
        self.speed_x -= (self.speed_x / 100 * nx_slow) if self.speed_x > 0 else (self.speed_x / 100 * nx_slow)
        self.speed_y -= (self.speed_y / 100 * nx_slow) if self.speed_y > 0 else (self.speed_y / 100 * nx_slow)
        if 0 < self.speed_x < 1 or 0 > self.speed_x > -1:
            self.speed_x = 0
        if 0 < self.speed_y < 1 or 0 > self.speed_y > -1:
            self.speed_y = 0

    def color_of_speed(self):
        self.abs_speed = (abs(self.speed_x) ** 2 + abs(self.speed_y) ** 2) ** 0.5
        s = int(self.abs_speed)
        red, green, blue = 255, 255, 0

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
        if self.radius > self.pos_x + self.speed_x:
            self.pos_x = 1 + self.radius
            self.speed_x *= -1
        elif self.radius + self.pos_x + self.speed_x > self.sc.get_size()[0]:
            self.pos_x = self.sc.get_size()[0] - self.radius - 1
            self.speed_x *= -1
        if self.radius > self.pos_y + self.speed_y:
            self.pos_y = 1 + self.radius
            self.speed_y *= -1
        elif self.radius + self.pos_y + self.speed_y > self.sc.get_size()[1]:
            self.pos_y = self.sc.get_size()[1] - self.radius - 1
            self.speed_y *= -1
        self.pos_x += int(self.speed_x)
        self.pos_y += int(self.speed_y)
        self.pos = (self.pos_x, self.pos_y)

    def speed_limit(self, limit):
        if self.speed_x > limit:
            self.speed_x = limit

        if self.speed_x < - limit:
            self.speed_x = - limit

        if self.speed_y > limit:
            self.speed_y = limit

        if self.speed_y < - limit:
            self.speed_y = - limit

    def _show(self):
        pygame.draw.ellipse(self.sc, self.color,
                            (self.pos_x - self.radius, self.pos_y - self.radius, self.radius * 2, self.radius * 2))

    def ball_stretch(self):
        pass
