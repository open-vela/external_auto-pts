#
# auto-pts - The Bluetooth PTS Automation Framework
#
# Copyright (c) 2017, Intel Corporation.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

# Generated by h2py.py (CPython 2.7.10) from
# zephyr/tests/bluetooth/tester/src/bttester.h
BTP_MTU = 1024
BTP_INDEX_NONE = 0xff
BTP_SERVICE_ID_CORE = 0
BTP_SERVICE_ID_GAP = 1
BTP_SERVICE_ID_GATT = 2
BTP_SERVICE_ID_L2CAP = 3
BTP_SERVICE_ID_MESH = 4
BTP_STATUS_SUCCESS = 0x00
BTP_STATUS_FAILED = 0x01
BTP_STATUS_UNKNOWN_CMD = 0x02
BTP_STATUS_NOT_READY = 0x03
BTP_STATUS = 0x00
CORE_READ_SUPPORTED_COMMANDS = 0x01
CORE_READ_SUPPORTED_SERVICES = 0x02
CORE_REGISTER_SERVICE = 0x03
CORE_UNREGISTER_SERVICE = 0x04
CORE_EV_IUT_READY = 0x80
GAP_READ_SUPPORTED_COMMANDS = 0x01
GAP_READ_CONTROLLER_INDEX_LIST = 0x02
GAP_SETTINGS_POWERED = 0
GAP_SETTINGS_CONNECTABLE = 1
GAP_SETTINGS_FAST_CONNECTABLE = 2
GAP_SETTINGS_DISCOVERABLE = 3
GAP_SETTINGS_BONDABLE = 4
GAP_SETTINGS_LINK_SEC_3 = 5
GAP_SETTINGS_SSP = 6
GAP_SETTINGS_BREDR = 7
GAP_SETTINGS_HS = 8
GAP_SETTINGS_LE = 9
GAP_SETTINGS_ADVERTISING = 10
GAP_SETTINGS_SC = 11
GAP_SETTINGS_DEBUG_KEYS = 12
GAP_SETTINGS_PRIVACY = 13
GAP_SETTINGS_CONTROLLER_CONFIG = 14
GAP_SETTINGS_STATIC_ADDRESS = 15
GAP_READ_CONTROLLER_INFO = 0x03
GAP_RESET = 0x04
GAP_SET_POWERED = 0x05
GAP_SET_CONNECTABLE = 0x06
GAP_SET_FAST_CONNECTABLE = 0x07
GAP_NON_DISCOVERABLE = 0x00
GAP_GENERAL_DISCOVERABLE = 0x01
GAP_LIMITED_DISCOVERABLE = 0x02
GAP_SET_DISCOVERABLE = 0x08
GAP_SET_BONDABLE = 0x09
GAP_START_ADVERTISING = 0x0a
GAP_STOP_ADVERTISING = 0x0b
GAP_DISCOVERY_FLAG_LE = 0x01
GAP_DISCOVERY_FLAG_BREDR = 0x02
GAP_DISCOVERY_FLAG_LIMITED = 0x04
GAP_DISCOVERY_FLAG_LE_ACTIVE_SCAN = 0x08
GAP_DISCOVERY_FLAG_LE_OBSERVE = 0x10
GAP_START_DISCOVERY = 0x0c
GAP_STOP_DISCOVERY = 0x0d
GAP_CONNECT = 0x0e
GAP_DISCONNECT = 0x0f
GAP_IO_CAP_DISPLAY_ONLY = 0
GAP_IO_CAP_DISPLAY_YESNO = 1
GAP_IO_CAP_KEYBOARD_ONLY = 2
GAP_IO_CAP_NO_INPUT_OUTPUT = 3
GAP_IO_CAP_KEYBOARD_DISPLAY = 4
GAP_SET_IO_CAP = 0x10
GAP_PAIR = 0x11
GAP_UNPAIR = 0x12
GAP_PASSKEY_ENTRY = 0x13
GAP_PASSKEY_CONFIRM = 0x14
GAP_EV_NEW_SETTINGS = 0x80
GAP_DEVICE_FOUND_FLAG_RSSI = 0x01
GAP_DEVICE_FOUND_FLAG_AD = 0x02
GAP_DEVICE_FOUND_FLAG_SD = 0x04
GAP_EV_DEVICE_FOUND = 0x81
GAP_EV_DEVICE_CONNECTED = 0x82
GAP_EV_DEVICE_DISCONNECTED = 0x83
GAP_EV_PASSKEY_DISPLAY = 0x84
GAP_EV_PASSKEY_ENTRY_REQ = 0x85
GAP_EV_PASSKEY_CONFIRM_REQ = 0x86
GAP_EV_IDENTITY_RESOLVED = 0x87
GATT_READ_SUPPORTED_COMMANDS = 0x01
GATT_SERVICE_PRIMARY = 0x00
GATT_SERVICE_SECONDARY = 0x01
GATT_ADD_SERVICE = 0x02
GATT_ADD_CHARACTERISTIC = 0x03
GATT_ADD_DESCRIPTOR = 0x04
GATT_ADD_INCLUDED_SERVICE = 0x05
GATT_SET_VALUE = 0x06
GATT_START_SERVER = 0x07
GATT_SET_ENC_KEY_SIZE = 0x09
GATT_EXCHANGE_MTU = 0x0a
GATT_DISC_PRIM_UUID = 0x0c
GATT_FIND_INCLUDED = 0x0d
GATT_DISC_ALL_CHRC = 0x0e
GATT_DISC_CHRC_UUID = 0x0f
GATT_DISC_ALL_DESC = 0x10
GATT_READ = 0x11
GATT_READ_LONG = 0x13
GATT_READ_MULTIPLE = 0x14
GATT_WRITE_WITHOUT_RSP = 0x15
GATT_SIGNED_WRITE_WITHOUT_RSP = 0x16
GATT_WRITE = 0x17
GATT_WRITE_LONG = 0x18
GATT_CFG_NOTIFY = 0x1a
GATT_CFG_INDICATE = 0x1b
GATT_GET_ATTRIBUTES = 0x1c
GATT_GET_ATTRIBUTE_VALUE = 0x1d
GATT_EV_NOTIFICATION = 0x80
GATT_EV_ATTR_VALUE_CHANGED = 0x81
L2CAP_READ_SUPPORTED_COMMANDS = 0x01
L2CAP_CONNECT = 0x02
L2CAP_DISCONNECT = 0x03
L2CAP_SEND_DATA = 0x04
L2CAP_TRANSPORT_BREDR = 0x00
L2CAP_TRANSPORT_LE = 0x01
L2CAP_LISTEN = 0x05
L2CAP_ACCEPT_CONNECTION = 0x06
L2CAP_EV_CONNECTION_REQ = 0x80
L2CAP_EV_CONNECTED = 0x81
L2CAP_EV_DISCONNECTED = 0x82
L2CAP_EV_DATA_RECEIVED = 0x83
MESH_READ_SUPPORTED_COMMANDS = 0x01
MESH_OUT_BLINK = 0x01
MESH_OUT_BEEP = 0x02
MESH_OUT_VIBRATE = 0x04
MESH_OUT_DISPLAY_NUMBER = 0x08
MESH_OUT_DISPLAY_STRING = 0x10
MESH_IN_PUSH = 0x01
MESH_IN_TWIST = 0x02
MESH_IN_ENTER_NUMBER = 0x04
MESH_IN_ENTER_STRING = 0x08
MESH_CONFIG_PROVISIONING = 0x02
MESH_PROVISION_NODE = 0x03
MESH_INIT = 0x04
MESH_RESET = 0x05
MESH_INPUT_NUMBER = 0x06
MESH_INPUT_STRING = 0x07
MESH_IV_UPDATE_TEST_MODE = 0x08
MESH_IV_UPDATE_TOGGLE = 0x09
MESH_NET_SEND = 0x0a
MESH_HEALTH_ADD_FAULTS = 0x0b
MESH_HEALTH_CLEAR_FAULTS = 0x0c
MESH_LPN_SET = 0x0d
MESH_LPN_POLL = 0x0e
MESH_MODEL_SEND = 0x0f
MESH_LPN_SUBSCRIBE = 0x10
MESH_LPN_UNSUBSCRIBE = 0x11
MESH_RPL_CLEAR = 0x12
MESH_EV_OUT_NUMBER_ACTION = 0x80
MESH_EV_OUT_STRING_ACTION = 0x81
MESH_EV_IN_ACTION = 0x82
MESH_EV_PROVISIONED = 0x83
MESH_PROV_BEARER_PB_ADV = 0x00
MESH_PROV_BEARER_PB_GATT = 0x01
MESH_EV_PROV_LINK_OPEN = 0x84
MESH_EV_PROV_LINK_CLOSED = 0x85
MESH_EV_NET_RECV = 0x86
MESH_EV_INVALID_BEARER = 0x87
