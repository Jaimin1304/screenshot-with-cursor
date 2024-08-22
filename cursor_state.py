from win32con import (
    IDC_APPSTARTING,
    IDC_ARROW,
    IDC_CROSS,
    IDC_HAND,
    IDC_HELP,
    IDC_IBEAM,
    IDC_ICON,
    IDC_NO,
    IDC_SIZE,
    IDC_SIZEALL,
    IDC_SIZENESW,
    IDC_SIZENS,
    IDC_SIZENWSE,
    IDC_SIZEWE,
    IDC_UPARROW,
    IDC_WAIT,
)

from win32gui import LoadCursor, GetCursorInfo

DEFAULT_CURSORS = {
    LoadCursor(0, IDC_APPSTARTING): "appStarting",
    LoadCursor(0, IDC_ARROW): "Arrow",
    LoadCursor(0, IDC_CROSS): "Cross",
    LoadCursor(0, IDC_HAND): "Hand",
    LoadCursor(0, IDC_HELP): "Help",
    LoadCursor(0, IDC_IBEAM): "IBeam",
    LoadCursor(0, IDC_ICON): "ICon",
    LoadCursor(0, IDC_NO): "No",
    LoadCursor(0, IDC_SIZE): "Size",
    LoadCursor(0, IDC_SIZEALL): "sizeAll",
    LoadCursor(0, IDC_SIZENESW): "sizeNesw",
    LoadCursor(0, IDC_SIZENS): "sizeNs",
    LoadCursor(0, IDC_SIZENWSE): "sizeNwse",
    LoadCursor(0, IDC_SIZEWE): "sizeWe",
    LoadCursor(0, IDC_UPARROW): "upArrow",
    LoadCursor(0, IDC_WAIT): "Wait",
}


def get_current_cursor():
    curr_cursor_handle = GetCursorInfo()[1]
    res = DEFAULT_CURSORS.get(curr_cursor_handle, "None")
    print(res)
    return res


if __name__ == "__main__":
    while True:
        get_current_cursor()
