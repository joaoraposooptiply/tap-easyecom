"""EasyEcom tap class."""

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_easyecom.streams import (
    ProductsStream,
    SuppliersStream,
    SellOrdersStream,
    SellOrderLinesStream,
    BuyOrdersStream,
    BuyOrderLinesStream,
    ReceiptsStream,
    ReceiptLineStream,
    ReturnsStream,
    ReturnLinesStream,
)

STREAM_TYPES = [
    ProductsStream,
    SuppliersStream,
    SellOrdersStream,
    SellOrderLinesStream,
    BuyOrdersStream,
    BuyOrderLinesStream,
    ReceiptsStream,
    ReceiptLineStream,
    ReturnsStream,
    ReturnLinesStream,
]


class TapEasyEcom(Tap):
    """EasyEcom tap class."""

    name = "tap-easyecom"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("auth_token", th.StringType, required=True),
        th.Property("project_ids", th.ArrayType(th.StringType), required=True),
        th.Property("start_date", th.DateTimeType,),
    ).to_dict()

    def discover_streams(self):
        return [stream(self) for stream in STREAM_TYPES]


if __name__ == "__main__":
    TapEasyEcom.cli()
