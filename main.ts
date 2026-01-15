input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    Helyzet += -1
    led.toggle(Helyzet, 4)
    led.unplot(Helyzet + 1, 4)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    for (let index = 0; index < 5; index++) {
        led.plot(Helyzet, 4 - index)
        basic.pause(10)
        led.unplot(Helyzet, 0)
        led.unplot(Helyzet, 1)
        led.unplot(Helyzet, 2)
        led.unplot(Helyzet, 3)
    }
    if (true) {
        pont += 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Helyzet += 1
    led.toggle(Helyzet, 4)
    led.unplot(Helyzet - 1, 4)
})
let Helyzet = 0
OLED.init(128, 64)
let pont = 0
Helyzet = 0
basic.showLeds(`
    # # # # #
    . . . . .
    . . . . .
    . . . . .
    # . . . .
    `)
basic.forever(function on_forever() {
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(587, music.beat(BeatFraction.Whole))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Half))
    music.playTone(440, music.beat(BeatFraction.Whole))
    music.playTone(440, music.beat(BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(587, music.beat(BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(494, music.beat(BeatFraction.Double + BeatFraction.Half))
    music.playTone(523, music.beat(BeatFraction.Half))
    music.playTone(587, music.beat(BeatFraction.Whole))
    music.playTone(659, music.beat(BeatFraction.Whole))
    music.playTone(523, music.beat(BeatFraction.Whole))
    music.playTone(440, music.beat(BeatFraction.Whole))
    music.playTone(440, music.beat(BeatFraction.Whole))
    basic.pause(1000)
})
