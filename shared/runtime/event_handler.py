"""
Base event handler class.

All trading services will inherit from this.
"""


class EventHandler:

    def handle(self, event: dict):
        """
        Process incoming event.
        """

        raise NotImplementedError("Handler must implement handle()")
