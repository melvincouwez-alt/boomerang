# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2026 melvincouwez-alt
"""The microphone muted for a call is always given back (no PipeWire touched): python3 -m unittest"""

import os
import tempfile
import unittest
from unittest import mock

from covalenced import calls


class CallMuteTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.mkdtemp()
        self.mark = os.path.join(tmp, "covalence", "microphone-muted")
        self.commands = []
        patches = [
            mock.patch.object(calls, "MUTE_MARK", self.mark),
            mock.patch.object(calls.GLib, "spawn_command_line_sync", self._spawn),
            mock.patch.object(calls, "log", lambda *_: None),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    def _spawn(self, command):
        self.commands.append(command)
        return True, b"Volume: 0.50", b"", 0

    def _calls(self):
        c = calls.Calls(None, None, mock.Mock(), lambda: None)
        c.notifications = {}
        return c

    def test_late_mute_after_call_is_ignored(self):
        c = self._calls()
        c.set_muted(True)
        self.assertFalse(c.muted)
        self.assertEqual(self.commands, [])

    def test_mute_then_end_restores_in_order(self):
        c = self._calls()
        c.calls["/call"] = {"State": "active"}
        c.set_muted(True)
        self.assertTrue(os.path.exists(self.mark))
        c.calls["/call"]["State"] = "disconnected"
        c._call_gone("/call")
        self.assertEqual(self.commands[-1], "wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0")
        self.assertFalse(os.path.exists(self.mark))

    def test_stale_mute_undone_at_start(self):
        os.makedirs(os.path.dirname(self.mark))
        with open(self.mark, "w") as mark:
            mark.write("0")
        self._calls()
        self.assertEqual(self.commands, ["wpctl set-mute @DEFAULT_AUDIO_SOURCE@ 0"])
        self.assertFalse(os.path.exists(self.mark))

    def test_already_muted_microphone_stays_muted(self):
        os.makedirs(os.path.dirname(self.mark))
        with open(self.mark, "w") as mark:
            mark.write("1")
        self._calls()
        self.assertEqual(self.commands, [])


if __name__ == "__main__":
    unittest.main()
