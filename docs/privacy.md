# Privacy

Boomerang runs entirely on your computer. Its author runs no server and receives no data: no
Boomerang account, no telemetry, no usage statistics, no crash reports sent anywhere.

## Data handled

- Received from your iPhone over Bluetooth: notifications, SMS and iMessage messages (text,
  sender, date), contacts and their pictures, call history, music and battery state.
- Exchanged directly with Apple's servers: iCloud mail, calendars, reminders and contacts, iCloud
  Drive files and iCloud Photos.
- AirPods: battery, settings and name, read over Bluetooth.

## Where it is stored

| Data | Location |
|---|---|
| Messages, iPhone contacts, contact pictures, call history, drafts | `~/.local/share/boomerang/messages/` (folder 0700, files 0600, readable by your account only) |
| iPhone notifications | in memory only, never written to disk |
| Settings (modules, per-app choices, headphones) | `~/.config/boomerang/` |
| iCloud Drive and Photos configuration | `~/.config/boomerang/rclone.conf`, encrypted by rclone |
| iCloud Drive and Photos file cache | `~/.cache/rclone/` (rclone's cache, at most 5 GB and 7 days by default, adjustable) |
| Passwords and encryption key | your session keyring (GNOME Keyring) |
| iCloud accounts (mail, calendars, contacts) | Evolution Data Server: `~/.config/evolution/sources/`, cache in `~/.cache/evolution/` and `~/.local/share/evolution/` |

Boomerang's logs (`journalctl --user -u boomerangd`) record events and counts, never message text,
names or phone numbers.

## Network

Only between your computer and Apple (iCloud), under Apple's terms. Bluetooth links the computer
and the iPhone without going through the Internet. Three other network accesses exist:

- icons of the iPhone apps that send notifications: Boomerang asks Apple's public App Store
  lookup service for the icon of an app, sending only its identifier (for example
  `net.whatsapp.WhatsApp`), never the content of a notification. Icons are kept in
  `~/.cache/boomerang/app-icons/`. To turn this off, set `app-icons=false` in the
  `[notifications]` group of `~/.config/boomerang/boomerangd.conf`;
- artwork of what the iPhone is playing (Now Playing): the iPhone does not send it, so
  Boomerang asks Apple's public iTunes Search service with the artist and the title only,
  and keeps the image only when both match. Artwork is kept in `~/.cache/boomerang/artwork/`.
  To turn this off, set `artwork=false` in the `[media]` group of
  `~/.config/boomerang/boomerangd.conf`;
- downloading rclone from <https://downloads.rclone.org>, when you ask for it.

## Deletion

1. In Boomerang, turn the modules off and sign out of iCloud in Apple Services.
2. Delete `~/.local/share/boomerang/`, `~/.config/boomerang/`, `~/.cache/boomerang/` and `~/.cache/rclone/`.
3. In Passwords and Keys, delete the "Boomerang" and "iCloud" entries.

Uninstalling the package does not remove these files.

Messages and contacts of the people you talk to remain your responsibility: do not share these
files.
