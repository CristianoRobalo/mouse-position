#! env/bin/python3

from threading import Thread

from pynput import mouse


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print(f'{"Pressed" if pressed else "Released"}(x = {x}, y = {y})')


def get_position_thread():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

try:
    gpt = Thread(target=get_position_thread)
    gpt.daemon = True
    gpt.start()

    while True:
        x, y = mouse.Controller().position
        position_output = f'x={x:4d}, y={y:4d}'
        print(position_output, end='\b' * len(position_output), flush=True)
except KeyboardInterrupt:
    print('\nDone!')
    exit(0)
