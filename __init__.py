"""
Binary Ninja plugin that creates a deeplink to the current address and adds it to the clipboard.
"""

from binaryninja.plugin import PluginCommand
from binaryninja.binaryview import BinaryView
from binaryninja.log import log_debug
from PySide6.QtGui import QGuiApplication


def copy_as_deeplink(bv: BinaryView, address: int) -> None:
    """
    Creates a deeplink to the current address and adds it to the clipboard.
    """
    link = f"binaryninja://{bv.file.filename}?expr={hex(address)}"
    clip = QGuiApplication.clipboard()
    clip.setText(link)
    log_debug(f"Copied deeplink: {link}")


PluginCommand.register_for_address(
    "Copy as deeplink",
    "Creates a deeplink to the current address and adds it to the clipboard.",
    copy_as_deeplink,
)
