import tcod as libtcod

def handle_keys(key):
    
    #Movment Keys
    if key.vk == libtcod.KEY_UP:
        return {'move':(0, -1)}
    elif key.vk == libtcod.KEY_DOWN:
        return {'move':(0, 1)}
    elif key.vk == libtcod.KEY_LEFT:
        return {'move':(-1, 0)}
    elif key.vk == libtcod.KEY_RIGHT:
        return {'move':(1, 0)}
    
    #Toggle Fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen': True}

    #Exit Game
    elif key.vk == libtcod.KEY_ESCAPE:
        return {'exit': True}

    #No Keypress
    return{}