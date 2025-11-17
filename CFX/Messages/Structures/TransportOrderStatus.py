from enum import Enum


class TransportOrderStatus(Enum):
    """
    The status of an order to transport goods
    """
    
    # The status is unknown
    Unspecified = "Unspecified"
    
    # The order is awaiting fulfillment
    Pending = "Pending"
    
    # The ordered items are being gathered and readied for transport
    Kitting = "Kitting"
    
    # The ordered items are ready to be transported, but have not yet departed the point of origination
    Kitted = "Kitted"
    
    # The ordered items are in transit
    InTransit = "InTransit"
    
    # The ordered items have been delivered to their final destination
    Delivered = "Delivered"