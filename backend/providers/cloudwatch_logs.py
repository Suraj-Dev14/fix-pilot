import os
import boto3

from dotenv import load_dotenv

load_dotenv()

from .logs import LogProvider


class CloudWatchLogProvider(LogProvider):
    """Log provider backed by AWS CloudWatch Logs."""

    def __init__(self, log_group: str):
        self.log_group = log_group
        self.region_name = os.getenv("AWS_DEFAULT_REGION")
        self.client = boto3.client(
            "logs",
            region_name=self.region_name,
        )

    def search(
        self,
        service: str,
        search_term: str,
        start_time: int | None = None,
        end_time: int | None = None,
    ) -> list[dict]:
        results = []

        request = {
            "logGroupName": self.log_group,
            "filterPattern": search_term,
        }

        if start_time is not None:
            request["startTime"] = start_time

        if end_time is not None:
            request["endTime"] = end_time

        while True:

            response = self.client.filter_log_events(**request)

            for event in response.get("events", []):
                results.append(
                    {
                        "service": service,
                        "timestamp": event.get("timestamp"),
                        "message": event.get("message", ""),
                        "log_stream": event.get("logStreamName"),
                        "event_id": event.get("eventId"),
                    }
                )

            next_token = response.get("nextToken")

            if not next_token:
                break

            request["nextToken"] = next_token

        return results