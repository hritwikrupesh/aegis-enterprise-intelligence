import json

from google.cloud import pubsub_v1
from app.cloud.cloud_event_processor import CloudEventProcessor


class PubSubSubscriber:
    """
    Receives enterprise events from Google Cloud Pub/Sub.
    """

    def __init__(self):

        self.project_id = "aegis-501914"

        self.subscription_id = "enterprise-events-test"

        self.subscriber = pubsub_v1.SubscriberClient()

        self.subscription_path = self.subscriber.subscription_path(
            self.project_id,
            self.subscription_id,
        )
        self.processor = CloudEventProcessor()

    def pull_messages(self):

        response = self.subscriber.pull(
            request={
                "subscription": self.subscription_path,
                "max_messages": 10,
            }
        )

        if not response.received_messages:
            print("No messages available.")
            return

        ack_ids = []

        for received in response.received_messages:

            message = received.message.data.decode("utf-8")

            print("\nReceived Message")
            print("-" * 50)

            event = self.processor.process(message)

            print(event)

            ack_ids.append(received.ack_id)

        self.subscriber.acknowledge(
            request={
                "subscription": self.subscription_path,
                "ack_ids": ack_ids,
            }
        )

        print(f"\nAcknowledged {len(ack_ids)} message(s).")