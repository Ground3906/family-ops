#Requires AutoHotkey v2.0

^+t:: {
    now := FormatTime(, "dddd, MMMM d, yyyy") . " at " . FormatTime(, "HH:mm")
    SendText("[Context: Current date/time is " now "]")
}