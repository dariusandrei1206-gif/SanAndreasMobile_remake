[app]
title = San Andreas Python Edition
package.name = sanandreaspython
package.domain = org.cartergames
source.dir = .
source.include_exts = py,json,png,jpg,kv,atlas,txt
version = 0.2.0
requirements = python3,kivy
orientation = landscape
fullscreen = 1
android.permissions =
android.api = 35
android.minapi = 23
android.ndk = 27b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
