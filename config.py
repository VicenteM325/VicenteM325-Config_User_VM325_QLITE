# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import subprocess

from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


#Variables
mod = "mod4"
terminal = guess_terminal()
color_barra =  "#212121" 
dispositivo_red = "wlan0"
tamano_barra = 30
tamano_fuente = 15
tamano_icono = 20
fuente_predeterminada = 'Ubuntu Mono Nerd Font'
color_activo = "#f1fa8c"
color_fg = "#ffffff"
color_bg = "#212121"
color_inactivo = "#8f8f90"
color_oscuro = "#44475a"
color_actualizaciones = "#bc0000"
color_ventana_info = "#cbcacf"
color_layout_normal = "#322f3e"
color_layout_focus = "#6b6b6c"
#color_grupo1 = "#AEBBC3" #Color Gris Claro
#color_grupo2 = "#6A828D" #Color Gris Azulado
#color_grupo3 = "#40535B" #Color Gris Oscuro
color_grupo1 = "#2c2c2c" #Color Oscuro
color_grupo2 = "#2c2c2c" #Color Oscuro
color_grupo3 = "#2c2c2c" #Color Oscuro
color_grupo4 = "#2c2c2c" #Color Oscuro


#Funciones

#Funcion para separar elementos
def fc_separador():
    return widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    foreground = color_fg,
                    background = color_bg
                )
# Funcion para crear pestanas argumento 0 izq, argumento 1 der
def fc_pestana(vColor, tipo):
    if tipo == 0:
        icono = ""
    else:
        icono = ""
    return widget.TextBox(
                    text = icono,
                    fontsize = tamano_barra +5,
                    foreground = vColor,
                    background = color_bg,
                    padding = -3

                )

def fc_icono(icono, color_grupo):
    return widget.TextBox(
        text = icono,
        foreground = color_fg,
        background = color_grupo,
        fontsize = tamano_icono
    )

    
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    #Teclas para lanzar menu rofi
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Abrir menu"),
    
    #Teclas para lanzar navegador firefox
    Key([mod], "d", lazy.spawn("firefox"), desc="Lanzar navegador firefox"),
    
    #Teclas para lanzar navegador Brave 
    Key([mod], "b", lazy.spawn("brave"), desc="Lanzar navegador brave"),

    #Teclas para cambiar idioma de teclado
    Key([mod], "i", lazy.spawn("setxkbmap us")),  # Cambiar a inglés
    Key([mod, "shift"], "i", lazy.spawn("setxkbmap es")),  # Cambiar a español

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #Atajo Volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),

    #Brillo de Pantalla
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #Captura de Pantalla
    Key([],"Print", lazy.spawn("scrot")),
    Key([mod],"Print", lazy.spawn("scrot -s")),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

#Listado de iconos nerd font

groups = [Group(i) for i in [
    "  ", "  ", "  ", "  " ,"  ", "  ", "  ", "  ", 
]
]

for i,group in enumerate (groups):
    numeroEscritorio =str(i+1)
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),

            Key(
                [mod], "period", lazy.next_screen(), desc="Move focus to next monitor"
            ),
            Key(
                [mod], "comma", lazy.prev_screen(), desc="Move focus to previous monitor"
            ),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.Columns(
        border_normal=color_layout_normal,
        border_focus=color_layout_focus,
        border_width=4,
        border_normal_stack=color_layout_normal,
        border_focus_stack=color_layout_focus,
        border_on_single=2,
        margin=5,
        margin_on_single=10,
    ),
    #layout.MonadTall(
    #    border_normal=color_layout_normal,
    #    border_focus=color_layout_focus,
    #    margin=10,
    #    border_width=3,
    #    single_border_width=2,
    #    single_margin=10,
    #),
    #layout.VerticalTile(
    #    border_normal=color_layout_normal,
    #    border_focus=color_layout_focus,
    #    border_width=4,
    #    border_on_single=2,
    #    margin=5,
    #    margin_on_single=10,
    #),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente_predeterminada,
    fontsize=tamano_fuente,
    padding=3,
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    disable_drag = True,
                    fontsize = tamano_icono,
                    foreground = color_fg,
                    highlight_method = 'block',
                    inactive = color_inactivo,
                    other_current_screen_border = color_oscuro,
                    other_screen_border = color_oscuro,
                    padding_x = 0,
                    padding_y = 10,
                ),
                fc_separador(),
                widget.Prompt(),
                widget.WindowName(
                    foreground = color_ventana_info,
                    background = color_bg,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    icon_size = tamano_icono,
                    background = color_bg
                ),
                fc_separador(),
                # Bateria
                widget.Battery(
                format="{char} {percent:2.0%}",
                discharge_char='↓',
                charge_char='↑',
                low_foreground='ff0000',
                ),
                fc_separador(),
                # Pestana grupo 1
               fc_pestana(color_grupo1, 0),
               fc_icono("", color_grupo1),
               widget.ThermalSensor(
                foreground = color_fg,
                background = color_grupo1,
                threshold = 50,
                tag_sensor = "Core 0",
                fmt = 'T1:{}'
               ),
               widget.ThermalSensor(
                foreground = color_fg,
                background = color_grupo1,
                threshold = 50,
                tag_sensor = "Core 1",
                fmt = 'T2:{}'
               ),
               fc_icono(" ", color_grupo1),
               widget.Memory(
                foreground = color_fg,
                background = color_grupo1,
               ),
               fc_pestana(color_grupo1, 1),
               fc_separador(),
                #Fin pestana grupo 1

                #Inicio pestana grupo 2
                fc_pestana(color_grupo2, 0),
                fc_icono("  ", color_grupo2),
                widget.CheckUpdates(
                    background = color_grupo2,
                    colour_have_updates = color_actualizaciones,
                    colour_no_updates = color_fg,
                    no_update_string = '0',
                    display_format = '{updates}',
                    update_interval = 1800,
                    distro='Arch_checkupdates'
                ),
                fc_icono("   ", color_grupo2),
                widget.Net(
                    foreground = color_fg,
                    background = color_grupo2,
                    format = '{down}     {up}',
                    interface = dispositivo_red,
                    use_bits = 'true'
                ),
                fc_pestana(color_grupo2, 1),
                fc_separador(),
                #Fin pestana grupo 2

                #Inicio pestana grupo 3
                fc_pestana(color_grupo3, 0),
                widget.Clock(
                    background = color_grupo3,
                    foreground = color_fg,
                    format="%Y-%m-%d %A %I:%M %p"
                
                ),
                fc_icono("",color_grupo3),
                widget.Volume(
                    foreground = color_fg,
                    background = color_grupo3,
                    limit_max_volume = True,
                    fontsize = tamano_fuente,
                ),
                fc_pestana(color_grupo3,1),
                fc_separador(),
                #Fin pestana grupo 3

                #Inicio pestana grupo 4
                fc_pestana(color_grupo4, 0),
                widget.CurrentLayoutIcon(
                    foreground = color_fg,
                    background = color_grupo4,
                    scale = 0.6,
                ),
                widget.CurrentLayout(
                    foreground = color_fg,
                    background = color_grupo4,
                ),
                fc_pestana(color_grupo4, 1),
                fc_separador(),
                #Fin pestana grupo 4

            ],
            tamano_barra,
            background = color_barra,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

qtile.mouse = mouse

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]

)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])
    picom_conf_path = os.path.expanduser("~/.config/picom/picom.conf")
    subprocess.Popen(['picom', '--config', picom_conf_path])