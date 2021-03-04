#!/usr/bin/env python

import Common.Globals as Globals
import wx
import wx.adv

from datetime import datetime, timezone
from dateutil import tz

from esperclient.models.v0_command_args import V0CommandArgs
from esperclient.models.v0_command_schedule_args import V0CommandScheduleArgs


class CommandDialog(wx.Dialog):
    def __init__(self, title, value="{\n\n}"):
        super(CommandDialog, self).__init__(
            None,
            wx.ID_ANY,
            size=(400, 200),
            style=wx.DEFAULT_DIALOG_STYLE
            | wx.STAY_ON_TOP
            | wx.OK
            | wx.CANCEL
            | wx.RESIZE_BORDER,
        )
        self.SetTitle("Create Command")

        sizer_1 = wx.FlexGridSizer(3, 1, 0, 0)

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        grid_sizer_1 = wx.FlexGridSizer(1, 3, 0, 0)

        self.command = wx.Panel(self.panel_1, wx.ID_ANY)
        grid_sizer_1.Add(self.command, 1, wx.ALL | wx.EXPAND, 3)

        sizer_12 = wx.StaticBoxSizer(
            wx.StaticBox(self.command, wx.ID_ANY, "Command Arguements"), wx.VERTICAL
        )

        self.panel_18 = wx.Panel(self.command, wx.ID_ANY)
        sizer_12.Add(self.panel_18, 1, wx.EXPAND, 0)

        grid_sizer_2 = wx.FlexGridSizer(4, 1, 0, 0)

        self.panel_5 = wx.Panel(self.panel_18, wx.ID_ANY)
        grid_sizer_2.Add(self.panel_5, 1, wx.ALL | wx.EXPAND, 2)

        grid_sizer_5 = wx.GridSizer(1, 2, 0, 0)

        self.panel_6 = wx.Panel(self.panel_5, wx.ID_ANY)
        grid_sizer_5.Add(self.panel_6, 1, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.VERTICAL)

        label_4 = wx.StaticText(self.panel_6, wx.ID_ANY, "Command Type")
        sizer_6.Add(label_4, 0, 0, 0)

        self.choice_1 = wx.Choice(
            self.panel_6, wx.ID_ANY, choices=Globals.COMMAND_TYPES
        )
        self.choice_1.SetSelection(-1)
        sizer_6.Add(self.choice_1, 0, wx.EXPAND, 0)

        self.panel_7 = wx.Panel(self.panel_5, wx.ID_ANY)
        grid_sizer_5.Add(self.panel_7, 1, wx.EXPAND | wx.LEFT, 2)

        sizer_7 = wx.BoxSizer(wx.VERTICAL)

        label_5 = wx.StaticText(self.panel_7, wx.ID_ANY, "Package Name")
        sizer_7.Add(label_5, 0, 0, 0)

        self.text_ctrl_2 = wx.TextCtrl(self.panel_7, wx.ID_ANY, "")
        self.text_ctrl_2.Enable(False)
        sizer_7.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)

        self.panel_4 = wx.Panel(self.panel_18, wx.ID_ANY)
        grid_sizer_2.Add(self.panel_4, 1, wx.ALL | wx.EXPAND, 2)

        grid_sizer_4 = wx.GridSizer(1, 2, 0, 0)

        self.panel_8 = wx.Panel(self.panel_4, wx.ID_ANY)
        grid_sizer_4.Add(self.panel_8, 1, wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        label_3 = wx.StaticText(self.panel_8, wx.ID_ANY, "App Version Id")
        sizer_5.Add(label_3, 0, 0, 0)

        self.text_ctrl_3 = wx.TextCtrl(self.panel_8, wx.ID_ANY, "")
        self.text_ctrl_3.Enable(False)
        sizer_5.Add(self.text_ctrl_3, 0, wx.EXPAND, 0)

        self.panel_9 = wx.Panel(self.panel_4, wx.ID_ANY)
        grid_sizer_4.Add(self.panel_9, 1, wx.EXPAND | wx.LEFT, 2)

        sizer_8 = wx.BoxSizer(wx.VERTICAL)

        label_6 = wx.StaticText(self.panel_9, wx.ID_ANY, "App State")
        sizer_8.Add(label_6, 0, 0, 0)

        self.choice_2 = wx.Choice(
            self.panel_9, wx.ID_ANY, choices=["", "Show", "Hide", "Disable"]
        )
        self.choice_2.Enable(False)
        self.choice_2.SetSelection(0)
        sizer_8.Add(self.choice_2, 0, wx.EXPAND, 0)

        self.panel_3 = wx.Panel(self.panel_18, wx.ID_ANY)
        grid_sizer_2.Add(self.panel_3, 1, wx.ALL | wx.EXPAND, 2)

        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)

        self.panel_10 = wx.Panel(self.panel_3, wx.ID_ANY)
        grid_sizer_3.Add(self.panel_10, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)

        label_2 = wx.StaticText(self.panel_10, wx.ID_ANY, "Device State")
        sizer_4.Add(label_2, 0, 0, 0)

        self.choice_3 = wx.Choice(
            self.panel_10, wx.ID_ANY, choices=["", "Unlocked", "Locked"]
        )
        self.choice_3.Enable(False)
        self.choice_3.SetSelection(0)
        sizer_4.Add(self.choice_3, 0, wx.EXPAND, 0)

        self.panel_11 = wx.Panel(self.panel_3, wx.ID_ANY)
        grid_sizer_3.Add(self.panel_11, 1, wx.EXPAND | wx.LEFT, 2)

        sizer_9 = wx.BoxSizer(wx.VERTICAL)

        label_7 = wx.StaticText(self.panel_11, wx.ID_ANY, "Lock Message")
        sizer_9.Add(label_7, 0, 0, 0)

        self.text_ctrl_4 = wx.TextCtrl(self.panel_11, wx.ID_ANY, "")
        self.text_ctrl_4.Enable(False)
        sizer_9.Add(self.text_ctrl_4, 0, wx.EXPAND, 0)

        self.panel_2 = wx.Panel(self.panel_18, wx.ID_ANY)
        grid_sizer_2.Add(self.panel_2, 1, wx.ALL | wx.EXPAND, 2)

        sizer_3 = wx.FlexGridSizer(2, 1, 0, 0)

        label_1 = wx.StaticText(self.panel_2, wx.ID_ANY, "Custom Config:")
        sizer_3.Add(label_1, 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(
            self.panel_2, wx.ID_ANY, "", style=wx.TE_BESTWRAP | wx.TE_MULTILINE
        )
        sizer_3.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)

        static_line_2 = wx.StaticLine(self.panel_1, wx.ID_ANY, style=wx.LI_VERTICAL)
        grid_sizer_1.Add(static_line_2, 0, wx.ALL | wx.EXPAND, 2)

        self.schedule = wx.Panel(self.panel_1, wx.ID_ANY)
        grid_sizer_1.Add(self.schedule, 1, wx.ALL | wx.EXPAND, 3)

        sizer_10 = wx.StaticBoxSizer(
            wx.StaticBox(self.schedule, wx.ID_ANY, "Schedule Arguements"), wx.VERTICAL
        )

        self.panel_13 = wx.Panel(self.schedule, wx.ID_ANY)
        sizer_10.Add(self.panel_13, 1, wx.EXPAND, 0)

        grid_sizer_6 = wx.FlexGridSizer(5, 1, 0, 0)

        self.panel_14 = wx.Panel(self.panel_13, wx.ID_ANY)
        grid_sizer_6.Add(self.panel_14, 1, wx.EXPAND, 0)

        sizer_11 = wx.BoxSizer(wx.VERTICAL)

        label_9 = wx.StaticText(self.panel_14, wx.ID_ANY, "Type")
        sizer_11.Add(label_9, 0, 0, 0)

        self.choice_4 = wx.Choice(
            self.panel_14, wx.ID_ANY, choices=["Window", "Reocurring", "Immediate"]
        )
        self.choice_4.SetSelection(0)
        sizer_11.Add(self.choice_4, 0, wx.EXPAND, 0)

        self.panel_15 = wx.Panel(self.panel_13, wx.ID_ANY)
        grid_sizer_6.Add(self.panel_15, 1, wx.EXPAND, 0)

        sizer_13 = wx.BoxSizer(wx.VERTICAL)

        label_10 = wx.StaticText(self.panel_15, wx.ID_ANY, "Time Type")
        sizer_13.Add(label_10, 0, 0, 0)

        self.choice_5 = wx.Choice(
            self.panel_15, wx.ID_ANY, choices=["Device", "Console"]
        )
        self.choice_5.SetSelection(0)
        sizer_13.Add(self.choice_5, 0, wx.EXPAND, 0)

        self.panel_16 = wx.Panel(self.panel_13, wx.ID_ANY)
        grid_sizer_6.Add(self.panel_16, 1, wx.EXPAND, 0)

        grid_sizer_8 = wx.GridSizer(2, 1, 0, 0)

        self.panel_19 = wx.Panel(self.panel_16, wx.ID_ANY)
        grid_sizer_8.Add(self.panel_19, 1, wx.EXPAND, 0)

        grid_sizer_9 = wx.GridSizer(2, 1, 0, 0)

        label_11 = wx.StaticText(self.panel_19, wx.ID_ANY, "Start Datetime")
        grid_sizer_9.Add(label_11, 0, 0, 0)

        self.panel_20 = wx.Panel(self.panel_19, wx.ID_ANY)
        grid_sizer_9.Add(self.panel_20, 1, wx.EXPAND, 0)

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)

        self.datepicker_ctrl_1 = wx.adv.DatePickerCtrl(self.panel_20, wx.ID_ANY)
        sizer_14.Add(self.datepicker_ctrl_1, 0, 0, 0)

        sizer_14.Add((20, 20), 0, wx.EXPAND, 0)

        self.timepicker_ctrl_2 = wx.adv.TimePickerCtrl(self.panel_20, wx.ID_ANY)
        sizer_14.Add(self.timepicker_ctrl_2, 0, 0, 0)

        self.panel_21 = wx.Panel(self.panel_16, wx.ID_ANY)
        grid_sizer_8.Add(self.panel_21, 1, wx.EXPAND, 0)

        grid_sizer_10 = wx.GridSizer(2, 1, 0, 0)

        label_12 = wx.StaticText(self.panel_21, wx.ID_ANY, "End Datetime")
        grid_sizer_10.Add(label_12, 0, 0, 0)

        self.panel_22 = wx.Panel(self.panel_21, wx.ID_ANY)
        grid_sizer_10.Add(self.panel_22, 1, wx.EXPAND, 0)

        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)

        self.datepicker_ctrl_3 = wx.adv.DatePickerCtrl(self.panel_22, wx.ID_ANY)
        sizer_15.Add(self.datepicker_ctrl_3, 0, 0, 0)

        sizer_15.Add((20, 20), 0, wx.EXPAND, 0)

        self.timepicker_ctrl_4 = wx.adv.TimePickerCtrl(self.panel_22, wx.ID_ANY)
        sizer_15.Add(self.timepicker_ctrl_4, 0, 0, 0)

        self.panel_17 = wx.Panel(self.panel_13, wx.ID_ANY)
        grid_sizer_6.Add(self.panel_17, 1, wx.EXPAND, 0)

        grid_sizer_11 = wx.GridSizer(2, 1, 0, 0)

        self.panel_23 = wx.Panel(self.panel_17, wx.ID_ANY)
        grid_sizer_11.Add(self.panel_23, 1, wx.EXPAND, 0)

        grid_sizer_12 = wx.GridSizer(2, 1, 0, 0)

        label_13 = wx.StaticText(self.panel_23, wx.ID_ANY, "Window Start Datetime")
        grid_sizer_12.Add(label_13, 0, 0, 0)

        self.panel_24 = wx.Panel(self.panel_23, wx.ID_ANY)
        grid_sizer_12.Add(self.panel_24, 1, wx.EXPAND, 0)

        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)

        self.datepicker_ctrl_5 = wx.adv.DatePickerCtrl(self.panel_24, wx.ID_ANY)
        sizer_16.Add(self.datepicker_ctrl_5, 0, 0, 0)

        sizer_16.Add((20, 20), 0, wx.EXPAND, 0)

        self.timepicker_ctrl_6 = wx.adv.TimePickerCtrl(self.panel_24, wx.ID_ANY)
        sizer_16.Add(self.timepicker_ctrl_6, 0, 0, 0)

        self.panel_25 = wx.Panel(self.panel_17, wx.ID_ANY)
        grid_sizer_11.Add(self.panel_25, 1, wx.EXPAND, 0)

        grid_sizer_13 = wx.GridSizer(2, 1, 0, 0)

        label_14 = wx.StaticText(self.panel_25, wx.ID_ANY, "Window End Datetime")
        grid_sizer_13.Add(label_14, 0, 0, 0)

        self.panel_26 = wx.Panel(self.panel_25, wx.ID_ANY)
        grid_sizer_13.Add(self.panel_26, 1, wx.EXPAND, 0)

        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)

        self.datepicker_ctrl_7 = wx.adv.DatePickerCtrl(self.panel_26, wx.ID_ANY)
        sizer_17.Add(self.datepicker_ctrl_7, 0, 0, 0)

        sizer_17.Add((20, 20), 0, wx.EXPAND, 0)

        self.timepicker_ctrl_8 = wx.adv.TimePickerCtrl(self.panel_26, wx.ID_ANY)
        sizer_17.Add(self.timepicker_ctrl_8, 0, 0, 0)

        self.panel_12 = wx.Panel(self.panel_13, wx.ID_ANY)
        grid_sizer_6.Add(self.panel_12, 1, wx.EXPAND, 0)

        grid_sizer_7 = wx.FlexGridSizer(2, 1, 0, 0)

        label_8 = wx.StaticText(self.panel_12, wx.ID_ANY, "Days")
        grid_sizer_7.Add(label_8, 0, 0, 0)

        self.check_list_box_1 = wx.CheckListBox(
            self.panel_12,
            wx.ID_ANY,
            choices=[
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ],
            style=wx.LB_MULTIPLE | wx.LB_NEEDED_SB,
        )
        grid_sizer_7.Add(self.check_list_box_1, 0, wx.EXPAND, 0)

        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_1, 0, wx.ALL | wx.EXPAND, 2)

        sizer_2 = wx.StdDialogButtonSizer()
        sizer_1.Add(sizer_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

        self.button_OK = wx.Button(self, wx.ID_OK, "")
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
        sizer_2.AddButton(self.button_CANCEL)

        sizer_2.Realize()

        grid_sizer_7.AddGrowableRow(1)
        grid_sizer_7.AddGrowableCol(0)
        self.panel_12.SetSizer(grid_sizer_7)

        self.panel_26.SetSizer(sizer_17)

        self.panel_25.SetSizer(grid_sizer_13)

        self.panel_24.SetSizer(sizer_16)

        self.panel_23.SetSizer(grid_sizer_12)

        self.panel_17.SetSizer(grid_sizer_11)

        self.panel_22.SetSizer(sizer_15)

        self.panel_21.SetSizer(grid_sizer_10)

        self.panel_20.SetSizer(sizer_14)

        self.panel_19.SetSizer(grid_sizer_9)

        self.panel_16.SetSizer(grid_sizer_8)

        self.panel_15.SetSizer(sizer_13)

        self.panel_14.SetSizer(sizer_11)

        grid_sizer_6.AddGrowableRow(4)
        grid_sizer_6.AddGrowableCol(0)
        self.panel_13.SetSizer(grid_sizer_6)

        self.schedule.SetSizer(sizer_10)

        sizer_3.AddGrowableRow(1)
        sizer_3.AddGrowableCol(0)
        self.panel_2.SetSizer(sizer_3)

        self.panel_11.SetSizer(sizer_9)

        self.panel_10.SetSizer(sizer_4)

        self.panel_3.SetSizer(grid_sizer_3)

        self.panel_9.SetSizer(sizer_8)

        self.panel_8.SetSizer(sizer_5)

        self.panel_4.SetSizer(grid_sizer_4)

        self.panel_7.SetSizer(sizer_7)

        self.panel_6.SetSizer(sizer_6)

        self.panel_5.SetSizer(grid_sizer_5)

        grid_sizer_2.AddGrowableRow(3)
        grid_sizer_2.AddGrowableCol(0)
        self.panel_18.SetSizer(grid_sizer_2)

        self.command.SetSizer(sizer_12)

        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(0)
        grid_sizer_1.AddGrowableCol(2)
        self.panel_1.SetSizer(grid_sizer_1)

        sizer_1.AddGrowableRow(0)
        sizer_1.AddGrowableCol(0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.button_CANCEL.GetId())

        self.Layout()
        self.Centre()

        self.choice_1.Bind(wx.EVT_CHOICE, self.onCommandType)
        self.choice_3.Bind(wx.EVT_CHOICE, self.onDeviceState)
        self.button_OK.Bind(wx.EVT_BUTTON, self.OnClose)
        self.button_CANCEL.Bind(wx.EVT_BUTTON, self.OnClose)

        self.datepicker_ctrl_1.Bind(wx.adv.EVT_DATE_CHANGED, self.onStartDateTime)
        self.timepicker_ctrl_2.Bind(wx.adv.EVT_TIME_CHANGED, self.onStartDateTime)

        self.datepicker_ctrl_3.Bind(wx.adv.EVT_DATE_CHANGED, self.onEndDateTime)
        self.timepicker_ctrl_4.Bind(wx.adv.EVT_TIME_CHANGED, self.onEndDateTime)

        self.datepicker_ctrl_5.Bind(wx.adv.EVT_DATE_CHANGED, self.onWinStartDateTime)
        self.timepicker_ctrl_6.Bind(wx.adv.EVT_TIME_CHANGED, self.onWinStartDateTime)

        self.datepicker_ctrl_7.Bind(wx.adv.EVT_DATE_CHANGED, self.onWinEndDateTime)
        self.timepicker_ctrl_8.Bind(wx.adv.EVT_TIME_CHANGED, self.onWinEndDateTime)

        self.choice_4.Bind(wx.EVT_CHOICE, self.onScheduleType)

        self.startDateTime = None
        self.endDateTime = None
        self.winStartDateTime = None
        self.winEndDateTime = None
        # self.SetSize((500, 400))
        # self.SetTitle(title)
        # emptyJson = "{\n\n}"

        # sizer_1 = wx.BoxSizer(wx.VERTICAL)

        # self.panel_1 = wx.Panel(self, wx.ID_ANY)
        # sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)

        # sizer_2 = wx.BoxSizer(wx.VERTICAL)

        # grid_sizer_1 = wx.GridSizer(2, 1, 0, 0)
        # sizer_2.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        # self.window_1 = wx.SplitterWindow(self.panel_1, wx.ID_ANY)
        # self.window_1.SetMinimumPaneSize(20)
        # grid_sizer_1.Add(self.window_1, 1, wx.ALL | wx.EXPAND, 5)

        # self.window_1_pane_1 = wx.Panel(self.window_1, wx.ID_ANY)

        # sizer_7 = wx.BoxSizer(wx.VERTICAL)

        # label_1 = wx.StaticText(self.window_1_pane_1, wx.ID_ANY, "Enter Cmd Args JSON:")
        # label_1.SetFont(
        #     wx.Font(
        #         11,
        #         wx.FONTFAMILY_DEFAULT,
        #         wx.FONTSTYLE_NORMAL,
        #         wx.FONTWEIGHT_LIGHT,
        #         0,
        #         "",
        #     )
        # )
        # sizer_7.Add(label_1, 0, wx.ALL, 5)

        # self.panel_2 = wx.Panel(self.window_1_pane_1, wx.ID_ANY)
        # sizer_7.Add(self.panel_2, 1, wx.ALL | wx.EXPAND, 5)

        # sizer_3 = wx.GridSizer(1, 1, 0, 0)

        # self.text_ctrl_1 = wx.TextCtrl(
        #     self.panel_2, wx.ID_ANY, emptyJson, style=wx.TE_MULTILINE
        # )
        # self.text_ctrl_1.SetFocus()
        # sizer_3.Add(self.text_ctrl_1, 0, wx.EXPAND, 0)

        # self.window_1_pane_2 = wx.Panel(self.window_1, wx.ID_ANY)

        # sizer_8 = wx.BoxSizer(wx.VERTICAL)

        # label_3 = wx.StaticText(
        #     self.window_1_pane_2, wx.ID_ANY, "Enter Schedule Args JSON:"
        # )
        # label_3.SetFont(
        #     wx.Font(
        #         11,
        #         wx.FONTFAMILY_DEFAULT,
        #         wx.FONTSTYLE_NORMAL,
        #         wx.FONTWEIGHT_LIGHT,
        #         0,
        #         "",
        #     )
        # )
        # sizer_8.Add(label_3, 0, wx.ALL, 5)

        # self.panel_4 = wx.Panel(self.window_1_pane_2, wx.ID_ANY)
        # sizer_8.Add(self.panel_4, 1, wx.ALL | wx.EXPAND, 5)

        # sizer_9 = wx.GridSizer(1, 1, 0, 0)

        # self.text_ctrl_2 = wx.TextCtrl(
        #     self.panel_4, wx.ID_ANY, emptyJson, style=wx.TE_MULTILINE
        # )
        # sizer_9.Add(self.text_ctrl_2, 0, wx.EXPAND, 0)

        # self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        # grid_sizer_1.Add(self.panel_3, 1, wx.ALL | wx.EXPAND, 5)

        # sizer_5 = wx.BoxSizer(wx.VERTICAL)

        # label_2 = wx.StaticText(self.panel_3, wx.ID_ANY, "Command Type")
        # label_2.SetFont(
        #     wx.Font(
        #         11,
        #         wx.FONTFAMILY_DEFAULT,
        #         wx.FONTSTYLE_NORMAL,
        #         wx.FONTWEIGHT_LIGHT,
        #         0,
        #         "",
        #     )
        # )
        # sizer_5.Add(label_2, 0, wx.ALL, 5)

        # self.cmdTypeBox = wx.ComboBox(
        #     self.panel_3,
        #     wx.ID_ANY,
        #     choices=Globals.COMMAND_TYPES,
        #     style=wx.CB_DROPDOWN | wx.CB_READONLY | wx.CB_SIMPLE | wx.CB_SORT,
        # )
        # sizer_5.Add(self.cmdTypeBox, 0, wx.ALL | wx.SHAPED, 5)

        # static_line_1 = wx.StaticLine(self.panel_1, wx.ID_ANY)
        # sizer_2.Add(static_line_1, 0, wx.EXPAND, 0)

        # sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        # sizer_2.Add(sizer_4, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        # self.okBtn = wx.Button(self.panel_1, wx.ID_OK, "OK")
        # sizer_4.Add(self.okBtn, 0, wx.ALL, 5)

        # sizer_4.Add((20, 20), 0, wx.ALL, 5)

        # self.cancelBtn = wx.Button(self.panel_1, wx.ID_CANCEL, "Cancel")
        # sizer_4.Add(self.cancelBtn, 0, wx.ALL, 5)

        # self.panel_3.SetSizer(sizer_5)

        # self.panel_4.SetSizer(sizer_9)

        # self.window_1_pane_2.SetSizer(sizer_8)

        # self.panel_2.SetSizer(sizer_3)

        # self.window_1_pane_1.SetSizer(sizer_7)

        # self.window_1.SplitVertically(self.window_1_pane_1, self.window_1_pane_2)

        # self.panel_1.SetSizer(sizer_2)

        # self.okBtn.Bind(wx.EVT_BUTTON, self.OnClose)
        # self.cancelBtn.Bind(wx.EVT_BUTTON, self.OnClose)

        # self.SetSizer(sizer_1)

        # self.Layout()
        # self.Centre()

    def onCommandType(self, event):
        type = event.String
        self.choice_2.Enable(False)
        self.choice_3.Enable(False)
        self.text_ctrl_2.Enable(False)
        self.text_ctrl_3.Enable(False)
        self.text_ctrl_4.Enable(False)
        if type.lower() == "set_app_state":
            self.choice_2.Enable(True)
            self.text_ctrl_2.Enable(True)
            self.text_ctrl_3.Enable(True)
        elif type.lower() == "set_device_lockdown_state":
            self.choice_3.Enable(True)
        elif type.lower() == "set_kiosk_app":
            self.text_ctrl_2.Enable(True)
            self.text_ctrl_3.Enable(True)

    def onDeviceState(self, event):
        state = event.String
        if state.lower() == "locked":
            self.text_ctrl_4.Enable(True)
        else:
            self.text_ctrl_4.Enable(False)
            self.text_ctrl_4.SetValue("")

    def onScheduleType(self, event):
        type = event.String

    def onStartDateTime(self, event):
        datetime.now(tz.tzutc()).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.startDateTime = None

        self.startDateTime = datetime(
            self.datepicker_ctrl_1.GetValue().GetYear(),
            self.datepicker_ctrl_1.GetValue().GetMonth(),
            self.datepicker_ctrl_1.GetValue().GetDay(),
            hour=self.timepicker_ctrl_2.GetValue().GetHour(),
            second=self.timepicker_ctrl_2.GetValue().GetSecond(),
            tzinfo=tz.tzutc(),
        )

    def onEndDateTime(self, event):
        self.endDateTime = datetime(
            self.datepicker_ctrl_3.GetValue().GetYear(),
            self.datepicker_ctrl_3.GetValue().GetMonth(),
            self.datepicker_ctrl_3.GetValue().GetDay(),
            hour=self.timepicker_ctrl_4.GetValue().GetHour(),
            second=self.timepicker_ctrl_4.GetValue().GetSecond(),
            tzinfo=tz.tzutc(),
        )

    def onWinStartDateTime(self, event):
        self.winStartDateTime = datetime(
            self.datepicker_ctrl_7.GetValue().GetYear(),
            self.datepicker_ctrl_7.GetValue().GetMonth(),
            self.datepicker_ctrl_7.GetValue().GetDay(),
            hour=self.timepicker_ctrl_6.GetValue().GetHour(),
            second=self.timepicker_ctrl_6.GetValue().GetSecond(),
            tzinfo=tz.tzutc(),
        )

    def onWinEndDateTime(self, event):
        self.winEndDateTime = datetime(
            self.datepicker_ctrl_7.GetValue().GetYear(),
            self.datepicker_ctrl_7.GetValue().GetMonth(),
            self.datepicker_ctrl_7.GetValue().GetDay(),
            hour=self.timepicker_ctrl_8.GetValue().GetHour(),
            second=self.timepicker_ctrl_8.GetValue().GetSecond(),
            tzinfo=tz.tzutc(),
        )

    def GetValue(self):
        command_args = V0CommandArgs(
            app_state=self.choice_2.GetStringSelection(),
            app_version=self.text_ctrl_3.GetValue(),
            device_alias_name=None,
            custom_settings_config=self.text_ctrl_1.GetValue(),
            package_name=self.text_ctrl_2.GetValue(),
            policy_url=None,
            state=self.choice_3.GetStringSelection().upper(),
            message=self.text_ctrl_4.GetValue(),
            wifi_access_points=None,
        )
        schedule_args = V0CommandScheduleArgs(
            name=self.choice_1.GetStringSelection(),
            start_datetime=self.startDateTime,
            end_datetime=self.endDateTime,
            time_type=self.choice_5.GetStringSelection(),
            window_start_time=self.winStartDateTime,
            window_end_time=self.winEndDateTime,
            days=list(self.check_list_box_1.GetCheckedStrings()),
        )
        return (
            command_args,
            self.choice_1.GetStringSelection(),
            schedule_args,
            self.choice_4.GetStringSelection(),
        )

    def OnClose(self, event):
        if self.IsModal():
            self.EndModal(event.EventObject.Id)
        else:
            self.Close()
