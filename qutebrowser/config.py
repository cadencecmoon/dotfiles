# config.py
#
# NOTE: config.py is intended for advanced users who are comfortable
# with manually migrating the config file on qutebrowser upgrades. If
# you prefer, you can also configure qutebrowser using the
# :set/:bind/:config-* commands without having to write a config.py
# file.
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103

config.load_autoconfig(False)

c.auto_save.session = True

# Format of timestamps (e.g. for the history completion).
c.completion.timestamp_format = '%d-%m-%Y %H:%M'

# Confirm quit if downloading
c.confirm_quit = ["downloads"]

# Download locations
c.downloads.location.directory = "~/Downloads"

c.url.searchengines = {'DEFAULT': 'https://www.google.com/search?q={}', 
                       'duck': 'https://start.duckduckgo.com/?q={}',
                       'aw': 'https://wiki.archlinux.org/?search={}',
                       'goog': 'https://www.google.com/search?q={}',
                       're': 'https://www.reddit.com/search?q={}',
                       # Go to a given subreddit
                       'sr': 'https://www.reddit.com/r/{unquoted}',
                       'gh': 'https://github.com/search?q={}',
                       # Jumpt to github repo or user
                       'ghr': 'https://github.com/{unquoted}',
                       'wiki': 'https://en.wikipedia.org/wiki/{}',
                       'yt': 'https://www.youtube.com/results?search_query={}'}

c.url.default_page = 'https://start.duckduckgo.com'

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
c.content.cookies.accept = 'all'

# Value to send in the Accept-Language header
c.content.headers.accept_language = 'en-US,pl-PL;q=0.9'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString

# Original that I setup but cloudflare gives issues logging into GitLab
# c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) QtWebEngine/{qt_version} qutebrowser/{qutebrowser_version} Chromium/{upstream_browser_version}'

# Set Chromium back to 67.0.1 so I can sign in to GitLab due to cloudflare issues
c.content.headers.user_agent = 'Mozilla/5.0 ({os_info}) QtWebEngine/{qt_version} qutebrowser/{qutebrowser_version} Chromium/67.0.1'

# Load images automatically in web pages.
# Type: Bool
c.content.images = True

# Enable JavaScript.
# Type: Bool
c.content.javascript.enabled = True

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.notifications.enabled = 'ask'

# Allow websites to register protocol handlers via
# `navigator.registerProtocolHandler`.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.register_protocol_handler = 'ask'

c.editor.command = ['foot', '-e', 'nvim', '{file}', '-c', 'normal {line}G{column0}l']

c.fileselect.multiple_files.command = ['foot', '-e', 'ranger', '--choosefiles={}']

c.fileselect.folder.command = ['foot', '-e', 'ranger', '--choosedir={}']

#c.spellcheck.languages = ['en-US','pl-PL']

c.tabs.padding = {'bottom': 4, 'left': 5, 'right': 5, 'top': 2}

c.tabs.select_on_remove = 'prev'

c.fonts.default_family = 'Agave Nerd Font'
c.fonts.default_size = '10pt'
c.fonts.web.family.standard = 'Agave Nerd Font'
c.fonts.web.size.default = 14

# Font used for the context menu. If set to null, the Qt default is
# used.
# Type: Font
c.fonts.contextmenu = 'default_size default_family'

config.bind(',M', 'hint links spawn mpv {hint-url}')
config.bind('xb', 'config-cycle statusbar.show never always')
config.bind('xt', 'config-cycle tabs.show never always ')
config.bind('xx', 'config-cycle statusbar.show never always;; config-cycle tabs.show never always ')

# Custom stylesheet for qt to set tab mouse hover info window font size
c.qt.args += ['stylesheet=/home/cadence/.config/qutebrowser/stylesheet.qss']

c.content.autoplay = False
config.source('gruvbox.py')
