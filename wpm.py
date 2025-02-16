import curses
from curses import wrapper
import time

def start_screen(stdscr):
    #clears the screen
    stdscr.clear()
    
    #Add the text "Hello." at the top left corner
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to start the test: ")
    
    #Refresh the screen to show the changes
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    
    # Display the WPM in a fixed position
    stdscr.addstr(1,0,f"Word per minute(WPM): {wpm}")  
    
    # Display the current text with color for correct/incorrect characters
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0,i,char, color)
            
   
def wpm_test(stdscr):
    target_text = "The quick brown fox jumps over the lazy dog while the birds fly high above the trees."
    current_text = [ ]
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True) #set to non blocking mode
    
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        
        #Calculate wpm
        wpm = round(len(current_text) / (time_elapsed / 60) / 5)
        
        
        stdscr.clear()
        display_text(stdscr, target_text, current_text,wpm)
        stdscr.refresh()
        
        # Check if user has typed enough characters
        if  len(current_text) >= len(target_text):
            stdscr.nodelay(False)
            break
        
        try:
            key = stdscr.getkey()
        
        except:
            continue
        
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
           if len(current_text) > 0:
               current_text.pop()
        elif len(current_text) < len(target_text):       
            current_text.append(key)
        
        
        
def main(stdscr):
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    while True:
        start_screen(stdscr)
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You comleted the text. Press any key to start again, or ESC to exit.")
        key = stdscr.getkey()
        if ord(key) == stdscr.getkey():
            break
    
#Call the wrapper function to initialize curses and start the main function
wrapper(main)