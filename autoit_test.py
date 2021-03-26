import autoit
import time

XTU_UI_LAUNCHER_PATH    = r'C:\Program Files\Intel\Intel(R) Extreme Tuning Utility\Client\XtuUiLauncher.exe'
#autoit.run(XTU_UI_LAUNCHER_PATH)
autoit.win_active("Intel® Extreme Tuning Utility")
a = autoit.win_get_pos("Intel® Extreme Tuning Utility")
x = a[0]
y = a[1]
print(a)
time.sleep(1)
#autoit.control_click("[Class:#32770]", "Button2")
#autoit.win_activate_by_handle("HwndWrapper[PerfTune.exe;;af8861d2-4c46-45c8-8afc-bcd2ab7efcdb]")

autoit.mouse_click("left",x + 63, y + 205)
time.sleep(1)
autoit.mouse_click("left",x + 243, y + 129)
time.sleep(1)
# Days
#autoit.mouse_click("left",x + 558, y + 133)
autoit.mouse_click("left",x + 755, y + 135)
time.sleep(1)
autoit.mouse_click("left",x + 303, y + 331)

