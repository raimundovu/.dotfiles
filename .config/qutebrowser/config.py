pnight = {
    'background': '#292d3e',
    'background2': '#34324a',
    'highlight': '#444267',
    'gray': '#676e95',
    'foreground': '#a6accd',
    'white': '#eeffff',
    'cyan': '#89ddff',
    'blue': '#82aaff',
    'red': '#f07178',
    'orange': '#f78c6c',
    'yellow': '#ffcb6b',
    'green': '#c3e88d',
    'magenta': '#c792ea',
}

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = pnight['background']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = pnight['background']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = pnight['background']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = pnight['white']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = pnight['background2']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = pnight['background2']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = pnight['foreground']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = pnight['gray']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = pnight['gray']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = pnight['gray']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = pnight['white']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = pnight['yellow']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = pnight['background2']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = pnight['white']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = pnight['background']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = pnight['red']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = pnight['white']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = pnight['magenta']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = pnight['yellow']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = pnight['background']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = pnight['blue']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = pnight['background2']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = pnight['white']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = pnight['yellow']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = pnight['red']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = pnight['red']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = pnight['white']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = pnight['cyan']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = pnight['cyan']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = pnight['white']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = pnight['orange']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = pnight['orange']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = pnight['white']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = pnight['highlight']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + pnight['background']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = pnight['white']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = pnight['gray']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = pnight['magenta']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = pnight['white']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = pnight['magenta']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = pnight['white']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = pnight['highlight']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = pnight['white']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = pnight['highlight']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = pnight['white']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = pnight['green']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = pnight['background2']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = pnight['background']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = pnight['white']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = pnight['blue']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = pnight['white']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = pnight['gray']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = pnight['white']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = pnight['white']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = pnight['red']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = pnight['white']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = pnight['cyan']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = pnight['white']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = pnight['green']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = pnight['orange']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = pnight['gray']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = pnight['background']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = pnight['white']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = pnight['red']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = pnight['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = pnight['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = pnight['background']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = pnight['white']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = pnight['gray']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = pnight['white']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = pnight['gray']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = pnight['white']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'
pnight = {
    'background': '#292d3e',
    'background2': '#34324a',
    'highlight': '#444267',
    'gray': '#676e95',
    'foreground': '#a6accd',
    'white': '#eeffff',
    'cyan': '#89ddff',
    'blue': '#82aaff',
    'red': '#f07178',
    'orange': '#f78c6c',
    'yellow': '#ffcb6b',
    'green': '#c3e88d',
    'magenta': '#c792ea',
}

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = pnight['background']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = pnight['background']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = pnight['background']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = pnight['white']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = pnight['background2']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = pnight['background2']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = pnight['foreground']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = pnight['gray']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = pnight['gray']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = pnight['gray']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = pnight['white']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = pnight['yellow']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = pnight['background2']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = pnight['white']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = pnight['background']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = pnight['red']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = pnight['white']

## Color gradient stop for download backgrounds.
## Type: QtColor
c.colors.downloads.stop.bg = pnight['magenta']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = pnight['yellow']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = pnight['background']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = pnight['blue']

## Background color of the keyhint widget.
## Type: QssColor
c.colors.keyhint.bg = pnight['background2']

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = pnight['white']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = pnight['yellow']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = pnight['red']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = pnight['red']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = pnight['white']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = pnight['cyan']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = pnight['cyan']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = pnight['white']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = pnight['orange']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = pnight['orange']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = pnight['white']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = pnight['highlight']

# ## Border used around UI elements in prompts.
# ## Type: String
c.colors.prompts.border = '1px solid ' + pnight['background']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = pnight['white']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = pnight['gray']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = pnight['magenta']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = pnight['white']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = pnight['magenta']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = pnight['white']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = pnight['highlight']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = pnight['white']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = pnight['highlight']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = pnight['white']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = pnight['green']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = pnight['background2']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = pnight['background']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = pnight['white']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = pnight['blue']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = pnight['white']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = pnight['gray']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = pnight['white']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = pnight['white']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = pnight['red']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = pnight['white']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = pnight['cyan']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = pnight['white']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = pnight['green']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = pnight['orange']

## Background color of the tab bar.
## Type: QtColor
c.colors.tabs.bar.bg = pnight['gray']

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = pnight['background']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = pnight['white']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = pnight['red']

## Color gradient start for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.start = pnight['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
# c.colors.tabs.indicator.stop = pnight['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = pnight['background']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = pnight['white']

# ## Background color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.bg = pnight['gray']

# ## Foreground color of selected even tabs.
# ## Type: QtColor
c.colors.tabs.selected.even.fg = pnight['white']

# ## Background color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.bg = pnight['gray']

# ## Foreground color of selected odd tabs.
# ## Type: QtColor
c.colors.tabs.selected.odd.fg = pnight['white']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'

