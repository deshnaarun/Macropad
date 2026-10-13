#include QMK_KEYBOARD_H
#include <stdio.h>
#include "cat_frames.h"

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        KC_A,   KC_B,     // SW1, SW2
        KC_C,   KC_D,     // SW3, SW5
        KC_MUTE           // encoder push-button
    )
};

/* ---------- activity tracking ----------
 * A 4-key macropad doesn't produce meaningful WPM, so the cat reacts to how
 * often you press keys / click / turn the encoder instead. */
#define CAT_AWAKE_MS   3000   // no input for this long -> cat falls asleep
#define CAT_RUN_RATE      4   // inputs within CAT_WINDOW_MS needed to start running
#define CAT_WINDOW_MS  1000
#define CAT_HISTORY       8

static uint32_t input_times[CAT_HISTORY];
static uint8_t  input_head   = 0;
static uint32_t last_input   = 0;
static bool     has_input    = false;
static uint32_t total_inputs = 0;

static void note_activity(void) {
    last_input = timer_read32();
    has_input  = true;
    input_times[input_head] = last_input;
    input_head = (input_head + 1) % CAT_HISTORY;
    total_inputs++;
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (record->event.pressed) {
        note_activity();
    }
    return true;
}

#ifdef ENCODER_ENABLE
bool encoder_update_user(uint8_t index, bool clockwise) {
    if (index == 0) {
        note_activity();
        if (clockwise) {
            tap_code(KC_VOLU);
        } else {
            tap_code(KC_VOLD);
        }
    }
    return true;
}
#endif

/* ---------- cat animation ---------- */
typedef enum { CAT_SLEEP, CAT_WALK, CAT_RUN } cat_state_t;

static cat_state_t cat_state(void) {
    if (!has_input || timer_elapsed32(last_input) > CAT_AWAKE_MS) {
        return CAT_SLEEP;
    }
    uint8_t recent = 0;
    for (uint8_t i = 0; i < CAT_HISTORY; i++) {
        if (timer_elapsed32(input_times[i]) <= CAT_WINDOW_MS) {
            recent++;
        }
    }
    return (recent >= CAT_RUN_RATE) ? CAT_RUN : CAT_WALK;
}

static const char *const sleep_frames[] = {cat_sleep_0, cat_sleep_1};
static const char *const walk_frames[]  = {cat_walk_0, cat_walk_1, cat_walk_2, cat_walk_3};
static const char *const run_frames[]   = {cat_run_0, cat_run_1};

#ifdef OLED_DISPLAY_128X64
/* 128x64: text on the top half, cat walks across the bottom half (pages 4-7)
 * and wraps around the screen edge. */
#    define CAT_TOP_PAGE 4
#    define CAT_MOVES    1
#else
/* 128x32: cat stays put on the left, text on the right. */
#    define CAT_TOP_PAGE 0
#    define CAT_MOVES    0
#endif

static void draw_cat(const char *frame, uint8_t cat_x) {
#if CAT_MOVES
    for (uint8_t page = 0; page < CAT_PAGES; page++) {
        for (uint8_t x = 0; x < OLED_DISPLAY_WIDTH; x++) {
            uint8_t col = (uint8_t)(x - cat_x) % OLED_DISPLAY_WIDTH;  // wraps
            char b = (col < CAT_W) ? pgm_read_byte(frame + page * CAT_W + col) : 0;
            if (page == CAT_PAGES - 1) b |= 0x80;  // ground line on the bottom row
            oled_write_raw_byte(b, (CAT_TOP_PAGE + page) * OLED_DISPLAY_WIDTH + x);
        }
    }
#else
    (void)cat_x;
    for (uint8_t page = 0; page < CAT_PAGES; page++) {
        oled_set_cursor(0, page);
        oled_write_raw_P(frame + page * CAT_W, CAT_W);
    }
#endif
}

static void draw_text(const char *label) {
    char buf[22];
#if CAT_MOVES
    oled_set_cursor(0, 0);
    oled_write_P(PSTR("MACROPAD"), false);
    oled_set_cursor(0, 2);
    snprintf(buf, sizeof(buf), "cat: %-8s", label);
    oled_write(buf, false);
    oled_set_cursor(0, 3);
    snprintf(buf, sizeof(buf), "presses: %-8lu", (unsigned long)total_inputs);
    oled_write(buf, false);
#else
    oled_set_cursor(9, 0);
    oled_write_P(PSTR("MACROPAD"), false);
    oled_set_cursor(9, 1);
    snprintf(buf, sizeof(buf), "%-11s", label);
    oled_write(buf, false);
    oled_set_cursor(9, 3);
    snprintf(buf, sizeof(buf), "n:%-8lu", (unsigned long)total_inputs);
    oled_write(buf, false);
#endif
}

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_0;  // landscape; use OLED_ROTATION_180 if it shows upside down
}

bool oled_task_user(void) {
    static uint32_t    anim_timer = 0;
    static uint8_t     frame      = 0;
    static uint8_t     cat_x      = 8;
    static cat_state_t last_state = CAT_SLEEP;

    cat_state_t state = cat_state();
    if (state != last_state) {
        frame      = 0;
        last_state = state;
        anim_timer = 0;  // redraw immediately
    }

    uint16_t interval;
    uint8_t  count, step;
    const char *const *frames;
    const char *label;
    switch (state) {
        case CAT_RUN:  interval = 90;  count = 2; step = 6; frames = run_frames;   label = "zoom!"; break;
        case CAT_WALK: interval = 180; count = 4; step = 2; frames = walk_frames;  label = "walk";  break;
        default:       interval = 700; count = 2; step = 0; frames = sleep_frames; label = "zzz";   break;
    }

    if (anim_timer == 0 || timer_elapsed32(anim_timer) >= interval) {
        anim_timer = timer_read32();
        if (anim_timer == 0) anim_timer = 1;
        cat_x = (cat_x + step) % OLED_DISPLAY_WIDTH;
        draw_cat(frames[frame], cat_x);
        frame = (frame + 1) % count;
        draw_text(label);
    }
    return false;
}
