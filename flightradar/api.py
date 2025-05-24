from __future__ import annotations


def get_flight_data(flight_number: str) -> dict:
    """
    Fetch flight data for a given flight number.

    Args:
        flight_number (str): The flight number to fetch data for.

    Returns:
        dict: A dictionary containing flight data.
    """
    # Placeholder implementation
    return {
        "flight_number": flight_number,
        "status": "On Time",
        "departure": "2023-10-01T12:00:00Z",
        "arrival": "2023-10-01T14:00:00Z",
        "origin": "JFK",
        "destination": "LAX",
    }
