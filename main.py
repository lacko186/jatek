def on_button_pressed_a():
    global Helyzet
    Helyzet += -1
    led.toggle(Helyzet, 4)
    led.unplot(Helyzet + 1, 4)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global pont
    for index in range(5):
        led.plot(Helyzet, 4 - index)
        basic.pause(10)
        led.unplot(Helyzet, 0)
        led.unplot(Helyzet, 1)
        led.unplot(Helyzet, 2)
        led.unplot(Helyzet, 3)
    if True:
        pont += 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Helyzet
    Helyzet += 1
    led.toggle(Helyzet, 4)
    led.unplot(Helyzet - 1, 4)
input.on_button_pressed(Button.B, on_button_pressed_b)

Helyzet = 0
OLED.init(128, 64)
pont = 0
Helyzet = 0
basic.show_leds("""
    # # # # #
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    """)

def on_forever():
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(587, music.beat(BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.DOUBLE + BeatFraction.HALF))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(587, music.beat(BeatFraction.WHOLE))
    music.play_tone(659, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    basic.pause(1000)
basic.forever(on_forever)
