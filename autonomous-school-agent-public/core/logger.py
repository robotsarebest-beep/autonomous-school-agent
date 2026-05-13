import sys
from rich.console import Console
from rich.logging import RichHandler
import logging

console = Console()

def setup_logger():
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True, console=console)]
    )
    return logging.getLogger("autonomous-school-agent")

logger = setup_logger()

def info(msg):
    logger.info(msg)

def error(msg):
    logger.error(msg)

def success(msg):
    console.print(f"[bold green]✔[/bold green] {msg}")

def warn(msg):
    logger.warning(msg)
