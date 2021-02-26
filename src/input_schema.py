from schema import Schema, Optional, Regex, Or

class InputSchema:

    schema = Schema({
        "id": str,
        "received_at": Regex(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}'),
        "anonymous_id": str,
        Optional("context_app_version"): str,
        Optional("context_device_ad_tracking_enabled"): bool,
        "context_device_manufacturer": str,
        "context_device_model": str,
        "context_device_type": str,
        "context_locale": str,
        Optional("context_library_name"): str,
        Optional("context_library_version"): str,
        "context_network_wifi": bool,
        "context_os_name": str,
        Optional("context_timezone"): str,
        "event": str,
        "event_text": str,
        "original_timestamp": Regex(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\+\d{4}'),
        "sent_at": Regex(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}'),
        "timestamp": Regex(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{6}'),
        Optional("user_id"): str,
        "context_network_carrier": str,
        Optional("context_device_token"): Or(str, None),
        "context_traits_taxfix_language": str
    })
