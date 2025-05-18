# Copy as deeplink
Author: pathtofile

Binary Ninja plugin that creates a deeplink to the current address and adds it to the clipboard. Example deeplink:
```
binaryninja:///path/to/binary.bndb?expr=0x40369e
```

The link can then be saved into an external Wiki, notebook, etc. Binary Ninja automatically installs a link handler at install time, so you just need to 'open' the link in a browser or from the commandline
and it will open the right database as the correct location.

## License
This plugin is released under an [MIT license](./license).
