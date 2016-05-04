import pyglet
import os

def resource_path(relative_path):

    ''' Get absolute path to resource, works for dev and 
    for deployment with Pyinstsaller'''

    try:
        # PyInstaller creates a temp folder and stores 
        # path in _MEIPASS
        base_bath = sys._MEIPASS
        pyglet.resource.path = [base_path]
        pyglet.resource.reindex()

    except Exception:
        base_path = os.path.abspath(".")
        pyglet.resource.path = [base_path]
        pyglet.resource.reindex()
    
    return os.path.join(base_path, relative_path)

paddle_file = 'paddle.png'
ball_file = 'ball.png'
paddle = pyglet.image.load(resource_path(paddle_file))
ball = pyglet.image.load(resource_path(ball_file))
