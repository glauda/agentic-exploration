import datetime
from zoneinfo import ZoneInfo

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("time-server")


@mcp.tool()
def get_current_time(city: str) -> str:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        str: The current time in the specified city or an error message.
    """
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return f"Sorry, I don't have timezone information for {city}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


if __name__ == "__main__":
    mcp.run()
