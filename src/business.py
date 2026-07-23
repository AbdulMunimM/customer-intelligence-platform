"""
Business logic for customer segments.
"""

CLUSTER_INFO = {

    0: {
        "name": "Lost Customers",
        "description": (
            "Customers who have not purchased for a long time, "
            "buy infrequently, and spend very little."
        ),
        "recommendation": (
            "Launch win-back campaigns, discount offers, "
            "and personalized emails."
        ),
        "priority": "Low"
    },

    1: {
        "name": "Active Customers",
        "description": (
            "Customers who purchase regularly with moderate spending."
        ),
        "recommendation": (
            "Encourage repeat purchases using loyalty programs "
            "and personalized recommendations."
        ),
        "priority": "Medium"
    },

    2: {
        "name": "VIP Customers",
        "description": (
            "Most valuable customers with high purchase frequency "
            "and high spending."
        ),
        "recommendation": (
            "Offer premium services, exclusive discounts, "
            "early product access, and reward programs."
        ),
        "priority": "Highest"
    },

    3: {
        "name": "At-Risk Customers",
        "description": (
            "Previously valuable customers whose activity has declined."
        ),
        "recommendation": (
            "Send targeted promotions and re-engagement campaigns "
            "before they become inactive."
        ),
        "priority": "High"
    }

}

def get_cluster_info(cluster_id):
    """
    Return business information for a cluster.
    """

    return CLUSTER_INFO.get(
        cluster_id,
        {
            "name": "Unknown",
            "description": "",
            "recommendation": "",
            "priority": ""
        }
    )

def print_cluster_info(cluster_id):
    """
    Print business interpretation of a cluster.
    """

    info = get_cluster_info(cluster_id)

    print("=" * 60)

    print(f"Segment: {info['name']}")

    print()

    print(f"Description : {info['description']}")

    print()

    print(f"Recommendation : {info['recommendation']}")

    print()

    print(f"Business Priority : {info['priority']}")

    print("=" * 60)

SEGMENT_COLORS = {

    0: "#D9534F",      # Red

    1: "#5BC0DE",      # Blue

    2: "#5CB85C",      # Green

    3: "#F0AD4E"       # Orange

}

SEGMENT_EMOJIS = {

    0: "😴",

    1: "🙂",

    2: "👑",

    3: "⚠️"

}

def get_segment_display(cluster_id):
    """
    Return formatted segment label.
    """

    info = get_cluster_info(cluster_id)

    emoji = SEGMENT_EMOJIS.get(cluster_id, "")

    return f"{emoji} {info['name']}"

