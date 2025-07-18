#!/usr/bin/env python3
"""
Script to create a Mac .app bundle for the PacMan game.
This makes the game feel more native on macOS.
"""

import os
import shutil
import stat

def create_mac_app():
    app_name = "PacMan"
    app_dir = f"{app_name}.app"
    
    # Create app bundle structure
    contents_dir = os.path.join(app_dir, "Contents")
    macos_dir = os.path.join(contents_dir, "MacOS")
    resources_dir = os.path.join(contents_dir, "Resources")
    
    # Remove existing app if it exists
    if os.path.exists(app_dir):
        shutil.rmtree(app_dir)
    
    # Create directories
    os.makedirs(macos_dir)
    os.makedirs(resources_dir)
    
    # Create Info.plist
    info_plist = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>{app_name}</string>
    <key>CFBundleIdentifier</key>
    <string>com.example.pacman</string>
    <key>CFBundleName</key>
    <string>{app_name}</string>
    <key>CFBundleDisplayName</key>
    <string>PacMan Game</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>CFBundleSignature</key>
    <string>????</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.9</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>'''
    
    with open(os.path.join(contents_dir, "Info.plist"), "w") as f:
        f.write(info_plist)
    
    # Create launcher script
    launcher_script = f'''#!/bin/bash
cd "$(dirname "$0")/../Resources"
python3 pacman_game.py
'''
    
    launcher_path = os.path.join(macos_dir, app_name)
    with open(launcher_path, "w") as f:
        f.write(launcher_script)
    
    # Make launcher executable
    st = os.stat(launcher_path)
    os.chmod(launcher_path, st.st_mode | stat.S_IEXEC)
    
    # Copy game files to Resources
    shutil.copy("pacman_game.py", resources_dir)
    shutil.copy("requirements.txt", resources_dir)
    if os.path.exists("README.md"):
        shutil.copy("README.md", resources_dir)
    
    print(f"✅ Created {app_dir}")
    print(f"🎮 You can now run the game by double-clicking {app_dir}")
    print("📱 The app bundle makes it feel like a native Mac application!")

if __name__ == "__main__":
    create_mac_app()