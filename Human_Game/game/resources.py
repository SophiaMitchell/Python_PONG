import pyglet

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

paddle = pyglet.resource.image("paddle.jpg")
ball = pyglet.resource.image("tennis_ball.jpg")
