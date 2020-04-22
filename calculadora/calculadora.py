import tkinter as tk
import tkinter.font as tkFont

#Variables
screenSize = { 'width': 480, 'height': 480 }
result = 0

# Main Window
root = tk.Tk()
root.title('Calculadora')
root.minsize( screenSize['width'], screenSize['height'] )
root.resizable( False, False )

#Theme
ThemePalette = {
    "Primary" : "#2c003e",
    "Accent"  : "#fe346e"
    
}

ThemeFonts = {
    "Display" : tkFont.Font( family = 'Calibri', size = 56 ),
    "Numpad"  : tkFont.Font( family = 'Calibri', size = 24)
}

# Seccion Display
seccion_display = tk.Frame( master = root, bg = ThemePalette['Primary'] )
seccion_display.place( anchor = tk.NW, relwidth = 1.0, relheight = 0.2)
seccion_display.place_configure(relx = 0, rely = 0)

# Label Display
label_display = tk.Label(  master = seccion_display, 
    bg = ThemePalette['Primary'],
    fg = "white",
    text = str( result ),
    font = ThemeFonts['Display']
)
label_display.place( anchor = tk.CENTER, rely = 0.5 )
label_display.place_configure( anchor = tk.E, relx = 0.9 )

# Seccion Numpad
seccion_numpad = tk.Frame( master = root, bg = ThemePalette['Accent'])
seccion_numpad.place ( anchor = tk.NW, relwidth = 1.0, relheight = 0.8, relx = 0, rely = 0.2)

# Buttons
calcButtons = {}
ButtonSym = ['0','1', '2','3','4','5','6','7','8','9','+','-','x','÷', '=','.','C','%','+/-']

for sym in ButtonSym:
    calcButtons[sym] = tk.Button( master = seccion_numpad,
        text = sym,
        font = ThemeFonts['Numpad'],
        bg = ThemePalette['Accent']
    )
    calcButtons[sym].place( anchor = tk.NW, relwidth = 1/4, relheight = 1/5)
calcButtons['0'].place_configure( relwidth = 1/2 )

calcButtons['C'].place_configure( relx = 0, rely = 0 )
calcButtons['+/-'].place_configure( relx = 0.25, rely = 0 )
calcButtons['%'].place_configure( relx = 0.5, rely = 0 )
calcButtons['÷'].place_configure( relx = 0.75, rely = 0 )

calcButtons['7'].place_configure( relx = 0, rely = 0.2 )
calcButtons['8'].place_configure( relx = 0.25, rely = 0.2 )
calcButtons['9'].place_configure( relx = 0.5, rely = 0.2 )
calcButtons['x'].place_configure( relx = 0.75, rely = 0.2 )

calcButtons['4'].place_configure( relx = 0, rely = 0.4 )
calcButtons['5'].place_configure( relx = 0.25, rely = 0.4 )
calcButtons['6'].place_configure( relx = 0.5, rely = 0.4 )
calcButtons['-'].place_configure( relx = 0.75, rely = 0.4 )

calcButtons['1'].place_configure( relx = 0, rely = 0.6 )
calcButtons['2'].place_configure( relx = 0.25, rely = 0.6 )
calcButtons['3'].place_configure( relx = 0.5, rely = 0.6 )
calcButtons['+'].place_configure( relx = 0.75, rely = 0.6 )

calcButtons['0'].place_configure( relx = 0, rely = 0.8 )
calcButtons['.'].place_configure( relx = 0.5, rely = 0.8 )
calcButtons['='].place_configure( relx = 0.75, rely = 0.8 )

root.mainloop()