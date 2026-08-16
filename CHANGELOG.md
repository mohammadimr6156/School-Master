# Changelog

All notable changes to **School Master** will be documented in this file.

## [v1.2] - 2026-08-17
### Changed
- Removed external Google Fonts dependencies (Vazirmatn) and switched to local system fonts (Segoe UI, Tahoma) to make the application fully functional without an internet connection.
- Updated Excel export to use Tahoma instead of Vazirmatn for reliable fallback.
- Updated README typography.

## [v1.1] - 2026-08-17
### Added
- Prepared application for `.exe` packaging using PyInstaller.
- Fixed taskbar icon grouping in Windows using AppUserModelID.
- Modified paths handling to safely preserve user data (`data.json`) outside PyInstaller's temporary directories.

## [v1.0] - 2026-08-16
- Initial release of School Master — school scheduling and planning system.
- Persian-language interface using pywebview.
- Single-file frontend (index.html) with embedded HTML/CSS/JS.
- main.py controls the application window.
- data.json serves as the local database.
