set fish_greeting ""

export EDITOR='nvim'
export VISUAl='nvim'
export BROWSER='qutebrowser'
export TERMINAL='kitty'
export XDG_SESSION_TYPE=wayland
export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
export DEVKITPRO=/opt/devkitpro
export DEVKITARM=/opt/devkitpro/devkitARM
export DEVKITPPC=/opt/devkitpro/devkitPPC

fish_add_path /lib/emscripten
fish_add_path /home/cadence/.cargo/bin

if status is-login
    if test -z "$WAYLAND_DISPLAY" -a "$XDG_VTNR"
    dbus-run-session river
    end
end
