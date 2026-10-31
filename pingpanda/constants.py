"""The texts and the colours that PingPanda prints."""

from colorama import Fore

# Banner
BANNER = """
╔═══════════════════════════════╗
║       StatusChecker.py        ║
║   Created By: BLACK-SCORP10   ║
║   Enanched By: matteocapricci ║
╚═══════════════════════════════╝
"""

# Color Codes
COLORS = {
    "1xx": Fore.WHITE,
    "2xx": Fore.GREEN,
    "3xx": Fore.YELLOW,
    "4xx": Fore.RED,
    "5xx": Fore.LIGHTRED_EX,
    "Invalid": Fore.WHITE,
}

# The order in which the status groups are printed
STATUS_GROUPS = ("1xx", "2xx", "3xx", "4xx", "5xx", "Invalid")
