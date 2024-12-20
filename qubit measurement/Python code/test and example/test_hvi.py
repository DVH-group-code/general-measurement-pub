hvicode.hvi.load_to_hw()
hvicode.hvi.run(hvicode.hvi.no_wait)
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['max_cycle'].write(1)
hvicode.hvi.sync_sequence.scopes['din'].registers['din_delay'].write(delay_digitizer)
hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['finish_delay'].write(finish_delay)

import keyboard

while True:
    a = hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].read()
    if a == 0:
        hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(1)  # start measurement
    if keyboard.is_pressed("q"):
        break


hvicode.hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(2)  # stop HVI program
hvicode.hvi.release_hw()

hvi.load_to_hw()
hvi.run(hvi.no_wait)
hvi.sync_sequence.scopes['awg1Engine'].registers['hvi_status'].write(2)
hvi.release_hw()
awg1.close()
din.close()