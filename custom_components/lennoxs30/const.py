"""Constants used by the integration"""
from typing import Final


CONF_FAST_POLL_INTERVAL = "fast_scan_interval"
CONF_FAST_POLL_COUNT = "fast_scan_count"
CONF_ALLERGEN_DEFENDER_SWITCH = "allergen_defender_switch"
CONF_APP_ID = "app_id"
CONF_INIT_WAIT_TIME = "init_wait_time"
CONF_CREATE_SENSORS = "create_sensors"
CONF_CREATE_INVERTER_POWER = "create_inverter_power"
CONF_CREATE_DIAGNOSTICS_SENSORS = "create_diagnostic_sensors"
CONF_PII_IN_MESSAGE_LOGS = "pii_in_message_logs"
CONF_MESSAGE_DEBUG_LOGGING = "message_debug_logging"
CONF_LOG_MESSAGES_TO_FILE = "log_messages_to_file"
CONF_MESSAGE_DEBUG_FILE = "message_debug_file"
CONF_CLOUD_CONNECTION = "cloud_connection"
CONF_LOCAL_CONNECTION = "local_connection"
CONF_CREATE_PARAMETERS = "create_parameters"

DEFAULT_CLOUD_TIMEOUT = 60
DEFAULT_LOCAL_TIMEOUT = 30

LENNOX_DEFAULT_CLOUD_APP_ID = "mapp079372367644467046827001"
LENNOX_DEFAULT_LOCAL_APP_ID = "homeassistant"

MANAGER = "manager"

LENNOX_DOMAIN = "lennoxs30"
LENNOX_MFG = "Lennox"

UNIQUE_ID_SUFFIX_DIAG_SENSOR: Final = "DS"
UNIQUE_ID_SUFFIX_EQ_PARAM_NUMBER: Final = "EPN"
UNIQUE_ID_SUFFIX_EQ_PARAM_SELECT: Final = "EPS"
UNIQUE_ID_SUFFIX_INTENET_STATUS_SENSOR: Final = "_INT_STAT"
UNIQUE_ID_SUFFIX_RELAY_STATUS_SENSOR: Final = "_REL_STAT"
UNIQUE_ID_SUFFIX_TIMED_VENTILATION_NUMBER: Final = "_TIMED_VENT"
UNIQUE_ID_SUFFIX_CLOUD_CONNECTED_SENSOR: Final = "_CLOUD_STAT"
UNIQUE_ID_SUFFIX_PARAMETER_SAFETY_SWITCH: Final = "_SW_PAR_SAFE"
UNIQUE_ID_SUFFIX_PARAMETER_UPDATE_BUTTON: Final = "_BUT_PU"
UNIQUE_ID_SUFFIX_ALERT_SENSOR: Final = "_ALERT"
UNIQUE_ID_SUFFIX_ACTIVE_ALERTS_SENSOR: Final = "_ACTIVE_ALERTS"
UNIQUE_ID_SUFFIX_HP_LOW_AMBIENT_LOCKOUT: Final = "_HP_LOW_AMB_LO"
UNIQUE_ID_SUFFIX_AUX_HI_AMBIENT_LOCKOUT: Final = "_AUX_HI_AMB_LO"
UNIQUE_ID_SUFFIX_RESET_SMART_HUB: Final = "_RESET_SMART_HUB"

VENTILATION_EQUIPMENT_ID = -900
