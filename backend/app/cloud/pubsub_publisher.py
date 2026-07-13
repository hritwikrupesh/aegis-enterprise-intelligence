import json

from google.cloud import pubsub_v1

from app.domain.entities.enterprise_event import EnterpriseEvent


class PubSubPublisher:
    """
    Publishes enterprise events to Google Cloud Pub/Sub.
    """

    def __init__(self):

        self.project_id = "aegis-501914"

        self.topic_id = "enterprise-events"

        self.publisher = pubsub_v1.PublisherClient()

        self.topic_path = self.publisher.topic_path(
            self.project_id,
            self.topic_id,
        )

    def publish(
        self,
        event: EnterpriseEvent,
    ) -> None:

        message = event.to_json().encode("utf-8")

        future = self.publisher.publish(
            self.topic_path,
            message,
        )

        print(
            f"Published message: {future.result()}"
        )