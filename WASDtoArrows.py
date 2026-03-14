import keyboard
keyboard.remap_key('w', 'up')
keyboard.remap_key('a', 'left')
keyboard.remap_key('s', 'down')
keyboard.remap_key('d', 'right')

print("W, A, S and D was changed to the arrow keys.")
print("Close this Window to revert it.")

keyboard.wait()